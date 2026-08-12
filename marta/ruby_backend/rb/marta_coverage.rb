#!/usr/bin/env ruby
# frozen_string_literal: true

# MARTA Ruby coverage helper.
#
# Runs a set of spec files under Ruby's built-in Coverage module (the engine
# SimpleCov wraps) and emits per-line hit counts for the code under test as JSON
# on stdout. The Python side intersects these per-line hits with each method's
# line range (from marta_parse.rb) to synthesise per-method missing_lines — the
# structure coverage.py hands the original MARTA for free.
#
#   ruby marta_coverage.rb <source_abs_dir> <spec1> [spec2 ...]
#
# `lines` is an array indexed by (line - 1): an integer hit count, or null for
# non-executable lines. RSpec's own output goes to stderr so stdout stays pure
# JSON. Exit code is 0 even if some examples fail (coverage is still valid).

require "coverage"
Coverage.start(lines: true, branches: true)

require "json"

# --isolated: ignora o .rspec do projeto (specs gerados sao auto-contidos);
# sem a flag, corre com a config do projeto (medicao de suites humanas).
isolated = ARGV.delete("--isolated") ? true : false
# --minitest: os ficheiros de teste sao Minitest (nao RSpec).
minitest_mode = ARGV.delete("--minitest") ? true : false
source_dir = ARGV.shift
# .dup é essencial: o modo minitest faz ARGV.clear (Minitest.run parseia ARGV),
# e sem a cópia isso esvaziaria também esta lista — nenhum teste era carregado.
specs = ARGV.dup

if source_dir.nil? || specs.empty?
  warn "usage: ruby marta_coverage.rb <source_abs_dir> <spec1> [spec2 ...]"
  exit 2
end

# realpath, não expand_path: o Coverage reporta caminhos com os symlinks já
# resolvidos. No macOS /var é symlink de /private/var, por isso um source_dir
# em /var/folders (o que o mkdtemp devolve) nunca casava com os caminhos
# reportados em /private/var/folders — e a medição devolvia ZERO ficheiros,
# silenciosamente. Resolver dos dois lados evita o falso 0%.
source_dir = begin
  File.realpath(File.expand_path(source_dir))
rescue StandardError
  File.expand_path(source_dir)
end
$LOAD_PATH.unshift(source_dir)
# Suites humanas carregam helpers a partir da própria pasta de testes
# (`require "test_helper"` / `"spec_helper"`) — é o que o `rake test -Ilib -Itest`
# faz. Sem isto, medir a suite de um projeto minitest falha com LoadError.
%w[test spec].each do |d|
  p = File.expand_path(d, Dir.pwd)
  $LOAD_PATH.unshift(p) if File.directory?(p)
end

def emit_coverage(source_dir)
  result = Coverage.result
  files = {}
  prefix = source_dir + File::SEPARATOR
  result.each do |path, data|
    next unless path.start_with?(prefix)
    # Ramos: o Coverage devolve {[:if, id, l, c, el, ec] => {[:then, ...] => n}}.
    # Chaves de array não sobrevivem a JSON, e para atribuir um ramo a um método
    # só precisamos da LINHA onde ele começa e de quantas vezes correu. Achatamos
    # para pares [linha, execuções]; execuções == 0 é ramo não tomado.
    branches = []
    (data[:branches] || {}).each_value do |targets|
      targets.each { |tgt, count| branches << [tgt[2], count] }
    end
    files[path[prefix.length..]] = { "lines" => data[:lines], "branches" => branches }
  end
  $stdout.write(JSON.generate({ "source_dir" => source_dir, "files" => files }))
end

if minitest_mode
  require "minitest"
  # Silence Minitest's own console output (stdout must stay pure JSON) and emit
  # coverage only AFTER the suite runs — minitest executes via autorun's at_exit.
  module Minitest
    def self.plugin_marta_cov_options(_opts, _options); end

    def self.plugin_marta_cov_init(_options)
      reporter.reporters.clear
    end
  end
  Minitest.extensions << "marta_cov"
  Minitest.after_run { emit_coverage(source_dir) }
  ARGV.clear
  specs.each { |f| require File.expand_path(f) }
else
  require "rspec/core"
  # Keep stdout clean for JSON — send RSpec's report to stderr.
  rspec_args = isolated ? ["-O", "/dev/null", *specs] : specs
  RSpec::Core::Runner.run(rspec_args, $stderr, $stderr)
  emit_coverage(source_dir)
end

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
require "rspec/core"

# --isolated: ignora o .rspec do projeto (specs gerados sao auto-contidos);
# sem a flag, corre com a config do projeto (medicao de suites humanas).
isolated = ARGV.delete("--isolated") ? true : false
source_dir = ARGV.shift
specs = ARGV

if source_dir.nil? || specs.empty?
  warn "usage: ruby marta_coverage.rb <source_abs_dir> <spec1> [spec2 ...]"
  exit 2
end

source_dir = File.expand_path(source_dir)
$LOAD_PATH.unshift(source_dir)

# Keep stdout clean for JSON — send RSpec's report to stderr.
rspec_args = isolated ? ["-O", "/dev/null", *specs] : specs
RSpec::Core::Runner.run(rspec_args, $stderr, $stderr)

result = Coverage.result
files = {}
prefix = source_dir + File::SEPARATOR
result.each do |path, data|
  next unless path.start_with?(prefix)
  rel = path[prefix.length..]
  files[rel] = { "lines" => data[:lines] }
end

$stdout.write(JSON.generate({ "source_dir" => source_dir, "files" => files }))

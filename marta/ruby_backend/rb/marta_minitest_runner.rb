#!/usr/bin/env ruby
# frozen_string_literal: true

# MARTA Minitest runner helper.
#
# Minitest ships in the Ruby standard library but has no JSON reporter, so we
# install our own (a Minitest plugin built on AbstractReporter) and emit results
# in the SAME shape as `rspec -f json`, so the Python side treats both
# frameworks uniformly:
#
#   {"examples":[{"id","description","full_description","status","file_path",
#                 "line_number","exception":{"message"}}],
#    "summary":{"example_count","failure_count","errors_outside_of_examples_count"}}
#
#   ruby marta_minitest_runner.rb <test_file.rb> [-I dir ...]
#
# Exit code follows Minitest (0 = all green). No external gems required.

require "json"
require "minitest"

files = []
args = ARGV.dup
while (a = args.shift)
  if a == "-I"
    $LOAD_PATH.unshift(File.expand_path(args.shift.to_s))
  elsif a.start_with?("-I")
    $LOAD_PATH.unshift(File.expand_path(a[2..]))
  else
    files << a
  end
end
# Minitest.run parses ARGV itself — clear it so our paths aren't read as options.
ARGV.clear

if files.empty?
  warn "usage: ruby marta_minitest_runner.rb <test_file.rb> [-I dir ...]"
  exit 2
end

MARTA_RESULTS = []
MARTA_STATE = { load_error: nil }

class MartaJsonReporter < Minitest::AbstractReporter
  def record(result)
    failure = result.failures.first
    status =
      if result.skipped? then "pending"
      elsif failure.nil? then "passed"
      else "failed"
      end
    klass = result.respond_to?(:klass) ? result.klass : result.class.name
    # Recover the `def test_x` definition site so the Python salvage can map a
    # failing test onto its line range (as it does with RSpec `it` blocks).
    file, line = begin
      Object.const_get(klass).instance_method(result.name).source_location
    rescue StandardError
      [nil, nil]
    end
    MARTA_RESULTS << {
      "id" => "#{klass}##{result.name}",
      "description" => result.name.to_s,
      "full_description" => "#{klass} #{result.name}",
      "status" => status,
      "file_path" => file,
      "line_number" => line,
      "exception" => failure.nil? ? nil : { "message" => failure.message.to_s },
    }
  end

  # AbstractReporter#passed? is `true` by default — without this, Minitest's
  # autorun would exit 0 even with failures.
  def passed?
    MARTA_RESULTS.none? { |r| r["status"] == "failed" }
  end
end

# Minitest plugin: replace the default reporters so nothing pollutes stdout.
module Minitest
  def self.plugin_marta_options(_opts, _options); end

  def self.plugin_marta_init(_options)
    reporter.reporters.clear
    reporter << MartaJsonReporter.new
  end
end
Minitest.extensions << "marta"

Minitest.after_run do
  failures = MARTA_RESULTS.count { |r| r["status"] == "failed" }
  payload = {
    "examples" => MARTA_RESULTS,
    "summary" => {
      "example_count" => MARTA_RESULTS.size,
      "failure_count" => failures,
      "errors_outside_of_examples_count" => MARTA_STATE[:load_error] ? 1 : 0,
    },
  }
  payload["load_error"] = MARTA_STATE[:load_error] if MARTA_STATE[:load_error]
  $stdout.write(JSON.generate(payload))
end

# Loading the test files triggers minitest/autorun, whose at_exit runs the
# suite (with our reporter) and then fires after_run above.
begin
  files.each { |f| require File.expand_path(f) }
rescue Exception => e # rubocop:disable Lint/RescueException
  MARTA_STATE[:load_error] = "#{e.class}: #{e.message}"
  # No suite to run: emit now and bail with a failing status.
  $stdout.write(JSON.generate({
    "examples" => [],
    "summary" => { "example_count" => 0, "failure_count" => 0,
                   "errors_outside_of_examples_count" => 1 },
    "load_error" => MARTA_STATE[:load_error],
  }))
  exit 1
end

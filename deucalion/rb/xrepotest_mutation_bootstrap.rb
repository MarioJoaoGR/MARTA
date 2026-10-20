# frozen_string_literal: true
# Inspect, assert and record the actual environment before Mutant runs tests.
# Mutation generation, selection algorithms and scoring remain Mutant 0.15.1.
require 'json'
require 'mutant'
expected = JSON.parse(File.read(ARGV.shift))
raise 'Expected Mutant 0.15.1' unless Mutant::VERSION == '0.15.1'
check = Module.new do
  define_method(:bootstrap) do
    super().fmap do |env|
      subjects = env.subjects.map do |subject|
        { 'subject' => subject.expression.syntax,
          'file' => File.realpath(subject.source_path.to_s),
          'start_line' => subject.source_lines.begin,
          'end_line' => subject.source_lines.end }
      end
      index = env.integration.send(:all_tests_index)
      examples = index.map do |test, example|
        m = example.metadata
        { 'id' => test.id, 'file' => File.expand_path(m[:absolute_file_path] || m[:file_path]),
          'eligible' => env.integration.available_tests.include?(test),
          'selected' => env.selected_tests.include?(test) }
      end
      exact_subject = subjects.size == 1 && subjects.first == expected.slice('subject', 'file', 'start_line', 'end_line')
      suite = File.realpath(expected.fetch('suite'))
      exact_tests = !examples.empty? && examples.all? do |example|
        File.realpath(example.fetch('file')) == suite && example['eligible'] && example['selected']
      end
      audit = { 'subjects' => subjects, 'examples' => examples,
                'verified' => exact_subject && exact_tests,
                'mutations' => env.amount_mutations }
      File.write(expected.fetch('audit'), JSON.pretty_generate(audit) + "\n")
      raise 'Subject identity or supplied-suite isolation assertion failed' unless audit['verified']
      env
    end
  end
  private :bootstrap
end
Mutant::CLI::Command::Environment.prepend(check)
# Use the installed executable's existing CLI and mutation algorithm.
load Gem.bin_path('mutant', 'mutant-ruby')

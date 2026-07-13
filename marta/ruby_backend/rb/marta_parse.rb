#!/usr/bin/env ruby
# frozen_string_literal: true

# MARTA Ruby parser helper.
#
# Emits a JSON description of a Ruby source file — classes/modules and methods,
# each with source line ranges and typed parameter lists — on stdout. It is the
# Ruby-side counterpart to what Python's `ast` gives the original MARTA, and is
# consumed by the Python RubyBackend via subprocess.
#
#   ruby marta_parse.rb path/to/file.rb        # JSON for one file on stdout
#   ruby marta_parse.rb --stdin < file.rb      # read source from stdin
#
# Requires Prism (Ruby standard library from 3.3; default parser from 3.4).
# Parse errors do NOT abort: whatever was recoverable is emitted, with the
# error list under "errors" (exit code stays 0 so the caller can decide).

require "prism"
require "json"

module MartaParse
  # Flatten a ParametersNode into MARTA's language-neutral parameter model.
  # kinds: req (positional), opt (default), rest (*a), keyreq (k:), key (k: v),
  #        keyrest (**o), block (&b). Mirrors the distinctions coverage/prompts
  #        care about; the Python side maps these onto ArgMessage.
  def self.params(node)
    return [] if node.nil?
    out = []
    node.requireds.each { |p| out << { "name" => name_of(p), "kind" => "req" } }
    node.optionals.each { |p| out << { "name" => name_of(p), "kind" => "opt" } }
    if node.rest && node.rest.respond_to?(:name)
      out << { "name" => str_or_nil(node.rest.name), "kind" => "rest" }
    end
    # posts = required positionals appearing after a splat: `def f(a, *b, c)`
    node.posts.each { |p| out << { "name" => name_of(p), "kind" => "req" } }
    node.keywords.each do |p|
      kind = p.is_a?(Prism::OptionalKeywordParameterNode) ? "key" : "keyreq"
      out << { "name" => str_or_nil(p.name), "kind" => kind }
    end
    if node.keyword_rest && node.keyword_rest.respond_to?(:name)
      out << { "name" => str_or_nil(node.keyword_rest.name), "kind" => "keyrest" }
    end
    if node.block
      out << { "name" => str_or_nil(node.block.name), "kind" => "block" }
    end
    out
  end

  # RequiredParameterNode responds to :name; a destructuring param
  # (MultiTargetNode, e.g. `def f((a, b))`) does not — emit its source instead.
  def self.name_of(p)
    p.respond_to?(:name) ? str_or_nil(p.name) : p.slice
  end

  def self.str_or_nil(sym)
    sym.nil? ? nil : sym.to_s
  end

  class Walker < Prism::Visitor
    attr_reader :classes, :methods

    def initialize
      super
      @classes = []
      @methods = []
      @scope = []          # enclosing class/module names, e.g. ["Foo", "Bar"]
      @class_stack = []     # matching class/module hashes for mixin attribution
    end

    def owner
      @scope.empty? ? nil : @scope.join("::")
    end

    def visit_class_node(node)
      enter_namespace(node, "class")
    end

    def visit_module_node(node)
      enter_namespace(node, "module")
    end

    def enter_namespace(node, kind)
      name = node.name.to_s
      entry = {
        "name" => name,
        "qualified_name" => [owner, name].compact.join("::"),
        "kind" => kind,
        "superclass" => (kind == "class" && node.superclass ? node.superclass.slice : nil),
        "start_line" => node.location.start_line,
        "end_line" => node.location.end_line,
        "includes" => [],
        "extends" => [],
        "prepends" => [],
      }
      @classes << entry
      @scope.push(name)
      @class_stack.push(entry)
      visit_child_nodes(node)
      @class_stack.pop
      @scope.pop
    end

    def visit_def_node(node)
      # `def self.foo` / `def Klass.foo` carry a receiver; instance methods do not.
      receiver = node.receiver.nil? ? nil : node.receiver.slice
      @methods << {
        "name" => node.name.to_s,
        "owner" => owner,
        "receiver" => receiver,          # nil => instance method
        "singleton" => !node.receiver.nil?,
        "start_line" => node.location.start_line,
        "end_line" => node.location.end_line,
        "params" => MartaParse.params(node.parameters),
      }
      # Nested defs are legal but rare; recurse so we don't miss them.
      visit_child_nodes(node)
    end

    def visit_call_node(node)
      cur = @class_stack.last
      if cur && node.receiver.nil? &&
         %i[include extend prepend].include?(node.name) && node.arguments
        bucket = cur["#{node.name}s"]
        node.arguments.arguments.each { |arg| bucket << arg.slice }
      end
      visit_child_nodes(node)
    end
  end

  def self.analyze(source, path)
    result = Prism.parse(source)
    walker = Walker.new
    result.value.accept(walker)
    {
      "path" => path,
      "classes" => walker.classes,
      "methods" => walker.methods,
      "errors" => result.errors.map do |e|
        { "message" => e.message, "line" => e.location.start_line }
      end,
    }
  end
end

if $PROGRAM_NAME == __FILE__
  if ARGV[0] == "--stdin"
    src = $stdin.read
    path = ARGV[1] || "(stdin)"
  elsif ARGV[0] && !ARGV[0].start_with?("--")
    path = ARGV[0]
    src = File.read(path)
  else
    warn "usage: ruby marta_parse.rb <file.rb> | --stdin [name]"
    exit 2
  end
  puts JSON.generate(MartaParse.analyze(src, path))
end

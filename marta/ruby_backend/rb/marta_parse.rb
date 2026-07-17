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

    # RSpec example-defining calls whose blocks we may want to salvage/remove.
    EXAMPLE_CALLS = %i[it specify example scenario fit xit].freeze

    attr_reader :examples

    def initialize
      super
      @classes = []
      @methods = []
      @examples = []        # RSpec `it`/`specify`/... blocks with line ranges
      @scope = []          # enclosing class/module names, e.g. ["Foo", "Bar"]
      @class_stack = []     # matching class/module hashes for mixin attribution
      @method_stack = []    # current def(s): param names + members-called map
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
        "attributes" => [],   # methods created by attr_reader/writer/accessor
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
      params = MartaParse.params(node.parameters)
      # param_members: for each parameter, the methods invoked ON it in the body
      # (the Ruby duck-typing analogue of MARTA's attribute-access members —
      # used to guess a parameter's likely type by who responds to those calls).
      members = {}
      param_names = params.map { |p| p["name"] }.compact
      param_names.each { |n| members[n] = [] }
      calls = []   # every method call made in the body (for the call graph)
      @methods << {
        "name" => node.name.to_s,
        "owner" => owner,
        "receiver" => receiver,          # nil => instance method
        "singleton" => !node.receiver.nil?,
        "start_line" => node.location.start_line,
        "end_line" => node.location.end_line,
        "params" => params,
        "param_members" => members,
        "calls" => calls,
      }
      @method_stack.push({ names: param_names, members: members, calls: calls })
      visit_child_nodes(node)  # nested defs are legal but rare; recurse anyway
      @method_stack.pop
      members.each_value(&:uniq!)
    end

    def visit_call_node(node)
      cur = @class_stack.last
      if cur && node.receiver.nil? &&
         %i[include extend prepend].include?(node.name) && node.arguments
        bucket = cur["#{node.name}s"]
        node.arguments.arguments.each { |arg| bucket << arg.slice }
      end

      # attr_reader/writer/accessor create reader/writer methods — record them so
      # type inference knows the class responds to those names.
      if cur && node.receiver.nil? &&
         %i[attr_reader attr_writer attr_accessor].include?(node.name) && node.arguments
        node.arguments.arguments.each do |arg|
          next unless arg.is_a?(Prism::SymbolNode)
          nm = arg.value.to_s
          cur["attributes"] << nm if %i[attr_reader attr_accessor].include?(node.name)
          cur["attributes"] << "#{nm}=" if %i[attr_writer attr_accessor].include?(node.name)
        end
      end

      # Method invoked on a parameter (`param.foo`): record `foo` as a member
      # accessed on `param`, for type inference on the Python side.
      m = @method_stack.last
      if m && node.receiver.is_a?(Prism::LocalVariableReadNode)
        rname = node.receiver.name.to_s
        m[:members][rname] << node.name.to_s if m[:names].include?(rname)
      end

      # Record the call itself (name + receiver shape) for call-graph resolution.
      if m
        r = node.receiver
        if r.nil?
          kind = "none"; rname = nil
        elsif r.is_a?(Prism::SelfNode)
          kind = "self"; rname = nil
        elsif r.is_a?(Prism::ConstantReadNode) || r.is_a?(Prism::ConstantPathNode)
          kind = "const"; rname = r.slice
        elsif r.is_a?(Prism::LocalVariableReadNode)
          kind = "lvar"; rname = r.name.to_s
        else
          kind = "other"; rname = nil
        end
        m[:calls] << {
          "name" => node.name.to_s, "recv" => kind, "recv_name" => rname,
          "line" => node.location.start_line,
        }
      end

      # RSpec example blocks: `it "desc" do ... end`. Record the full call's
      # line range (the block is what gets removed when salvaging a failing
      # example) and its description, for the Python salvage step.
      if EXAMPLE_CALLS.include?(node.name) && node.block.is_a?(Prism::BlockNode)
        arg = node.arguments&.arguments&.first
        desc = arg.is_a?(Prism::StringNode) ? arg.unescaped : nil
        @examples << {
          "name" => node.name.to_s,
          "description" => desc,
          "start_line" => node.location.start_line,
          "end_line" => node.location.end_line,
        }
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
      "examples" => walker.examples,
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

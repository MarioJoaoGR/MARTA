# frozen_string_literal: true

# Closed-pattern evidence only; reuse the already parsed Prism tree.
module MartaStateFacts
  POLICY = "constructor-state-v1"
  MAX_ASSIGNMENTS = 64
  VALUES = %w[IntegerNode FloatNode RationalNode ImaginaryNode StringNode SymbolNode
              TrueNode FalseNode NilNode LocalVariableReadNode ConstantReadNode
              ConstantPathNode ArrayNode HashNode KeywordHashNode AssocNode
              ArgumentsNode RangeNode].freeze
  OPAQUE = %i[instance_variable_set remove_instance_variable instance_eval instance_exec
              class_eval module_eval eval allocate define_method define_singleton_method
              alias_method remove_method undef_method const_set remove_const refine using].freeze
  STRUCTURAL = %i[attr_reader attr_writer attr_accessor include extend prepend].freeze
  SENDS = %i[send public_send __send__].freeze

  def self.simple_value?(node)
    return true if node.nil?
    pending = [[node, 0]]
    visited = 0
    until pending.empty?
      current, depth = pending.pop
      visited += 1
      return false if visited > MartaReturnFacts::MAX_NODES || depth > MartaReturnFacts::MAX_DEPTH
      return false unless VALUES.include?(current.class.name.split("::").last)
      current.compact_child_nodes.each do |child|
        return false if visited + pending.length >= MartaReturnFacts::MAX_NODES
        pending << [child, depth + 1]
      end
    end
    true
  end

  def self.getter(node)
    body = node.body
    return nil unless body.is_a?(Prism::StatementsNode) && body.body.length == 1
    expression = body.body.first
    if expression.is_a?(Prism::ReturnNode)
      arguments = expression.arguments&.arguments
      return nil unless arguments && arguments.length == 1
      expression = arguments.first
    end
    return nil unless expression.is_a?(Prism::InstanceVariableReadNode)
    { "policy" => POLICY, "kind" => "instance_ivar", "ivar" => expression.name.to_s }
  end

  def self.constructor(node)
    if node.parameters
      defaults = node.parameters.optionals + node.parameters.keywords.select { |p| p.respond_to?(:value) }
      return nil if defaults.length > MAX_ASSIGNMENTS || !defaults.all? { |p| simple_value?(p.value) }
    end
    statements = node.body.is_a?(Prism::StatementsNode) ? node.body.body : []
    return nil if node.body && !node.body.is_a?(Prism::StatementsNode)
    return nil if statements.length > MAX_ASSIGNMENTS
    assignments = {}
    statements.each do |statement|
      return nil unless statement.is_a?(Prism::InstanceVariableWriteNode)
      value = statement.value
      fact = MartaReturnFacts.constructor_expression(value)
      if fact
        return nil unless simple_value?(value.arguments)
      else
        return nil unless simple_value?(value)
      end
      assignments[statement.name.to_s] = fact
    end
    { "closed" => true, "assignments" => assignments }
  end

  def self.for_class(node)
    readers, writers, constants = [], [], []
    closed = true
    statements = node.body.respond_to?(:body) ? node.body.body : []
    statements.each do |statement|
      if statement.is_a?(Prism::DefNode)
        closed &&= statement.receiver.nil? || statement.receiver.is_a?(Prism::SelfNode)
      elsif statement.is_a?(Prism::ConstantWriteNode)
        constants << statement.name.to_s
        closed &&= simple_value?(statement.value)
      elsif statement.is_a?(Prism::CallNode) && statement.receiver.nil? && statement.block.nil?
        arguments = statement.arguments&.arguments || []
        if %i[attr_reader attr_writer attr_accessor].include?(statement.name) &&
           arguments.all? { |arg| arg.is_a?(Prism::SymbolNode) && arg.value.match?(/\A[a-z_]\w*\z/) }
          names = arguments.map(&:value)
          readers.concat(names) if %i[attr_reader attr_accessor].include?(statement.name)
          writers.concat(names) if %i[attr_writer attr_accessor].include?(statement.name)
        elsif %i[private protected public].include?(statement.name) && arguments.empty?
          # Visibility does not change the stored object's class.
        else
          closed = false
        end
      else
        closed = false
      end
    end
    result = { "closed_body" => closed }
    result["readers"] = readers unless readers.empty?
    result["writers"] = writers unless writers.empty?
    result["constants"] = constants unless constants.empty?
    result
  end

  def self.opaque_call?(node)
    return true if OPAQUE.include?(node.name)
    return false unless SENDS.include?(node.name)
    argument = node.arguments&.arguments&.first
    name = if argument.is_a?(Prism::SymbolNode)
             argument.value
           elsif argument.is_a?(Prism::StringNode)
             argument.unescaped
           end
    name.nil? || OPAQUE.include?(name.to_sym) || SENDS.include?(name.to_sym)
  end
end

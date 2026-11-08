# frozen_string_literal: true

# Small syntactic facts only, sharing the existing Prism parse. No evaluation,
# global dataflow, call expansion or claims about runtime constructor dispatch.
module MartaReturnFacts
  POLICY = "direct-constructor-return-v1"
  MAX_NODES = 64
  MAX_DEPTH = 12
  TRANSFERS = %w[ReturnNode BreakNode NextNode RedoNode RetryNode YieldNode
                 SuperNode ForwardingSuperNode DefNode ClassNode ModuleNode
                 SingletonClassNode BlockNode LambdaNode].freeze

  def self.control_free?(node)
    return true if node.nil?
    pending = [[node, 0]]
    visited = 0
    until pending.empty?
      current, depth = pending.pop
      visited += 1
      return false if visited > MAX_NODES || depth > MAX_DEPTH
      return false if TRANSFERS.include?(current.class.name.split("::").last)
      current.compact_child_nodes.each do |child|
        return false if visited + pending.length >= MAX_NODES
        pending << [child, depth + 1]
      end
    end
    true
  end

  def self.constant_name(node)
    return nil unless node.is_a?(Prism::ConstantReadNode) || node.is_a?(Prism::ConstantPathNode)
    text = node.slice
    text.match?(/\A(?:::)?[A-Z]\w*(?:::[A-Z]\w*)*\z/) ? text : nil
  end

  def self.for_method(node)
    # Explicit receivers other than self are not bound to the lexical owner by
    # this parser's MethodInfo model; do not attach a return claim to that owner.
    return nil unless node.receiver.nil? || node.receiver.is_a?(Prism::SelfNode)
    body = node.body
    return nil unless body.is_a?(Prism::StatementsNode) && (1..MAX_DEPTH).cover?(body.body.length)
    return nil unless body.body[0...-1].all? { |statement| factory_prefix?(statement) }
    expression = body.body.last
    explicit = expression.is_a?(Prism::ReturnNode)
    if explicit
      args = expression.arguments&.arguments
      return nil unless args && args.length == 1
      expression = args.first
    end
    fact = constructor_expression(expression)
    if !fact && node.receiver.is_a?(Prism::SelfNode) && constructor_call?(expression) &&
       (expression.receiver.nil? || expression.receiver.is_a?(Prism::SelfNode))
      fact = { "policy" => POLICY, "kind" => "receiver_new",
               "line" => expression.location.start_line }
    end
    fact && fact.merge("explicit_return" => explicit)
  end

  def self.factory_prefix?(statement)
    if statement.is_a?(Prism::LocalVariableWriteNode)
      return control_free?(statement.value)
    end
    return false unless statement.is_a?(Prism::IfNode) || statement.is_a?(Prism::UnlessNode)
    return false if statement.compact_child_nodes.length != 2
    guard = statement.statements&.body
    return false unless guard&.length == 1 && control_free?(statement.predicate)
    call = guard.first
    call.is_a?(Prism::CallNode) && call.receiver.nil? &&
      [:raise, :fail].include?(call.name) && !call.block && control_free?(call.arguments)
  end

  def self.constructor_call?(expression)
    expression.is_a?(Prism::CallNode) && expression.name == :new &&
      !expression.safe_navigation? && !expression.block && control_free?(expression.arguments)
  end

  def self.constructor_expression(expression)
    return nil unless constructor_call?(expression)
    constant = constant_name(expression.receiver)
    return nil unless constant
    { "policy" => POLICY, "kind" => "constant_new", "constant" => constant,
      "line" => expression.location.start_line }
  end

  def self.receiver_call(node)
    return nil unless node.is_a?(Prism::CallNode)
    return nil if node.safe_navigation? || node.block || !control_free?(node.arguments)
    receiver = node.receiver
    if receiver.nil?
      kind = "none"; name = nil
    elsif receiver.is_a?(Prism::SelfNode)
      kind = "self"; name = nil
    elsif (name = constant_name(receiver))
      kind = "const"
    else
      return nil  # No recursive chain expansion in this first policy.
    end
    { "name" => node.name.to_s, "recv" => kind, "recv_name" => name,
      "line" => node.location.start_line }
  end
end

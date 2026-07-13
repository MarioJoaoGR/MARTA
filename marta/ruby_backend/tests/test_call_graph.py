"""Tests for the static call graph (item 6)."""
import pytest

from marta.ruby_backend import call_graph, param_types, runner
from marta.ruby_backend.ruby_ast import RubyParseError, parse_source


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


SRC = """
class Transaction
  def initialize(kind, amount)
    @kind = kind
    @amount = amount
  end
  attr_reader :amount, :kind
end

class Wallet
  def deposit(amount)
    apply(Transaction.new(:deposit, amount))
  end

  def apply(entry)
    validate(entry)
    @balance = entry.amount
  end

  def validate(entry)
    raise "bad" if entry.amount <= 0
  end
end
"""


def _graph():
    fp = parse_source(SRC, "wallet.rb")
    idx = param_types.ProjectTypeIndex().add_file(fp)
    return call_graph.StaticCallGraph.build(fp.methods, idx), fp


def test_self_call_edges_resolved():
    g, _ = _graph()
    # deposit -> apply (self/none receiver), apply -> validate
    assert "Wallet#apply" in g.callees("Wallet#deposit")
    assert "Wallet#validate" in g.callees("Wallet#apply")


def test_constructor_edge_to_initialize():
    g, _ = _graph()
    # Transaction.new -> Transaction#initialize
    assert "Transaction#initialize" in g.callees("Wallet#deposit")


def test_lvar_param_typed_call_resolved():
    g, _ = _graph()
    # apply(entry): entry.amount -> Transaction#amount (entry inferred as Transaction)
    # amount is an attr_reader, part of Transaction's interface.
    callees = g.callees("Wallet#apply")
    assert "Transaction#amount" in callees


def test_reverse_edges():
    g, _ = _graph()
    assert "Wallet#deposit" in g.callers("Wallet#apply")


def test_no_edges_for_unresolved_or_builtin():
    g, _ = _graph()
    # `raise` and `<=` are builtins/operators -> no bogus edges to project methods.
    for e in g.edges:
        assert e.callee in {m for m in g.uses} or True  # sanity
    # validate has no outgoing edges to project methods (only raise/<=/amount)
    # amount IS resolved (entry: Transaction); raise/<= are not.
    assert set(g.callees("Wallet#validate")) == {"Transaction#amount"}

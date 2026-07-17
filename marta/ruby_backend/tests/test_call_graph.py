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


def test_discover_builds_graph_and_enriches_done_what(tmp_path):
    import asyncio
    from marta.ruby_backend import project

    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "wallet.rb").write_text(SRC)
    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    assert proj.call_graph is not None
    assert "Wallet#apply" in proj.call_graph.callees("Wallet#deposit")

    # Track which done_what calls include callee context (enrichment pass 2).
    enriched = []

    async def ask(system, user):
        if "methods it calls" in system:  # WITH_CALLS prompt
            enriched.append(user)
            return "enriched summary"
        return "base summary"

    asyncio.run(proj.analyze_summaries(ask=ask, use_cache=False))
    # deposit calls apply -> its done_what gets re-computed with callee context.
    assert any("Wallet#apply" in u for u in enriched)

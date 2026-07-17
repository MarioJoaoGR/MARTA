"""Tests for the dynamic (TracePoint) call graph and static/dynamic comparison."""
import textwrap

import pytest

from marta.ruby_backend import call_graph, dyn_call_graph, param_types, runner
from marta.ruby_backend.ruby_ast import RubyParseError, parse_source


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


SRC = """\
class Transaction
  def initialize(kind, amount); @kind = kind; @amount = amount; end
  attr_reader :amount, :kind
end
class Wallet
  def deposit(amount); apply(Transaction.new(:deposit, amount)); end
  def apply(entry); validate(entry); @balance = entry.amount; end
  def validate(entry); raise "bad" if entry.amount <= 0; end
end
"""


def _project(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "wallet.rb").write_text(SRC)
    (tmp_path / "driver.rb").write_text('require "wallet"\nWallet.new.deposit(100)\n')
    return tmp_path


def test_dynamic_captures_exercised_edges(tmp_path):
    p = _project(tmp_path)
    g = dyn_call_graph.run_dynamic("src", str(p / "driver.rb"), cwd=str(p))
    assert "Wallet#apply" in g.callees("Wallet#deposit")
    assert "Transaction#initialize" in g.callees("Wallet#deposit")
    assert "Wallet#validate" in g.callees("Wallet#apply")


def test_dynamic_misses_c_level_attr_readers(tmp_path):
    p = _project(tmp_path)
    g = dyn_call_graph.run_dynamic("src", str(p / "driver.rb"), cwd=str(p))
    # attr_reader #amount is C-defined -> not traced by :call
    assert "Transaction#amount" not in g.callees("Wallet#apply")


def test_static_vs_dynamic_comparison(tmp_path):
    p = _project(tmp_path)
    fp = parse_source(SRC, "wallet.rb")
    idx = param_types.ProjectTypeIndex().add_file(fp)
    static_g = call_graph.StaticCallGraph.build(fp.methods, idx)
    dyn_g = dyn_call_graph.run_dynamic("src", str(p / "driver.rb"), cwd=str(p))

    cmp = dyn_call_graph.compare(static_g, dyn_g)
    # Method-to-method edges agree; the difference is the attr-accessor edges the
    # static graph adds and the dynamic one can't see.
    assert ("Wallet#deposit", "Wallet#apply") in cmp.both
    assert ("Wallet#apply", "Wallet#validate") in cmp.both
    assert ("Wallet#apply", "Transaction#amount") in cmp.static_only
    assert cmp.dynamic_only == set()  # dynamic saw nothing static missed here
    assert 0.0 <= cmp.agreement <= 1.0

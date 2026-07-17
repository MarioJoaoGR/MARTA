"""Tests for the function-level RAG (item 4), with a fake embedder.

A deterministic keyword-vector embedder keeps these fast and torch-free; the
real bge embedder is exercised only in an opt-in smoke test.
"""
import asyncio
import os

import pytest

from marta.ruby_backend import project, rag, runner
from marta.ruby_backend.ruby_ast import RubyParseError


# Fake embedder: bag-of-keywords vector over a fixed vocabulary. Similar text
# -> similar vector, enough to make top-k deterministic.
VOCAB = ["add", "sum", "subtract", "difference", "multiply", "product", "bank", "balance"]


def _vec(text):
    t = text.lower()
    return [float(t.count(w)) for w in VOCAB]


def _embed_documents(docs):
    return [_vec(d) for d in docs]


def _embed_query(q):
    return _vec(q)


class _T:
    """Minimal stand-in for MethodTarget (only what RAG reads)."""
    class _M:
        def __init__(self, qn):
            self.qualified_name = qn

    def __init__(self, qn, summary):
        self.method = self._M(qn)
        self.summary = summary
        self.done_what = ""


def _db():
    db = rag.RubyFunctionDatabase(_embed_documents, _embed_query)
    db.init([
        _T("Calc#add", "add two numbers and return the sum"),
        _T("Calc#subtract", "subtract to get the difference"),
        _T("Calc#multiply", "multiply to get the product"),
        _T("Bank#balance", "return the bank account balance"),
    ])
    return db


def test_query_returns_semantically_closest():
    db = _db()
    hits = db.query("compute the sum by adding numbers", k=1)
    assert hits[0].method.qualified_name == "Calc#add"


def test_query_excludes_self():
    db = _db()
    hits = db.query("add two numbers and return the sum", k=2, exclude="Calc#add")
    names = [h.method.qualified_name for h in hits]
    assert "Calc#add" not in names
    assert len(names) == 2


def test_related_lines_format():
    db = _db()
    lines = db.related_lines("bank balance", k=1)
    assert lines and lines[0].startswith("Bank#balance: ")


def test_empty_db_returns_nothing():
    db = rag.RubyFunctionDatabase(_embed_documents, _embed_query)
    db.init([])
    assert db.query("anything", k=3) == []


# --- wiring: RAG-derived related lines reach the Planner -------------------- #
def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_related_reaches_planner(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text(
        "class Calc\n  def add(a, b) = a + b\n  def sub(a, b) = a - b\nend\n"
    )
    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    proj.targets[0].summary = "add two numbers and return the sum"
    proj.targets[1].summary = "subtract to get the difference"
    proj.build_rag(_embed_documents, _embed_query)

    planner_prompts = []
    good = '''```ruby
require "calc"
RSpec.describe Calc do
  it "adds" do
    expect(Calc.new.add(2, 3)).to eq(5)
  end
end
```'''

    async def ask(system, user):
        if "Test Plan" in system:
            planner_prompts.append(user)
            return '[{"name":"a","desc":"x","setup":"None"}]'
        return good

    asyncio.run(proj.generate_all(ask=ask, limit=1))
    # The add method's Planner prompt should mention the related sub method.
    assert any("RELATED METHODS" in p and "Calc#sub" in p for p in planner_prompts)


@pytest.mark.skipif(
    os.getenv("MARTA_RAG_SMOKE") != "1", reason="set MARTA_RAG_SMOKE=1 to load bge"
)
def test_real_embedder_smoke():
    db = rag.RubyFunctionDatabase()  # real bge embedder
    db.init([
        _T("Calc#add", "add two numbers and return the sum"),
        _T("Bank#balance", "return the bank account balance"),
    ])
    hits = db.query("compute the total of two integers", k=1)
    assert hits[0].method.qualified_name == "Calc#add"

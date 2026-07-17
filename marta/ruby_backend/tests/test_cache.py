"""Tests for analysis caching (item 8)."""
import asyncio

import pytest

from marta.ruby_backend import cache, project, runner
from marta.ruby_backend.ruby_ast import RubyParseError


# --- hashing + roundtrip (no toolchain) ------------------------------------ #
def test_source_hash_changes_with_content(tmp_path):
    a = tmp_path / "a.rb"
    a.write_text("class A; end")
    h1 = cache.compute_source_hash([str(a)])
    a.write_text("class A; def x; end; end")
    h2 = cache.compute_source_hash([str(a)])
    assert h1 != h2


def test_save_load_roundtrip(tmp_path):
    p = cache.cache_path(str(tmp_path), "deepseek:16b")
    cache.save_analysis(p, "hash1", "deepseek:16b", {"A#x": {"summary": "s"}})
    assert cache.load_analysis(p, "hash1", "deepseek:16b") == {"A#x": {"summary": "s"}}
    # wrong hash or model -> miss
    assert cache.load_analysis(p, "other", "deepseek:16b") is None
    assert cache.load_analysis(p, "hash1", "other-model") is None


# --- cache hit skips the LLM ----------------------------------------------- #
def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_analyze_summaries_uses_cache_on_second_run(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "test-model")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "calc.rb").write_text("class Calc\n  def add(a, b) = a + b\nend\n")

    calls = {"n": 0}

    async def ask(system, user):
        calls["n"] += 1
        return "a summary"

    # First run: computes + saves cache.
    proj1 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    asyncio.run(proj1.analyze_summaries(ask=ask))
    first_calls = calls["n"]
    assert first_calls > 0
    assert proj1.targets[0].summary == "a summary"

    # Second run on unchanged source: cache hit, zero new LLM calls.
    proj2 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    asyncio.run(proj2.analyze_summaries(ask=ask))
    assert calls["n"] == first_calls               # no additional calls
    assert proj2.targets[0].summary == "a summary"  # loaded from cache


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_cache_invalidated_when_source_changes(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "test-model")
    (tmp_path / "src").mkdir()
    calc = tmp_path / "src" / "calc.rb"
    calc.write_text("class Calc\n  def add(a, b) = a + b\nend\n")

    calls = {"n": 0}

    async def ask(system, user):
        calls["n"] += 1
        return "s"

    proj1 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    asyncio.run(proj1.analyze_summaries(ask=ask))
    first = calls["n"]

    calc.write_text("class Calc\n  def add(a, b) = a + b + 1\nend\n")  # change source
    proj2 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    asyncio.run(proj2.analyze_summaries(ask=ask))
    assert calls["n"] > first  # cache invalidated -> recomputed


def test_call_graph_cache_roundtrip(tmp_path):
    from marta.ruby_backend.call_graph import CallEdge, CallGraph

    g = CallGraph(edges=[CallEdge("A#a", "A#b", 3, "self")])
    g._index()
    p = cache.call_graph_path(str(tmp_path))
    cache.save_call_graph(p, "h1", g.to_json())
    assert cache.load_call_graph(p, "other") is None       # hash mismatch -> miss
    loaded = cache.load_call_graph(p, "h1")
    g2 = CallGraph.from_json(loaded)
    assert "A#b" in g2.callees("A#a")

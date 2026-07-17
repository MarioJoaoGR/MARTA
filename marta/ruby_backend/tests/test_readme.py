"""Tests for README analysis -> what_todo (item 7)."""
import asyncio

import pytest

from marta.ruby_backend import project, readme, runner
from marta.ruby_backend.ruby_ast import RubyParseError


def _run(coro):
    return asyncio.run(coro)


# --- README location (no toolchain) ---------------------------------------- #
def test_nearest_readme_walks_up(tmp_path):
    (tmp_path / "README.md").write_text("root readme")
    (tmp_path / "a" / "b").mkdir(parents=True)
    (tmp_path / "a" / "README.md").write_text("a readme")
    # file in a/b -> nearest is a/README.md
    f = tmp_path / "a" / "b" / "x.rb"
    f.write_text("x")
    assert readme.nearest_readme(str(f), str(tmp_path)) == str(tmp_path / "a" / "README.md")
    # file directly under root -> root readme
    g = tmp_path / "y.rb"
    g.write_text("y")
    assert readme.nearest_readme(str(g), str(tmp_path)) == str(tmp_path / "README.md")


def test_nearest_readme_none_when_absent(tmp_path):
    (tmp_path / "src").mkdir()
    f = tmp_path / "src" / "x.rb"
    f.write_text("x")
    assert readme.nearest_readme(str(f), str(tmp_path / "src")) is None


def test_analyze_what_todo_uses_readme():
    seen = {}

    async def ask(system, user):
        seen["user"] = user
        return "intended to greet users"

    out = _run(readme.analyze_what_todo(ask, "def greet(u); end", "A greeting app"))
    assert out == "intended to greet users"
    assert "Project Overview" in seen["user"]
    assert "A greeting app" in seen["user"]


def test_overview_cache_analyzes_once(tmp_path):
    (tmp_path / "README.md").write_text("the project")
    (tmp_path / "a.rb").write_text("x")
    (tmp_path / "b.rb").write_text("y")
    calls = {"n": 0}

    async def ask(system, user):
        calls["n"] += 1
        return "overview"

    cache = readme.ReadmeOverviewCache(str(tmp_path))
    o1 = _run(cache.overview_for(ask, str(tmp_path / "a.rb")))
    o2 = _run(cache.overview_for(ask, str(tmp_path / "b.rb")))
    assert o1 == o2 == "overview"
    assert calls["n"] == 1  # same README analysed once


# --- wiring: what_todo flows into the merged summary ----------------------- #
def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_analyze_summaries_merges_what_todo(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "README.md").write_text("A calculator library")
    (tmp_path / "src" / "calc.rb").write_text("class Calc\n  def add(a, b) = a + b\nend\n")
    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()

    async def ask(system, user):
        if "README" in system:
            return "OVERVIEW: a calculator"
        if "intended to do" in system or "intended to do" in user:  # merge step
            return "MERGED SUMMARY"
        if "requirement" in system.lower() or "Project Overview" in user:
            return "WHAT_TODO: adds numbers"
        return "DONE_WHAT: returns a + b"

    _run(proj.analyze_summaries(ask))
    t = proj.targets[0]
    assert t.what_todo == "WHAT_TODO: adds numbers"
    assert t.summary == "MERGED SUMMARY"  # generate_summary merged both views

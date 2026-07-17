"""Tests for the two-perspective summary pipeline (item 3), stubbed LLM."""
import asyncio

import pytest

from marta.ruby_backend import project, runner, summaries
from marta.ruby_backend.ruby_ast import RubyParseError


def _run(coro):
    return asyncio.run(coro)


# --- summaries module (no toolchain) --------------------------------------- #
def test_done_what_source_only_prompt():
    seen = {}

    async def ask(system, user):
        seen["system"] = system
        seen["user"] = user
        return "does a thing"

    out = _run(summaries.analyze_done_what(ask, "def add(a, b) = a + b"))
    assert out == "does a thing"
    assert "methods it calls: \n" in seen["user"]  # empty call message
    assert "Ruby" in seen["system"]


def test_done_what_with_calls_uses_other_prompt():
    seen = {}

    async def ask(system, user):
        seen["system"] = system
        return "summary"

    _run(summaries.analyze_done_what(ask, "def f; g; end", called_summaries=["g: does g"]))
    assert "methods it calls" in seen["system"]


def test_generate_summary_skips_merge_without_what_todo():
    calls = {"n": 0}

    async def ask(system, user):
        calls["n"] += 1
        return "merged"

    out = _run(summaries.generate_summary(ask, "def x; end", done_what="did x"))
    assert out == "did x"       # returns done_what unchanged
    assert calls["n"] == 0      # no LLM call when there's nothing to merge


def test_generate_summary_merges_with_what_todo():
    async def ask(system, user):
        assert "What it is intended to do" in user
        return "final merged summary"

    out = _run(summaries.generate_summary(ask, "def x; end", "did x", what_todo="should x"))
    assert out == "final merged summary"


# --- wiring into the orchestrator ------------------------------------------ #
def _toolchain_ok() -> bool:
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_analyze_summaries_populates_targets_and_reaches_planner(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calculator.rb").write_text(
        "class Calculator\n  def add(a, b) = a + b\nend\n"
    )
    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()

    async def summ_ask(system, user):
        return "adds two numbers and returns the sum"

    _run(proj.analyze_summaries(summ_ask))
    assert proj.targets[0].summary == "adds two numbers and returns the sum"

    planner_prompts = []
    good = '''```ruby
require "calculator"
RSpec.describe Calculator do
  it "adds" do
    expect(Calculator.new.add(2, 3)).to eq(5)
  end
end
```'''

    async def gen_ask(system, user):
        if "Test Plan" in system:
            planner_prompts.append(user)
            return '[{"name":"adds","desc":"x","setup":"None"}]'
        return good

    _run(proj.generate_all(ask=gen_ask))
    # The summary computed earlier is fed into the Planner's context block.
    assert any("adds two numbers and returns the sum" in p for p in planner_prompts)

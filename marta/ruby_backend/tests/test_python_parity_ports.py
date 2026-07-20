"""Tests for the changes ported from the Python MARTA (commit 04ab6743):
anti-mock prompts, focused expectations, and the resume-safe round skip."""
import asyncio

import pytest

from marta.ruby_backend import project, prompts, runner
from marta.ruby_backend.ruby_ast import RubyParseError


# --- prompt content (no toolchain) ----------------------------------------- #
def test_planner_prompt_prefers_real_objects():
    p = prompts.plan_user("ctx")
    assert "SETUP GUIDANCE" in p
    assert "REAL objects" in p
    assert "Mock class" not in p  # the old mock-suggesting example is gone


def test_dev_prompt_has_anti_mock_and_focused_expectations():
    p = prompts.dev_user("instr", "src", "calc", "Calc")
    assert "AVOID MOCKS" in p
    assert "NEVER mock the class under test" in p
    assert "1 to 2 `expect` calls" in p
    assert "several small `it` blocks" in p


# --- resume-safe round skip ------------------------------------------------ #
def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_resumed_run_skips_existing_round_specs(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text("class Calc\n  def add(a, b) = a + b\nend\n")
    good = '''```ruby
require "calc"
RSpec.describe Calc do
  it "adds" do
    expect(Calc.new.add(2, 3)).to eq(5)
  end
end
```'''
    dev_calls = {"n": 0}

    async def ask(system, user):
        if "Test Plan" in system:
            return '[{"name":"a","desc":"x","setup":"None"}]'
        dev_calls["n"] += 1
        return good

    # Run 1: fresh source -> code_changed=True -> generates round 0 spec.
    p1 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    assert p1.code_changed is True
    asyncio.run(p1.generate_rounds(rounds=1, ask=ask, max_attempts=1))
    calls_run1 = dev_calls["n"]
    assert calls_run1 == 1
    assert (tmp_path / "marta_specs" / "calc__Calc__add_r0_spec.rb").exists()

    # Run 2 (resume): cg_cache hit -> code_changed=False -> round 0 skipped.
    p2 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    assert p2.code_changed is False
    asyncio.run(p2.generate_rounds(rounds=1, ask=ask, max_attempts=1))
    assert dev_calls["n"] == calls_run1  # no new Dev calls — spec reused from disk


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_changed_source_disables_skip(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    calc = tmp_path / "src" / "calc.rb"
    calc.write_text("class Calc\n  def add(a, b) = a + b\nend\n")
    good = '''```ruby
require "calc"
RSpec.describe Calc do
  it "adds" do
    expect(Calc.new.add(2, 3)).to eq(5)
  end
end
```'''
    dev_calls = {"n": 0}

    async def ask(system, user):
        if "Test Plan" in system:
            return '[{"name":"a","desc":"x","setup":"None"}]'
        dev_calls["n"] += 1
        return good

    p1 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    asyncio.run(p1.generate_rounds(rounds=1, ask=ask, max_attempts=1))
    first = dev_calls["n"]

    # Change the source: cg_cache miss -> code_changed=True -> regenerates.
    calc.write_text("class Calc\n  def add(a, b) = a + b + 0\nend\n")
    p2 = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    assert p2.code_changed is True
    asyncio.run(p2.generate_rounds(rounds=1, ask=ask, max_attempts=1))
    assert dev_calls["n"] > first

"""Tests for the Ruby project orchestrator (discovery + generation driving).

Stubbed LLM keeps it deterministic. Requires the Ruby/RSpec toolchain.
"""
import asyncio

import pytest

from marta.ruby_backend import project, runner
from marta.ruby_backend.ruby_ast import RubyParseError


def _toolchain_ok() -> bool:
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


def _make_project(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calculator.rb").write_text(
        "class Calculator\n"
        "  def initialize(base = 0)\n    @base = base\n  end\n"
        "  def add(a, b) = a + b + @base\n"
        "end\n"
    )
    return tmp_path


def test_discover_builds_targets(tmp_path):
    p = _make_project(tmp_path)
    proj = project.RubyProject(root_dir=str(p), source_dir="src").discover()
    assert len(proj.files) == 1
    # initialize is skipped; add remains
    names = [t.method.name for t in proj.targets]
    assert names == ["add"]
    t = proj.targets[0]
    assert t.require_target == "calculator"
    assert t.describe_subject == "Calculator"
    assert "class Calculator" in t.context_source  # whole class as context
    assert t.spec_path == "spec/calculator__Calculator__add_spec.rb"


def test_generate_all_with_stub(tmp_path):
    p = _make_project(tmp_path)
    proj = project.RubyProject(root_dir=str(p), source_dir="src").discover()

    good = '''```ruby
require "calculator"
RSpec.describe Calculator do
  it "adds" do
    expect(Calculator.new(0).add(2, 3)).to eq(5)
  end
end
```'''
    responses = ['[{"name":"adds","desc":"happy","setup":"None"}]', good]
    calls = {"n": 0}

    async def ask(system, user):
        i = calls["n"]; calls["n"] += 1
        return responses[min(i, len(responses) - 1)]

    outcomes = asyncio.run(proj.generate_all(ask=ask))
    assert len(outcomes) == 1
    assert outcomes[0].success
    assert (p / "spec" / "calculator__Calculator__add_spec.rb").exists()

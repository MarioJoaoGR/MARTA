"""Tests for Option D salvage (removing failing `it` blocks by line range).

The pure line-surgery logic is toolchain-free; the end-to-end salvage-through-
generation test needs the Ruby/RSpec toolchain and skips without it.
"""
import asyncio

import pytest

from marta.ruby_backend import generate, runner, salvage
from marta.ruby_backend.ruby_ast import ExampleBlock, RubyParseError, parse_source


# --- pure logic (no Ruby needed) ------------------------------------------ #
SPEC = """require "calculator"
RSpec.describe Calculator do
  it "passes" do
    expect(1).to eq(1)
  end
  it "fails" do
    expect(1).to eq(2)
  end
end
"""


def test_salvage_removes_failing_block():
    # `it "fails"` spans lines 6-8; the failing example's line_number is 6.
    examples = [
        ExampleBlock("it", "passes", 3, 5),
        ExampleBlock("it", "fails", 6, 8),
    ]
    result = salvage.salvage_spec(SPEC, examples, failed_lines=[6])
    assert result is not None
    trimmed, removed = result
    assert removed == 1
    assert '"passes"' in trimmed
    assert '"fails"' not in trimmed
    assert 'expect(1).to eq(2)' not in trimmed


def test_salvage_none_when_all_fail():
    examples = [ExampleBlock("it", "a", 3, 5), ExampleBlock("it", "b", 6, 8)]
    assert salvage.salvage_spec(SPEC, examples, failed_lines=[3, 6]) is None


def test_salvage_none_without_failures():
    examples = [ExampleBlock("it", "a", 3, 5)]
    assert salvage.salvage_spec(SPEC, examples, failed_lines=[]) is None


# --- integration through the toolchain ------------------------------------ #
def _toolchain_ok() -> bool:
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


needs_ruby = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


@needs_ruby
def test_parser_extracts_examples():
    fp = parse_source(SPEC, "calc_spec.rb")
    descs = [(e.name, e.description) for e in fp.examples]
    assert descs == [("it", "passes"), ("it", "fails")]
    fails = next(e for e in fp.examples if e.description == "fails")
    assert fails.start_line == 6


@needs_ruby
def test_generate_salvages_partial_spec(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calculator.rb").write_text(
        "class Calculator\n  def add(a, b) = a + b\nend\n"
    )
    mixed = '''```ruby
require "calculator"
RSpec.describe Calculator do
  it "adds correctly" do
    expect(Calculator.new.add(2, 3)).to eq(5)
  end
  it "is wrong on purpose" do
    expect(Calculator.new.add(2, 3)).to eq(999)
  end
end
```'''
    plan = '[{"name":"adds","desc":"x","setup":"None"}]'
    # LLM never fixes the failing example -> self-heal exhausts -> salvage kicks in.
    responses = [plan, mixed, mixed, mixed]
    calls = {"n": 0}

    async def ask(system, user):
        i = calls["n"]; calls["n"] += 1
        return responses[min(i, len(responses) - 1)]

    out = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calculator#add",
        describe_subject="Calculator",
        method_source="def add(a, b) = a + b",
        require_target="calculator",
        load_paths=["src"],
        spec_path="spec/add_spec.rb",
        cwd=str(tmp_path),
        ask=ask,
        max_attempts=2,
    ))
    assert out.success
    assert out.salvaged
    assert out.removed_examples == 1
    kept = (tmp_path / "spec" / "add_spec.rb").read_text()
    assert "adds correctly" in kept
    assert "is wrong on purpose" not in kept

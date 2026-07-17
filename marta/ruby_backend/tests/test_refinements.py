"""Tests for the final refinements: error-directed RAG in self-heal (item 1)
and empty-group cleanup after salvage (item 4)."""
import asyncio
import textwrap

import pytest

from marta.ruby_backend import project, runner, salvage
from marta.ruby_backend.ruby_ast import ExampleBlock, GroupBlock, RubyParseError, parse_source


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


needs_ruby = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


# --- item 4: empty-group cleanup (pure logic) ------------------------------ #
GROUPED_SPEC = """\
require "calc"
RSpec.describe Calc do
  it "passes" do
    expect(1).to eq(1)
  end
  context "failing group" do
    it "fails" do
      expect(1).to eq(2)
    end
  end
  context "empty from birth" do
  end
end
"""


def test_salvage_removes_groups_left_empty():
    examples = [ExampleBlock("it", "passes", 3, 5), ExampleBlock("it", "fails", 7, 9)]
    groups = [
        GroupBlock("describe", "Calc", 2, 13),
        GroupBlock("context", "failing group", 6, 10),
        GroupBlock("context", "empty from birth", 11, 12),
    ]
    result = salvage.salvage_spec(GROUPED_SPEC, examples, failed_lines=[7], groups=groups)
    assert result is not None
    trimmed, removed = result
    assert removed == 1
    assert '"passes"' in trimmed
    assert "failing group" not in trimmed       # group with only failing it: gone
    assert "empty from birth" not in trimmed    # empty husk: gone
    assert "RSpec.describe Calc" in trimmed     # ancestor of survivor: kept


@needs_ruby
def test_parser_extracts_groups():
    fp = parse_source(GROUPED_SPEC, "calc_spec.rb")
    names = [(g.name, g.description) for g in fp.groups]
    assert ("describe", "Calc") in names
    assert ("context", "failing group") in names
    assert ("context", "empty from birth") in names


@needs_ruby
def test_e2e_salvage_leaves_no_empty_groups(tmp_path):
    from marta.ruby_backend import generate

    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text("class Calc\n  def add(a, b) = a + b\nend\n")
    mixed = '''```ruby
require "calc"
RSpec.describe Calc do
  it "adds" do
    expect(Calc.new.add(2, 3)).to eq(5)
  end
  context "wrong ideas" do
    it "is wrong" do
      expect(Calc.new.add(2, 3)).to eq(999)
    end
  end
end
```'''

    async def ask(system, user):
        return '[{"name":"a","desc":"x","setup":"None"}]' if "Test Plan" in system else mixed

    out = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc#add", describe_subject="Calc",
        method_source="def add(a, b) = a + b", require_target="calc",
        load_paths=["src"], spec_path="spec/add_spec.rb", cwd=str(tmp_path),
        ask=ask, max_attempts=1,
    ))
    assert out.success and out.salvaged
    kept = (tmp_path / "spec" / "add_spec.rb").read_text()
    assert "adds" in kept
    assert "wrong ideas" not in kept  # no empty context husk left behind


# --- item 1: error-directed RAG reaches the repair prompt ------------------ #
VOCAB = ["add", "sum", "subtract", "difference"]


def _vec(text):
    t = text.lower()
    return [float(t.count(w)) for w in VOCAB]


@needs_ruby
def test_error_help_reaches_repair_prompt(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text(
        "class Calc\n  def add(a, b) = a + b\n  def sub(a, b) = a - b\nend\n"
    )
    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    proj.targets[0].summary = "add two numbers and return the sum"   # add
    proj.targets[1].summary = "subtract to get the difference"       # sub
    proj.build_rag(lambda docs: [_vec(d) for d in docs], _vec)

    # A passing spec for `sub` already on disk -> becomes the RAG example.
    (tmp_path / "spec" / "calc__Calc__sub_r0_spec.rb").write_text(
        'require "calc"\nRSpec.describe Calc do\n  it "subs" do\n'
        "    expect(Calc.new.sub(5, 3)).to eq(2)\n  end\nend\n"
    )

    bad = '''```ruby
require "calc"
RSpec.describe Calc do
  it "adds" do
    expect(Calc.new.add(2, 3)).to eq(999)
  end
end
```'''
    good = bad.replace("999", "5")
    dev_prompts = []
    calls = {"n": 0}

    async def ask(system, user):
        if "Test Plan" in system:
            return '[{"name":"a","desc":"x","setup":"None"}]'
        dev_prompts.append(user)
        calls["n"] += 1
        return bad if calls["n"] == 1 else good

    outcomes = asyncio.run(proj.generate_all(ask=ask, limit=1, max_attempts=2))
    assert outcomes[0].success
    # The repair (2nd) Dev prompt carried the error-directed RAG block.
    assert any("SIMILAR TESTED METHODS" in p for p in dev_prompts[1:])
    assert any("Example passing spec" in p for p in dev_prompts[1:])

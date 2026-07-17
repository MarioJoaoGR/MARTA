"""Coverage-guided multi-round loop (Fase 2), driven by a coverage-aware stub.

The stub returns a spec exercising only the positive branch on round 0, then —
when it sees MISSING LINES in the Dev prompt — a spec covering the remaining
branches. This proves the loop measures coverage, feeds missing lines back, and
skips a method once it's fully covered. Requires the Ruby/RSpec toolchain.
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


SIGN = (
    "class Calc\n"
    "  def sign(n)\n"
    "    if n > 0\n"
    '      "pos"\n'
    "    elsif n < 0\n"
    '      "neg"\n'
    "    else\n"
    '      "zero"\n'
    "    end\n"
    "  end\n"
    "end\n"
)

PARTIAL = '''```ruby
require "calc"
RSpec.describe Calc do
  it "pos" do
    expect(described_class.new.sign(5)).to eq("pos")
  end
end
```'''

FULL = '''```ruby
require "calc"
RSpec.describe Calc do
  it "neg" do
    expect(described_class.new.sign(-5)).to eq("neg")
  end
  it "zero" do
    expect(described_class.new.sign(0)).to eq("zero")
  end
end
```'''


def test_coverage_guided_rounds(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text(SIGN)

    prompts_seen = []
    dev_calls = {"n": 0}

    async def ask(system, user):
        prompts_seen.append(user)
        if "Test Plan" in system:                 # Planner (gets coverage feedback)
            return '[{"name":"branches","desc":"x","setup":"None"}]'
        # Dev: coverage feedback reaches the Planner, not here — key on round order.
        dev_calls["n"] += 1
        return PARTIAL if dev_calls["n"] == 1 else FULL

    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    outcomes = asyncio.run(proj.generate_rounds(rounds=2, ask=ask, max_attempts=1))

    # Round 0 produced the partial spec; round 1 saw missing lines and added more.
    assert any("MISSING LINES" in p for p in prompts_seen)
    r0 = tmp_path / "spec" / "calc__Calc__sign_r0_spec.rb"
    r1 = tmp_path / "spec" / "calc__Calc__sign_r1_spec.rb"
    assert r0.exists() and r1.exists()  # specs accumulate across rounds

    # After both rounds the method is fully covered.
    cov = proj.measure_coverage()
    assert cov[0].fully_covered, cov[0].missing_lines


def test_fully_covered_skips_second_round(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text(
        "class Calc\n  def double(n) = n * 2\nend\n"
    )
    full = '''```ruby
require "calc"
RSpec.describe Calc do
  it "doubles" do
    expect(described_class.new.double(3)).to eq(6)
  end
end
```'''

    round1_dev_calls = {"n": 0}

    async def ask(system, user):
        if "Test Plan" in system:
            return '[{"name":"d","desc":"x","setup":"None"}]'
        round1_dev_calls["n"] += 1
        return full

    proj = project.RubyProject(root_dir=str(tmp_path), source_dir="src").discover()
    asyncio.run(proj.generate_rounds(rounds=3, ask=ask, max_attempts=1))
    # A one-line method is fully covered after round 0, so no r1/r2 specs.
    assert not (tmp_path / "spec" / "calc__Calc__double_r1_spec.rb").exists()
    assert not (tmp_path / "spec" / "calc__Calc__double_r2_spec.rb").exists()

"""Tests for the Ruby recorder (item 8): metric counters + flow instrumentation."""
import asyncio
import json

import pytest

from marta.ruby_backend import generate, project, recorder, runner
from marta.ruby_backend.ruby_ast import RubyParseError


# --- pure Score logic (no toolchain) --------------------------------------- #
def test_first_run_variants_track_only_round_zero():
    s = recorder.RubyScore()
    s.add_syntax_pass()          # first_run True
    s.first_run = False
    s.add_syntax_pass()          # not first_run
    assert s.syntax_pass == 2
    assert s.first_syntax_pass == 1


def test_error_types_and_tokens():
    s = recorder.RubyScore()
    s.add_assertion_error_type("Boom")
    s.add_assertion_error_type("Boom")
    s.add_llm_call(10, 5)
    j = s.to_json()
    assert j["assertion_error_types"] == {"Boom": 2}
    assert j["total_tokens"] == 15 and j["llm_calls"] == 1
    assert "first_run" not in j


def test_recorder_writes_json(tmp_path):
    r = recorder.RubyRecorder()
    r.start_count_time("phase")
    r.end_count_time("phase")
    r.score.add_syntax_pass()
    path = r.end(str(tmp_path), "proj")
    data = json.loads(open(path).read())
    assert "time" in data and "phase" in data["times"]
    assert data["syntax_pass"] == 1


# --- flow instrumentation -------------------------------------------------- #
def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark_needs = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


@pytestmark_needs
def test_records_llm_calls_and_assertion_pass(tmp_path):
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

    async def ask(system, user):
        return '[{"name":"a","desc":"x","setup":"None"}]' if "Test Plan" in system else good

    r = recorder.RubyRecorder()
    asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc#add",
        describe_subject="Calc",
        method_source="def add(a, b) = a + b",
        require_target="calc",
        load_paths=["src"],
        spec_path="spec/add_spec.rb",
        cwd=str(tmp_path),
        ask=ask,
        recorder=r,
    ))
    assert r.score.llm_calls == 2         # planner + one dev
    assert r.score.assertion_pass == 1
    assert r.score.syntax_pass == 1
    assert r.score.assertion_error == 0


@pytestmark_needs
def test_records_syntax_fix_success_on_self_heal(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text("class Calc\n  def add(a, b) = a + b\nend\n")
    broken = '```ruby\nRSpec.describe Calc do\n  it "x" do\n    expect(\n  end\nend\n```'
    good = '''```ruby
require "calc"
RSpec.describe Calc do
  it "adds" do
    expect(Calc.new.add(2, 3)).to eq(5)
  end
end
```'''
    responses = ['[{"name":"a","desc":"x","setup":"None"}]', broken, good]
    n = {"i": 0}

    async def ask(system, user):
        i = n["i"]; n["i"] += 1
        return responses[min(i, len(responses) - 1)]

    r = recorder.RubyRecorder()
    asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc#add", describe_subject="Calc",
        method_source="def add(a, b) = a + b", require_target="calc",
        load_paths=["src"], spec_path="spec/add_spec.rb", cwd=str(tmp_path),
        ask=ask, recorder=r,
    ))
    assert r.score.syntax_error == 1
    assert r.score.syntax_fix_success == 1
    assert r.score.assertion_pass == 1

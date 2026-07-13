"""End-to-end test of the RSpec generation flow with a stubbed LLM.

Drives generate_spec_for_method with canned Planner/Dev responses so the whole
mechanism — plan parsing, code extraction, file write, syntax gate, RSpec run,
self-heal, keep/discard — is exercised deterministically, no live model needed.
Requires the Ruby/RSpec toolchain (skips otherwise).
"""
import asyncio

import pytest

from marta.ruby_backend import generate, runner
from marta.ruby_backend.ruby_ast import RubyParseError


def _toolchain_ok() -> bool:
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


CALCULATOR = "class Calculator\n  def add(a, b) = a + b\nend\n"

PLAN_RESPONSE = """```json
[
  {"name": "adds two numbers", "desc": "happy path", "setup": "None"}
]
```"""

GOOD_SPEC = '''```ruby
require "calculator"
RSpec.describe Calculator do
  it "adds two numbers" do
    expect(described_class.new.add(2, 3)).to eq(5)
  end
end
```'''

BROKEN_SPEC = '''```ruby
require "calculator"
RSpec.describe Calculator do
  it "adds two numbers" do
    expect(described_class.new.add(2, 3)).to eq(   # syntax error: unclosed
  end
end
```'''

FAILING_SPEC = '''```ruby
require "calculator"
RSpec.describe Calculator do
  it "adds two numbers" do
    expect(described_class.new.add(2, 3)).to eq(999)
  end
end
```'''


def _make_project(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calculator.rb").write_text(CALCULATOR)
    return tmp_path


def _scripted_ask(responses):
    """Return an async ask(system, user) that yields `responses` in order.
    The first call is the Planner; subsequent calls are Dev attempts."""
    calls = {"n": 0}

    async def ask(system, user):
        i = calls["n"]
        calls["n"] += 1
        return responses[min(i, len(responses) - 1)]

    return ask, calls


def _run(coro):
    return asyncio.run(coro)


def _gen(tmp_path, ask, **over):
    kwargs = dict(
        method_qualified_name="Calculator#add",
        describe_subject="Calculator",
        method_source="def add(a, b) = a + b",
        require_target="calculator",
        load_paths=["src"],
        spec_path="spec/add_spec.rb",
        cwd=str(tmp_path),
        ask=ask,
    )
    kwargs.update(over)
    return _run(generate.generate_spec_for_method(**kwargs))


def test_happy_path_two_calls(tmp_path):
    p = _make_project(tmp_path)
    ask, calls = _scripted_ask([PLAN_RESPONSE, GOOD_SPEC])
    out = _gen(p, ask)
    assert out.success
    assert out.attempts == 1
    assert calls["n"] == 2  # Planner + one Dev call
    assert (p / "spec" / "add_spec.rb").exists()  # kept on success
    assert list(out.results.values()) == ["passed"]


def test_self_heal_after_syntax_error(tmp_path):
    p = _make_project(tmp_path)
    # Planner, then a broken Dev response, then a good one on retry.
    ask, calls = _scripted_ask([PLAN_RESPONSE, BROKEN_SPEC, GOOD_SPEC])
    out = _gen(p, ask)
    assert out.success
    assert out.attempts == 2  # healed on the second Dev attempt
    assert (p / "spec" / "add_spec.rb").exists()


def test_failing_assertion_discards_and_reports(tmp_path):
    p = _make_project(tmp_path)
    ask, calls = _scripted_ask([PLAN_RESPONSE, FAILING_SPEC])  # always wrong
    out = _gen(p, ask, max_attempts=2)
    assert not out.success
    assert out.attempts == 2
    assert not (p / "spec" / "add_spec.rb").exists()  # discarded on total failure
    assert out.results  # per-example results still captured
    assert "999" in (out.last_error or "")


def test_plan_fallback_on_garbage(tmp_path):
    p = _make_project(tmp_path)
    ask, _ = _scripted_ask(["not json at all", GOOD_SPEC])
    out = _gen(p, ask)
    assert out.success  # fallback single-scenario plan still drives a good spec

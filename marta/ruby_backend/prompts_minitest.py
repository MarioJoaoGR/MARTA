"""Minitest-flavoured prompts.

Same contract as ``prompts`` (RSpec) — the generation flow reads them off the
backend, so swapping frameworks is just swapping this module. Only the Dev side
really differs: Minitest tests are plain ``def test_x`` methods inside a
``Minitest::Test`` subclass, with ``assert_*`` instead of ``expect().to``.
"""
from __future__ import annotations

from typing import List, Optional

# Planner and context are framework-agnostic — reuse them verbatim.
from .prompts import (  # noqa: F401
    PLAN_SYS,
    build_context_block,
    plan_user,
)


def get_ruby_code(response: str) -> str:
    from .prompts import get_ruby_code as _g
    return _g(response)


DEV_SYS = "You are a Minitest Expert. Write valid, runnable Ruby code."


def _class_name(describe_subject: str) -> str:
    """`Money::Bank::Base` -> `MoneyBankBaseTest`; `"foo"` -> `FooTest`."""
    token = describe_subject.strip().strip('"')
    parts = [p for p in token.replace("::", " ").replace("_", " ").split() if p]
    camel = "".join(p[:1].upper() + p[1:] for p in parts) or "Generated"
    return f"{camel}Test"


def dev_user(
    instruction: str,
    method_source: str,
    require_target: str,
    describe_subject: str,
) -> str:
    return f"""
{instruction}

METHOD UNDER TEST:
```ruby
{method_source}
```

RULES:
1. Output ONLY Ruby code in a ```ruby``` block (a complete, self-contained test file).
2. Start the file with:
   require "minitest/autorun"
   require "{require_target}"
3. Define `class {_class_name(describe_subject)} < Minitest::Test` containing one independent `def test_<snake_case_name>` method per scenario.
4. Use Minitest assertions: `assert_equal expected, actual`, `assert_raises(ArgumentError) {{ ... }}`, `assert_nil`, `assert_predicate`. Do NOT use RSpec syntax (`describe`/`it`/`expect`).
5. AVOID MOCKS unless strictly necessary: prefer constructing REAL objects with simple values. Only stub true external I/O (network, filesystem, subprocess, environment). NEVER mock the class under test or anything you can instantiate directly.
6. IF you must isolate a dependency, use a plain stub object or `Minitest::Mock` with `expect`, and always `verify` it. NEVER redefine global constants or monkey-patch classes directly.
7. ASSERTIONS: keep each test method focused — 1 to 2 assertions per method, asserting CONCRETE expected values derived from the source code. Prefer several small test methods over one with many assertions.
"""


def first_dev_instruction(scenarios: List[dict]) -> str:
    block = "\n".join(
        f"          {i + 1}. {s.get('name')}: {s.get('desc')} (setup: {s.get('setup')})"
        for i, s in enumerate(scenarios)
    )
    return (
        f"Write a SINGLE Minitest file containing ONE `def test_...` method for EACH "
        f"of these {len(scenarios)} scenarios:\n{block}"
    )


def repair_dev_instruction(last_error: str, similar_help: str = "") -> str:
    return (
        f"PREVIOUS CODE FAILED.\nERROR MESSAGE:\n{last_error}"
        f"{similar_help}\n"
        f"TASK: Rewrite the ENTIRE test file to fix this error. "
        f"Keep one independent `def test_...` method per scenario."
    )

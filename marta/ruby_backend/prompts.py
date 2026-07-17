"""RSpec-flavoured prompts for the Ruby backend.

The Ruby counterpart to the Planner/Dev prompt strings baked into
``generate_react_flow``. Kept as pure builders so they can be unit-tested and
swapped without touching the flow. The Planner emits a JSON test plan; the Dev
writes one complete spec file with one ``it`` block per scenario.
"""
from __future__ import annotations

from typing import List, Optional


def get_ruby_code(response: str) -> str:
    """Extract a Ruby code block from an LLM response.

    Mirrors ``utils.get_code`` but strips a leading ``ruby`` fence tag. Falls
    back to the raw text when no fenced block is present.
    """
    parts = response.split("```")
    if len(parts) < 3:
        return response.strip()
    body = "```".join(parts[1:-1])
    for tag in ("ruby", "rb"):
        if body[: len(tag)].lower() == tag:
            body = body[len(tag):]
            break
    return body.strip()


PLAN_SYS = "You are a QA Lead. Analyze the Ruby method and output a Test Plan in JSON format."


def plan_user(context_block: str) -> str:
    return f"""
Analyze the following Ruby method and generate a comprehensive test plan.

CONTEXT:
{context_block}

TASK:
Generate 3 distinct test scenarios covering:
CRITICAL: If 'MISSING LINES TO COVER' are provided in the context, you MUST design these scenarios specifically to execute those missing lines.
1. Valid inputs (Happy Path)
2. Edge cases (e.g., nil, empty arrays, boundary values)
3. Invalid inputs / error handling (e.g. raising an error)

SETUP GUIDANCE: prefer REAL objects with simple concrete values in 'setup';
only suggest doubles/stubs for true external I/O (network, filesystem, subprocess).

OUTPUT FORMAT:
Return ONLY a raw JSON list. No Markdown. No Explanations.
Example:
[
    {{"name": "adds two positive numbers", "desc": "Test standard input", "setup": "Real instance with minimal args"}},
    {{"name": "raises on nil argument", "desc": "Test ArgumentError", "setup": "None"}}
]
"""


DEV_SYS = "You are an RSpec Expert. Write valid, runnable Ruby code."


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
1. Output ONLY Ruby code in a ```ruby``` block (a complete, self-contained spec file).
2. Start the file with: require "{require_target}"
3. Use RSpec: `RSpec.describe {describe_subject} do ... end` with one independent `it "..." do ... end` block per scenario.
4. Use `expect(...).to eq(...)` / `raise_error(...)` matchers. Do NOT use any other test framework.
5. AVOID MOCKS unless strictly necessary: prefer constructing REAL objects with simple values. Only stub true external I/O (network, filesystem, subprocess, environment). NEVER mock the class under test, plain value objects, or anything you can instantiate directly. A wrong double fails the test without testing anything.
6. IF you must isolate a dependency, use RSpec doubles (`instance_double`, `double`) with `allow(...).to receive(...)`. NEVER redefine global constants or monkey-patch classes directly. NEVER assert on a double's internals. Strict state isolation is mandatory.
7. EXPECTATIONS: keep each `it` block focused — 1 to 2 `expect` calls per block, asserting CONCRETE expected values you derived from the source code. Prefer several small `it` blocks over one block with many expectations (one wrong expectation kills the whole example).
"""


def build_context_block(
    method_qualified_name: str,
    require_target: str,
    source_code: str,
    summary: Optional[str],
    coverage_info: str,
    related: Optional[List[str]] = None,
) -> str:
    related_block = ""
    if related:
        lines = ["RELATED METHODS IN THIS PROJECT (for inspiration):"]
        lines += [f"        - {r}" for r in related]
        related_block = "\n        " + "\n        ".join(lines)
    return f"""
        Method Name: {method_qualified_name}
        Require target: {require_target}

        SOURCE CODE:
        {source_code}

        SUMMARY:
        {summary if summary else "No summary available."}

        COVERAGE FEEDBACK:
        {coverage_info}
        {related_block}
        """


def first_dev_instruction(scenarios: List[dict]) -> str:
    block = "\n".join(
        f"          {i + 1}. {s.get('name')}: {s.get('desc')} (setup: {s.get('setup')})"
        for i, s in enumerate(scenarios)
    )
    return (
        f"Write a SINGLE RSpec file containing ONE `it` block for EACH of these "
        f"{len(scenarios)} scenarios:\n{block}"
    )


def repair_dev_instruction(last_error: str, similar_help: str = "") -> str:
    return (
        f"PREVIOUS CODE FAILED.\nERROR MESSAGE:\n{last_error}"
        f"{similar_help}\n"
        f"TASK: Rewrite the ENTIRE spec file to fix this error. "
        f"Keep one independent `it` block per scenario."
    )

"""Method-level RSpec generation flow (Ruby MVP, Fase 1).

The Ruby analogue of ``FunctionMessage.generate_react_flow``: Planner proposes a
JSON test plan, Dev writes one spec file covering every scenario, and a
self-healing loop feeds syntax/RSpec errors back until the file is green or the
attempt budget runs out. One round, no coverage loop yet (that is Fase 2).

The LLM is injected as ``ask`` (``async (system, user) -> str``), defaulting to
``gptapi.model.aask``. This keeps the flow runnable and testable without a live
model — pass a stub that returns canned responses.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Awaitable, Callable, Dict, List, Optional

from . import prompts, runner

AskFn = Callable[[str, str], Awaitable[str]]


@dataclass
class GenOutcome:
    method: str
    success: bool
    attempts: int
    spec_path: Optional[str] = None
    spec_code: Optional[str] = None
    last_error: Optional[str] = None
    results: Dict[str, str] = field(default_factory=dict)


def _default_ask() -> AskFn:
    # Imported lazily so the module (and its tests) don't pull in the LLM stack.
    from marta.gptapi import model
    return model.aask


def parse_plan(raw: str, fallback_name: str) -> List[dict]:
    """Robustly pull a JSON scenario list out of an LLM response.

    Mirrors the Planner parser in ``generate_react_flow``: strip markdown, take
    the outermost ``[...]``, and fall back to a single basic scenario.
    """
    try:
        clean = raw.replace("```json", "").replace("```", "").strip()
        start, end = clean.find("["), clean.rfind("]")
        if start != -1 and end != -1 and end > start:
            plan = json.loads(clean[start:end + 1])
            if isinstance(plan, list) and plan:
                return plan
    except (ValueError, TypeError):
        pass
    return [{"name": f"{fallback_name} basic functionality", "desc": "Basic functionality", "setup": "None"}]


async def generate_spec_for_method(
    *,
    method_qualified_name: str,
    describe_subject: str,
    method_source: str,
    require_target: str,
    load_paths: List[str],
    spec_path: str,
    cwd: str,
    ask: Optional[AskFn] = None,
    summary: str = "",
    coverage_info: str = "First pass: Try to achieve maximum coverage.",
    related: Optional[List[str]] = None,
    max_attempts: int = 3,
) -> GenOutcome:
    """Generate, self-heal and validate one spec file for one method.

    On success the spec file is left on disk (green). On total failure the file
    is removed and ``success`` is False; the caller can inspect ``results`` /
    ``last_error``. (Per-``it`` salvage is a later addition.)
    """
    ask = ask or _default_ask()

    # ---- Planner ---------------------------------------------------------- #
    context_block = prompts.build_context_block(
        method_qualified_name, require_target, method_source, summary, coverage_info, related
    )
    raw_plan = await ask(prompts.PLAN_SYS, prompts.plan_user(context_block))
    scenarios = parse_plan(raw_plan, describe_subject)

    # ---- Dev + self-healing ---------------------------------------------- #
    last_error: Optional[str] = None
    results: Dict[str, str] = {}
    spec_code: Optional[str] = None
    success = False
    attempt = 0

    for attempt in range(1, max_attempts + 1):
        if attempt == 1:
            instruction = prompts.first_dev_instruction(scenarios)
        else:
            instruction = prompts.repair_dev_instruction(last_error or "")

        raw_dev = await ask(
            prompts.DEV_SYS,
            prompts.dev_user(instruction, method_source, require_target, describe_subject),
        )
        spec_code = prompts.get_ruby_code(raw_dev)

        os.makedirs(os.path.dirname(os.path.join(cwd, spec_path)) or cwd, exist_ok=True)
        abs_spec = os.path.join(cwd, spec_path)
        with open(abs_spec, "w", encoding="utf-8") as f:
            f.write(spec_code + "\n")

        # Cheap gate first: ruby -c. Only run RSpec if it parses.
        syntax_err = runner.syntax_check(spec_code)
        if syntax_err is not None:
            last_error = syntax_err
            continue

        res = runner.run_rspec(spec_path, load_paths=load_paths, cwd=cwd)
        results = res.results
        if res.all_passed:
            success = True
            break
        last_error = res.output

    outcome = GenOutcome(
        method=method_qualified_name,
        success=success,
        attempts=attempt,
        spec_path=spec_path if success else None,
        spec_code=spec_code if success else None,
        last_error=None if success else last_error,
        results=results,
    )
    if not success:
        try:
            os.remove(os.path.join(cwd, spec_path))
        except OSError:
            pass
    return outcome

"""Method-level RSpec generation flow (Ruby MVP, Fase 1).

The Ruby analogue of ``FunctionMessage.generate_react_flow``: Planner proposes a
JSON test plan, Dev writes one spec file covering every scenario, and a
self-healing loop feeds syntax/RSpec errors back until the file is green or the
attempt budget runs out. One round, no coverage loop yet (that is Fase 2).

The LLM is injected as ``ask`` (``async (system, user) -> str``), defaulting to
``gptapi.model.aask``. Language-specific operations (syntax check, test runner,
salvage, prompts, parsing) go through an injected ``LanguageBackend`` (default
``RubyBackend``), so this ReAct loop is itself language-agnostic.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Awaitable, Callable, Dict, List, Optional

from .backend import LanguageBackend, RubyBackend
from .runner import RSpecResult

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
    salvaged: bool = False           # kept via Option D (some examples removed)
    removed_examples: int = 0


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
    recorder=None,
    backend: Optional[LanguageBackend] = None,
    error_help_fn: Optional[Callable[[str], str]] = None,
) -> GenOutcome:
    """Generate, self-heal and validate one spec file for one method.

    On success the spec file is left on disk (green). On total failure the file
    is removed and ``success`` is False; the caller can inspect ``results`` /
    ``last_error``. An optional ``RubyRecorder`` collects syntax/assertion/LLM
    metrics.
    """
    ask = ask or _default_ask()
    backend = backend or RubyBackend()
    prompts = backend.prompts
    score = recorder.score if recorder is not None else None
    if score is not None:
        # Credita llm_calls + tokens (delta do singleton gptapi) por chamada.
        from .recorder import token_tracking_ask
        ask = token_tracking_ask(ask, score)

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
    last_res: Optional[RSpecResult] = None
    success = False
    attempt = 0
    abs_spec = os.path.join(cwd, spec_path)

    def _write(code: str) -> None:
        os.makedirs(os.path.dirname(abs_spec) or cwd, exist_ok=True)
        with open(abs_spec, "w", encoding="utf-8") as f:
            f.write(code + "\n")

    for attempt in range(1, max_attempts + 1):
        if attempt == 1:
            instruction = prompts.first_dev_instruction(scenarios)
        else:
            # RAG dirigido ao erro (porta do generate_react_flow): métodos
            # semanticamente próximos do erro + um spec exemplo que já passa.
            similar_help = error_help_fn(last_error or "") if error_help_fn else ""
            instruction = prompts.repair_dev_instruction(last_error or "", similar_help)

        raw_dev = await ask(
            prompts.DEV_SYS,
            prompts.dev_user(instruction, method_source, require_target, describe_subject),
        )
        spec_code = prompts.get_ruby_code(raw_dev)
        _write(spec_code)

        # Cheap gate first: ruby -c. Only run RSpec if it parses.
        syntax_err = backend.syntax_check(spec_code)
        if score is not None:
            (score.add_syntax_error if syntax_err else score.add_syntax_pass)()
            if syntax_err is None and attempt > 1:
                score.add_syntax_fix_success()
        if syntax_err is not None:
            last_error = syntax_err
            last_res = None
            continue

        res = backend.run_tests(spec_path, load_paths, cwd)
        results = res.results
        last_res = res
        if res.all_passed:
            success = True
            if score is not None:
                score.add_assertion_pass()
                if attempt > 1:
                    score.add_assertion_fix_success()
            break
        last_error = res.output
        if score is not None:
            score.add_assertion_error()
            for e in res.failed:
                score.add_assertion_error_type((e.message or "Unknown").splitlines()[0][:80])

    # ---- Option D: salvage passing examples before discarding ------------ #
    salvaged = False
    removed = 0
    if not success and spec_code and last_res is not None and not last_res.load_error:
        failed_lines = [e.line_number for e in last_res.failed if e.line_number]
        fp = backend.parse_source(spec_code, spec_path)
        trimmed = backend.salvage(spec_code, fp.examples, failed_lines, fp.groups)
        if trimmed is not None:
            new_code, removed = trimmed
            if backend.syntax_check(new_code) is None:
                _write(new_code)
                recheck = backend.run_tests(spec_path, load_paths, cwd)
                if recheck.all_passed and recheck.examples:
                    success = True
                    salvaged = True
                    spec_code = new_code
                    results = recheck.results
                    if score is not None:
                        score.add_salvaged()
                        score.add_assertion_fix_success()

    outcome = GenOutcome(
        method=method_qualified_name,
        success=success,
        attempts=attempt,
        spec_path=spec_path if success else None,
        spec_code=spec_code if success else None,
        last_error=None if success else last_error,
        results=results,
        salvaged=salvaged,
        removed_examples=removed if salvaged else 0,
    )
    if not success:
        try:
            os.remove(abs_spec)
        except OSError:
            pass
    return outcome

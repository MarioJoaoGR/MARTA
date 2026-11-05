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

import os
from dataclasses import dataclass, field, replace
from typing import Awaitable, Callable, Dict, List, Optional

from .backend import LanguageBackend, RubyBackend
from .checkpoints import atomic_write
from .runner import RSpecResult
from .repair import FailureDiagnostic, RepairContext, diagnose_result
from .planning import parse_plan, validate_plan
from .prompt_budget import OptionalPart, PromptBudget

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
    plan_fallback: bool = False
    plan_validation_error: Optional[str] = None


def _default_ask() -> AskFn:
    # Imported lazily so the module (and its tests) don't pull in the LLM stack.
    from marta.gptapi import model
    from .requests import RubyAsk
    return RubyAsk(model) if getattr(model, "response_api", False) is True else model.aask


async def generate_spec_for_method(
    *,
    method_qualified_name: str,
    describe_subject: str,
    method_source: str,
    focal_source: Optional[str] = None,
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
    extra_requires: Optional[List[str]] = None,
    loading_context: str = "",
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
    budget = PromptBudget.from_ask(ask, recorder)
    source_part = OptionalPart("source_context", method_source, focal_source or method_source, compact=False)
    score = recorder.score if recorder is not None else None
    if score is not None:
        # Credita chamadas e usage da resposta deste pedido, e
        # etiqueta cada uma com a fase e o método (ver recorder.py).
        from .recorder import token_tracking_ask
        ask = token_tracking_ask(ask, score, recorder)

    # ---- Planner ---------------------------------------------------------- #
    def planner_user(values):
        context_block = prompts.build_context_block(
            method_qualified_name, require_target, values["source_context"], values["summary"],
            coverage_info, values["related"] or None)
        if loading_context:
            context_block += "\n\n" + loading_context
        return prompts.plan_user(context_block)
    planner_parts = [OptionalPart("related", related or [], []),
                     OptionalPart("summary", summary), source_part]
    if recorder is not None:
        with recorder.contexto(metodo=method_qualified_name):
            with recorder.fase("plano"):
                raw_plan = await ask(prompts.PLAN_SYS, budget.render(prompts.PLAN_SYS, planner_user, planner_parts))
    else:
        raw_plan = await ask(prompts.PLAN_SYS, budget.render(prompts.PLAN_SYS, planner_user, planner_parts))
    plan = validate_plan(raw_plan, describe_subject)
    scenarios = plan.scenarios
    if recorder is not None:
        recorder.evento(tipo="plan_validation", fase="plano", metodo=method_qualified_name,
                        valid=not plan.fallback_used, fallback_used=plan.fallback_used,
                        reason=plan.error, raw_plan=raw_plan if isinstance(raw_plan, str) else None,
                        raw_plan_type=type(raw_plan).__name__, effective_plan=scenarios)

    # ---- Dev + self-healing ---------------------------------------------- #
    last_error: Optional[str] = None
    results: Dict[str, str] = {}
    spec_code: Optional[str] = None
    last_res: Optional[RSpecResult] = None
    success = False
    attempt = 0
    previous_code: Optional[str] = None
    source_attempt: Optional[int] = None
    previous_validation: Optional[FailureDiagnostic] = None
    last_failure: Optional[FailureDiagnostic] = None
    abs_spec = os.path.join(cwd, spec_path)

    def _write(code: str) -> None:
        atomic_write(abs_spec, code + "\n")

    # Telemetria opcional: sem recorder, nullcontext e nada muda (ver recorder.py).
    from contextlib import nullcontext

    def _tel(fn, *a, **kw):
        return fn(*a, **kw) if recorder is not None else nullcontext()

    # Só se passa o kwarg quando há alguma coisa: backends que sobrepõem
    # run_tests(test_path, load_paths, cwd) sem ele continuam a funcionar.
    _extra = {"requires_extra": extra_requires} if extra_requires else {}

    for attempt in range(1, max_attempts + 1):
        if attempt == 1:
            instruction = prompts.first_dev_instruction(scenarios)
        else:
            # RAG dirigido ao erro (porta do generate_react_flow): métodos
            # semanticamente próximos do erro + um spec exemplo que já passa.
            similar_help = error_help_fn(last_error or "") if error_help_fn else ""
            context = RepairContext(plan=scenarios, failure=last_failure,
                                    previous_code=previous_code, source_attempt=source_attempt,
                                    previous_validation=previous_validation)
            if recorder is not None:
                recorder.evento(tipo="repair_context", fase="dev_reparacao", metodo=method_qualified_name,
                                tentativa=attempt, plan_id=context.plan_id,
                                source_attempt=source_attempt, previous_code_sha256=context.code_id,
                                last_failure_attempt=last_failure.attempt,
                                failure_stage=last_failure.stage, failure_category=last_failure.category)

        # A primeira escrita e as reparações são fases separadas: o que interessa
        # saber é quanto do custo total é o ciclo de auto-correção.
        fase = "dev_primeira" if attempt == 1 else "dev_reparacao"
        with _tel(recorder.contexto if recorder else None,
                  metodo=method_qualified_name, tentativa=attempt), \
                _tel(recorder.fase if recorder else None, fase):
            def developer_user(values):
                if attempt == 1:
                    dev_instruction = instruction
                else:
                    failure = replace(context.failure, examples=values["failure_examples"])
                    previous = context.previous_validation
                    if previous == context.failure:
                        previous = failure
                    elif previous is not None:
                        previous = replace(previous, examples=values["previous_examples"])
                    reduced_context = replace(context, failure=failure, previous_validation=previous)
                    dev_instruction = prompts.repair_dev_instruction(
                        values["error"], values["similar_help"], context=reduced_context)
                return prompts.dev_user(dev_instruction, values["source_context"], require_target,
                    describe_subject, **({"loading_context": loading_context} if loading_context else {}))
            parts = [source_part]
            if attempt > 1:
                # Keep full previous code/plan and typed failure status. Optional
                # example lists, retrieval and long traceback detail can shrink.
                error = last_error or ""
                excerpt = error if len(error) <= 768 else (
                    error[:512] + "\n[... diagnostic excerpt ...]\n" + error[-256:])
                parts = [OptionalPart("similar_help", similar_help, "", compact=False),
                         OptionalPart("previous_examples", context.previous_validation.examples
                                      if context.previous_validation else [], []),
                         OptionalPart("failure_examples", context.failure.examples, []),
                         OptionalPart("error", error, excerpt, compact=False), source_part]
            raw_dev = await ask(prompts.DEV_SYS, budget.render(prompts.DEV_SYS, developer_user, parts))
            spec_code = prompts.get_ruby_code(raw_dev)
            if not spec_code.strip():
                # An empty model response consumes this existing Dev attempt.
                # Never let an empty Ruby file become a successful test suite.
                last_error = "No test code was returned. Return a complete RSpec test file."
                last_res = None
                last_failure = FailureDiagnostic("empty_response", "model_output", attempt)
                if recorder is not None:
                    recorder.evento(tipo="generation_validation", fase=fase, etapa="empty",
                                    code=spec_code, output=last_error, valid=False)
                continue
            previous_code = spec_code
            source_attempt = attempt
            _write(spec_code)

            # Cheap gate first: ruby -c. Only run RSpec if it parses.
            with _tel(recorder.medir if recorder else None, "ruby -c"):
                syntax_err = backend.syntax_check(spec_code)
            if recorder is not None and syntax_err is not None:
                recorder.evento(tipo="generation_validation", fase=fase, etapa="syntax",
                                code=spec_code, output=syntax_err, valid=False)
        if score is not None:
            (score.add_syntax_error if syntax_err else score.add_syntax_pass)()
            if syntax_err is None and attempt > 1:
                score.add_syntax_fix_success()
        if syntax_err is not None:
            last_error = syntax_err
            last_res = None
            last_failure = FailureDiagnostic("syntax", "syntax", attempt)
            previous_validation = last_failure
            continue

        with _tel(recorder.medir if recorder else None, "rspec"):
            res = backend.run_tests(spec_path, load_paths, cwd, **_extra)
        results = res.results
        if recorder is not None:
            recorder.evento(tipo="generation_validation", fase=fase, etapa="rspec",
                            tentativa=attempt, metodo=method_qualified_name,
                            code=spec_code, output=res.output, valid=res.all_passed,
                            load_error=res.load_error)
        last_res = res
        if res.all_passed:
            success = True
            if score is not None:
                score.add_assertion_pass()
                if attempt > 1:
                    score.add_assertion_fix_success()
            break
        last_error = res.output
        last_failure = diagnose_result(res, attempt)
        previous_validation = last_failure
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
                with _tel(recorder.medir if recorder else None, "rspec"):
                    recheck = backend.run_tests(spec_path, load_paths, cwd, **_extra)
                if recorder is not None:
                    recorder.evento(tipo="generation_validation", fase="salvage", etapa="rspec",
                                    tentativa=attempt, metodo=method_qualified_name,
                                    code=new_code, output=recheck.output, valid=recheck.all_passed,
                                    load_error=recheck.load_error)
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
        plan_fallback=plan.fallback_used,
        plan_validation_error=plan.error,
    )
    if not success:
        try:
            os.remove(abs_spec)
        except OSError:
            pass
    return outcome

"""Observed repair state; no model calls or benchmark-specific repair recipes."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
import hashlib
import json
from typing import List, Optional

from .runner import RSpecResult


@dataclass(frozen=True)
class FailureDiagnostic:
    stage: str
    category: str
    attempt: int
    report_valid: Optional[bool] = None
    exit_code: Optional[int] = None
    validation_error: Optional[str] = None
    counts: Optional[dict] = None
    examples: List[dict] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


_EXCEPTION_CATEGORIES = {
    "LoadError": "loading",
    "NameError": "missing_constant",
    "NoMethodError": "missing_method",
    "ArgumentError": "arguments",
    "TypeError": "type_error",
    "RSpec::Expectations::ExpectationNotMetError": "assertion",
}


def diagnose_result(result: RSpecResult, attempt: int) -> FailureDiagnostic:
    """Use typed runner evidence, never guesses from arbitrary error substrings."""
    examples = []
    counts = None
    if result.report_valid:
        examples = [{"id": e.id, "name": e.full_description, "status": e.status,
                     "line": e.line_number, "exception_class": e.exception_class}
                    for e in result.examples]
        counts = {status: sum(e.status == status for e in result.examples)
                  for status in ("passed", "failed", "pending")}
    if result.timed_out:
        category = "timeout"
    elif not result.report_valid:
        category = "invalid_report"
    elif result.load_error:
        category = "outside_examples"
    elif result.failed:
        categories = {_EXCEPTION_CATEGORIES.get(e.exception_class, "execution") for e in result.failed}
        category = next(iter(categories)) if len(categories) == 1 else "mixed"
    elif not any(e.status == "passed" for e in result.examples):
        category = "no_passing_examples"
    else:
        category = "process_exit"
    return FailureDiagnostic(stage="rspec", category=category, attempt=attempt,
                             report_valid=result.report_valid, exit_code=result.exit_code,
                             validation_error=result.validation_error, counts=counts, examples=examples)


@dataclass(frozen=True)
class RepairContext:
    plan: List[dict]
    failure: FailureDiagnostic
    previous_code: Optional[str] = None
    source_attempt: Optional[int] = None
    previous_validation: Optional[FailureDiagnostic] = None

    @property
    def plan_id(self) -> str:
        encoded = json.dumps(self.plan, sort_keys=True, ensure_ascii=False).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    @property
    def code_id(self) -> Optional[str]:
        if self.previous_code is None:
            return None
        return hashlib.sha256(self.previous_code.encode("utf-8")).hexdigest()

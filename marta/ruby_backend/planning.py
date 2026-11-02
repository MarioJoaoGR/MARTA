"""Validate Planner output with an explicit, auditable fallback contract."""
from __future__ import annotations

from dataclasses import dataclass
import json
from typing import List, Optional

# The template requests three scenarios. This is a resource/format contract,
# not an empirically optimized scenario count or quality threshold.
MAX_PLAN_SCENARIOS = 3
MAX_PLAN_CHARS = 6000
_FIELDS = {"name", "desc", "setup"}


@dataclass(frozen=True)
class PlanValidation:
    scenarios: List[dict]
    fallback_used: bool = False
    error: Optional[str] = None


def _unique_fields(pairs):
    fields = {}
    for name, value in pairs:
        if name in fields:
            raise ValueError("duplicate JSON object field")
        fields[name] = value
    return fields


def validate_plan(raw, fallback_name: str, *, max_scenarios: int = MAX_PLAN_SCENARIOS,
                  max_chars: int = MAX_PLAN_CHARS) -> PlanValidation:
    """Accept a complete list; never silently retain only part of an invalid plan."""
    if (type(max_scenarios) is not int or type(max_chars) is not int
            or max_scenarios < 1 or max_chars < 1):
        raise ValueError("plan limits must be positive")
    try:
        if not isinstance(raw, str):
            raise ValueError("Planner response is not text")
        clean = raw.strip()
        if clean.startswith("```"):
            clean = clean[7:] if clean.lower().startswith("```json") else clean[3:]
            if not clean.rstrip().endswith("```"):
                raise ValueError("incomplete JSON code fence")
            clean = clean.rstrip()[:-3].strip()
        try:
            decoded = json.loads(clean, object_pairs_hook=_unique_fields)
        except json.JSONDecodeError:
            # Preserve support for prose surrounding an array. A JSON object
            # containing a nested array is not the requested top-level list.
            if clean.startswith("{"):
                raise ValueError("Planner response is not a JSON list")
            start, end = clean.find("["), clean.rfind("]")
            if start < 0 or end <= start:
                raise ValueError("Planner response has no complete JSON list")
            if 0 <= clean.find("{") < start:
                raise ValueError("Planner response wraps the list in a JSON object")
            decoded = json.loads(clean[start:end + 1], object_pairs_hook=_unique_fields)
        if not isinstance(decoded, list) or not 1 <= len(decoded) <= max_scenarios:
            raise ValueError(f"plan must contain 1 to {max_scenarios} scenarios")
        scenarios, names = [], set()
        for index, item in enumerate(decoded, 1):
            if not isinstance(item, dict) or set(item) != _FIELDS:
                raise ValueError(f"scenario {index} must contain only name, desc and setup")
            if any(not isinstance(item[key], str) or not item[key].strip() for key in _FIELDS):
                raise ValueError(f"scenario {index} fields must be nonempty text")
            scenario = {key: item[key].strip() for key in ("name", "desc", "setup")}
            if scenario["name"] in names:
                raise ValueError("scenario names must be distinct")
            names.add(scenario["name"])
            scenarios.append(scenario)
        encoded = json.dumps(scenarios, ensure_ascii=False)
        encoded.encode("utf-8")  # Reject escaped, unpaired Unicode surrogates before prompting.
        if len(encoded) > max_chars:
            raise ValueError(f"plan exceeds {max_chars} characters")
        return PlanValidation(scenarios)
    except (ValueError, RecursionError) as exc:
        return PlanValidation([
            {"name": f"{fallback_name} basic functionality", "desc": "Basic functionality", "setup": "None"}
        ], fallback_used=True, error=str(exc))


def parse_plan(raw, fallback_name: str) -> List[dict]:
    """Compatibility entry point; callers needing provenance use validate_plan."""
    return validate_plan(raw, fallback_name).scenarios

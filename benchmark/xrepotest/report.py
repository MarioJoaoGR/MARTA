"""Consumption and completion for a guarded XRepoTest run, including resumes."""
import argparse
from collections import defaultdict
import json
from pathlib import Path


def summarize(root):
    phases = defaultdict(lambda: {"calls": 0, "input_tokens": 0, "output_tokens": 0,
                                  "seconds": 0.0, "truncated": 0, "errors": 0, "cache_hits": 0})
    malformed = 0
    subprocesses = defaultdict(lambda: {"calls": 0, "seconds": 0.0})
    failures = []
    inherited_rounds = {}
    for path in sorted(root.glob("**/events.jsonl")):
        for line in path.read_text().splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                malformed += 1
                continue
            if event.get("tipo") == "generation_round_reused":
                # Interrupted ablation attempts may inherit the same seed again.
                # Charge that common round once; count all new physical calls.
                inherited_rounds[event["reuse_id"]] = {
                    k: event[k] for k in ("source", "task_id", "round", "no_spec", "usage")}
                continue
            row = phases[event.get("fase", "unlabelled")]
            if event.get("tipo") in {"ruby -c", "rspec", "cobertura"}:
                item = subprocesses[event["tipo"]]
                item["calls"] += 1
                item["seconds"] += event.get("segundos", 0)
            if event.get("tipo") in {"llm_infrastructure_failure", "summary_truncated"}:
                failures.append({"file": str(path.relative_to(root)), **event})
                # Before summary retries, an exception bypassed the outer LLM
                # event. Recover the known token usage without rewriting logs.
                if not event.get("llm_event_recorded"):
                    detail = event.get("detail", {})
                    row["calls"] += 1
                    row["input_tokens"] += detail.get("prompt_tokens", 0) or 0
                    row["output_tokens"] += detail.get("completion_tokens", 0) or 0
                    row["truncated"] += detail.get("finish_reason") == "length"
                    row["errors"] += bool(detail.get("erro"))
                    # The legacy event did not contain call duration or phase.
                    row.setdefault("calls_without_timing", 0)
                    row["calls_without_timing"] += 1
            if event.get("tipo") == "llm_cache_hit":
                row["cache_hits"] += 1
            elif event.get("tipo") == "llm":
                row["calls"] += 1
                row["input_tokens"] += event.get("prompt_tokens", 0)
                row["output_tokens"] += event.get("completion_tokens", 0)
                row["seconds"] += event.get("segundos", 0)
                row["truncated"] += bool(event.get("cortada"))
                row["errors"] += bool(event.get("erro"))
    states = defaultdict(int)
    for path in root.glob("tasks/*/state.json"):
        states[json.loads(path.read_text()).get("status", "unknown")] += 1
    audit = root / "generation_empty_upgrade.json"
    historical_note = json.loads(audit.read_text()).get("telemetry_note") if audit.exists() else None
    reuse_path = root / "analysis_reuse.json"
    reused = json.loads(reuse_path.read_text()) if reuse_path.exists() else None
    result = {"tasks": dict(states), "llm_by_phase": dict(phases), "ruby_subprocesses": dict(subprocesses),
            "historical_telemetry_note": historical_note,
            "inherited_analysis": ({"source": reused["source"], "checkpoint_count": reused["checkpoint_count"],
                                    "usage": reused["source_analysis_usage"], "note": reused["note"]} if reused else None),
            "infrastructure_failures": failures, "unreadable_event_lines": malformed,
            "note": "LLM seconds exclude Ruby/embedding/idle time; GPU billing must come from Slurm."}
    if inherited_rounds:
        result["inherited_first_rounds"] = list(inherited_rounds.values())
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("results", type=Path)
    args = p.parse_args()
    if not (args.results / "experiment.json").is_file():
        p.error("Not a guarded XRepoTest experiment")
    print(json.dumps(summarize(args.results), indent=2))


if __name__ == "__main__":
    main()

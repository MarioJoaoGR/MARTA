"""Audit static IR before and after MARTA validation, without Ruby/model execution.

Only the published detector is used. Candidate IR is diagnostic, not an extra
benchmark score or evidence of runtime invocation. Interrupted task archives
are excluded; only the attempt that produced the frozen export is inspected.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

POLICY = "frozen-generation-ir-audit-v1"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def audit_task(task, response, evaluation, events, invoke):
    tid, name = task["task_id"], task["function_name"]
    if len(response) > 1 or evaluation.get("test", []) != response:
        raise ValueError("Export/evaluation suites differ for task " + str(tid))
    checks = evaluation.get("checks", [])
    if len(checks) != bool(response):
        raise ValueError("Expected one check for a suite, none for no_tests")
    final = response[0] if response else ""
    final_ir = bool(invoke(final, name)) if final else False
    check = checks[0] if checks else {}
    if final_ir != bool(check.get("invocation")):
        raise ValueError("Recomputed official IR differs for task " + str(tid))
    validations = []
    for index, e in enumerate(events):
        if e.get("tipo") != "generation_validation":
            continue
        if e.get("task_id", tid) != tid or not isinstance(e.get("code"), str):
            raise ValueError("Invalid validation event in task " + str(tid))
        validations.append({"event_index": index, "round": e.get("ronda"),
                            "phase": e.get("fase"), "stage": e.get("etapa"),
                            "valid": bool(e.get("valid")), "code": e["code"],
                            "ir": bool(invoke(e["code"], name)) if e["code"].strip() else False})
    first = next((e for e in validations if e["round"] == 0 and e["phase"] == "dev_primeira"), None)
    rounds = defaultdict(list)
    for e in validations:
        if e["round"] is not None:
            rounds[e["round"]].append(e)
    losses = []
    for rnd, values in sorted(rounds.items()):
        accepted = [e for e in values if e["stage"] == "rspec" and e["valid"]]
        if not accepted:
            continue
        last = accepted[-1]
        initial = next((e for e in values if e["phase"] == "dev_primeira"), None)
        if last["phase"] == "salvage":
            before = [e for e in values if e["event_index"] < last["event_index"] and e["phase"] != "salvage"]
            prior = before[-1] if before else None
            if prior and prior["ir"] and not last["ir"]:
                losses.append({"round": rnd, "mechanism": "salvage", "before": prior, "after": last})
        elif last["phase"] == "dev_reparacao" and initial and initial["ir"] and not last["ir"]:
            losses.append({"round": rnd, "mechanism": "repair", "before": initial, "after": last})
    any_ir = any(e["ir"] for e in validations)
    if final_ir:
        category = "final_ir_positive"
    else:
        prefix = "nonempty" if final else "no_tests"
        suffix = "earlier_ir_positive" if any_ir else "no_earlier_ir" if validations else "missing_validation_telemetry"
        category = prefix + "_" + suffix
    llm = [e for e in events if e.get("tipo") == "llm"]
    return {"task_id": tid, "project": task["file_path"].split("/", 1)[0],
            "name": name, "file_path": task["file_path"], "category": category,
            "final_has_suite": bool(final), "final_ir": final_ir,
            "compiled": bool(check.get("compilation")), "passed": bool(check.get("tests")),
            "first_round_first_candidate_ir": first["ir"] if first else None,
            "any_candidate_ir": any_ir if validations else None,
            "validation_events": len(validations),
            "empty_candidate_events": sum(not e["code"].strip() for e in validations),
            "truncated_llm_calls": sum(bool(e.get("cortada")) for e in llm),
            "accepted_round_ir_losses": losses,
            "final_suite_sha256": sha(final.encode()),
            "first_candidate": first,
            "earlier_ir_example": next((e for e in validations if e["ir"]), None),
            "final_code": final}


def summarize(cases):
    n = len(cases)
    nonempty = sum(c["final_has_suite"] for c in cases)
    invoked = sum(c["final_ir"] for c in cases)
    first = [c for c in cases if c["first_round_first_candidate_ir"] is not None]
    return {"tasks": n, "nonempty_suites": nonempty, "no_tests": n - nonempty,
            "final_ir_positive": invoked, "final_ir_pct": 100 * invoked / n if n else 0,
            "ir_among_nonempty_pct": 100 * invoked / nonempty if nonempty else 0,
            "nonempty_ir_negative": nonempty - invoked,
            "categories": dict(Counter(c["category"] for c in cases)),
            "final_pass_and_ir": sum(c["passed"] and c["final_ir"] for c in cases),
            "final_pass_without_ir": sum(c["passed"] and not c["final_ir"] for c in cases),
            "first_candidate_available": len(first),
            "first_candidate_ir_positive": sum(c["first_round_first_candidate_ir"] for c in first),
            "first_to_final_transitions": dict(Counter(
                ("positive" if c["first_round_first_candidate_ir"] else "negative") + "_to_" +
                ("positive" if c["final_ir"] else "negative") for c in first)),
            "accepted_round_ir_losses": dict(Counter(
                loss["mechanism"] for c in cases for loss in c["accepted_round_ir_losses"])),
            "final_negative_with_accepted_round_loss": sum(
                not c["final_ir"] and bool(c["accepted_round_ir_losses"]) for c in cases),
            "tasks_with_truncated_llm_calls": sum(c["truncated_llm_calls"] > 0 for c in cases)}


def report(generation, evaluation, dataset):
    from benchmark.xrepotest.protocol import load_tasks
    from benchmark.xrepotest.runtime import validate_evaluator
    import base
    import ruby
    from ruby import test_utils
    hashes = {f"{package.__name__}/{f.name}": sha(f.read_bytes())
              for package in (base, ruby) for f in Path(package.__file__).parent.glob("*.py")}
    validate_evaluator(hashes)
    tasks = load_tasks(dataset)
    processed = generation / "processed.jsonl"
    exported = [json.loads(l) for l in processed.read_text().splitlines() if l.strip()]
    ids = {t["task_id"] for t in tasks}
    if len(exported) != len(ids) or {r["task_id"] for r in exported} != ids:
        raise ValueError("Expected one frozen export for every official task")
    exports = {r["task_id"]: r["response"] for r in exported}
    inputs = {"generation/processed.jsonl": sha(processed.read_bytes())}
    cases = []
    for task in tasks:
        tid = task["task_id"]
        folder = generation / "tasks" / str(tid)
        state = folder / "state.json"
        status = json.loads(state.read_text()).get("status")
        response = exports[tid]
        if status != ("complete" if response else "no_tests"):
            raise ValueError("Task not finished or export/state mismatch")
        final_path = folder / "final_spec.rb"
        if response and final_path.read_text() != response[0]:
            raise ValueError("Final suite differs from export")
        row_path = evaluation / "tasks" / (str(tid) + ".json")
        row = json.loads(row_path.read_text())
        if row["task_id"] != tid or row["function_name"] != task["function_name"] or row["file_path"] != task["file_path"]:
            raise ValueError("Official task/evaluation identity mismatch")
        event_path = folder / "events.jsonl"
        events = [json.loads(l) for l in event_path.read_text().splitlines() if l.strip()] if event_path.exists() else []
        for path, rel in [(row_path, "evaluation/tasks/" + row_path.name),
                          (state, "generation/tasks/" + str(tid) + "/state.json")]:
            inputs[rel] = sha(path.read_bytes())
        if event_path.exists():
            inputs["generation/tasks/" + str(tid) + "/events.jsonl"] = sha(event_path.read_bytes())
        cases.append(audit_task(task, response, row, events, test_utils.is_invoke_in_code))
    grouped = defaultdict(list)
    for case in cases:
        grouped[case["project"]].append(case)
    examples = defaultdict(list)
    detail = []
    for case in cases:
        if not case["final_ir"] and len(examples[case["category"]]) < 5:
            examples[case["category"]].append(case)
        # Keep complete before/after code only for transitions and examples.
        compact = {k: v for k, v in case.items() if k not in {"first_candidate", "earlier_ir_example", "final_code"}}
        detail.append(compact)
    return {"policy": POLICY, "diagnostic_only": True, "source_run": generation.parent.name,
            "detector_sha256": sha(Path(test_utils.__file__).read_bytes()),
            "script_sha256": sha(Path(__file__).read_bytes()), "input_sha256": inputs,
            "notes": ["No generation, test execution, or metric changes. Final IR recomputed and checked against every frozen evaluation result.",
                      "First candidate is the recorded Dev attempt 1 in round 0, including empty/syntax-failing outputs.",
                      "Any-candidate IR uses all recorded attempts/rounds; it is not a comparable one-request benchmark score.",
                      "Positive-to-negative transitions measure loss of recognition by the official static detector, not runtime execution.",
                      "Repair/salvage transitions can overlap; they do not prove every final IR-negative suite is a filtering artifact.",
                      "Interrupted task archives are excluded. Missing validation telemetry is reported separately.",
                      "An IR-negative suite without an earlier positive still needs inspection for indirect calls, detector limitations, or tests that miss the target."],
            "summary": summarize(cases),
            "by_project": {p: summarize(cs) for p, cs in sorted(grouped.items())},
            "task_details": detail, "examples": dict(examples)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generation", type=Path, required=True)
    parser.add_argument("--evaluation", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, default=Path("/app/xrepotest/ruby_functions.jsonl"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Use a new diagnostic output file")
    result = report(args.generation, args.evaluation, args.dataset)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(result["summary"], indent=2), flush=True)
    print("IR audit saved: " + str(args.output), flush=True)


if __name__ == "__main__":
    main()

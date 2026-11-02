"""Read saved evaluation logs only. Host Python 3.6; no Ruby/model execution."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

MODES = ("standard", "lsp_context", "file_context", "rag_bm25", "rag_dense")
ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
ERROR = re.compile(r"^\s*((?:[A-Z]\w*::)*[A-Z]\w*(?:Error|Exception)):\s*(.*)$", re.MULTILINE)


def log_text(row):
    logs = row.get("logs", [])
    if not isinstance(logs, list):
        raise ValueError("Expected the evaluator's list of logs")
    return ANSI.sub("", "\n".join(str(log) for log in logs if log is not None))


def signature(log):
    # These labels describe text in saved logs, not a verified root cause.
    match = ERROR.search(log)
    if match:
        return match.group(1)
    lower = log.lower()
    if "cannot load such file" in lower:
        return "cannot_load_such_file"
    if "test execution timeout" in lower:
        return "test_execution_timeout"
    if "evaluation error:" in lower:
        return "evaluation_error"
    if "syntax error" in lower:
        return "syntax_error"
    if "an error occurred while loading" in lower:
        return "loading_failure_unclassified"
    if "Failure/Error:" in log:
        return "rspec_failure_unclassified"
    return "unclassified_log" if log.strip() else "missing_log"


def summarize(rows):
    counts = Counter()
    patterns = Counter()
    projects = {}
    examples = {}
    for row in rows:
        project = row["file_path"].split("/", 1)[0]
        checks = row.get("checks", [])
        response = row.get("test", [])
        if len(response) > 1 or len(checks) != bool(response):
            raise ValueError("Expected one check for a response, none for an empty response")
        check = checks[0] if checks else {}
        stats = projects.setdefault(project, Counter())
        stats["tasks"] += 1
        counts["tasks"] += 1
        for key in ("compilation", "tests", "invocation"):
            counts[key] += bool(check.get(key))
            stats[key] += bool(check.get(key))
        if not response:
            counts["no_response"] += 1
            patterns["no_response"] += 1
            continue
        if check.get("tests"):
            continue
        text = log_text(row)
        label = signature(text)
        patterns[label] += 1
        # Keep a concrete saved example per signature for human verification.
        if label not in examples:
            examples[label] = {"task_id": row["task_id"], "project": project,
                "compiled": bool(check.get("compilation")),
                "log_excerpt": "\n".join(text.splitlines()[:24])}
    return {"counts": dict(counts), "log_signatures_heuristic": dict(patterns.most_common()),
            "by_project": {p: dict(v) for p, v in sorted(projects.items())}, "examples": examples,
            "note": "Saved log signatures are diagnostic, not proof of model or environment fault. No generation/evaluation was rerun."}


def inspect(root, mode, baseline):
    folder = root / "modes" / mode / "evaluation_core_v1"
    if not (folder / "summary.json").is_file():
        return {"mode": mode, "evaluation_complete": False}
    rows = [json.loads(p.read_text()) for p in (folder / "tasks").glob("*.json")]
    if len(rows) != 675 or {r["task_id"] for r in rows} != set(range(675)):
        raise ValueError("Completed evaluation must contain all 675 IDs exactly once")
    rows.sort(key=lambda r: r["task_id"])
    experiment = json.loads((folder / "experiment.json").read_text())
    compared = {k: k in experiment and k in baseline and experiment[k] == baseline[k] for k in
                ("dataset", "evaluator_commit", "evaluator_files", "environment")}
    return {"mode": mode, "evaluation_complete": True,
        "summary": json.loads((folder / "summary.json").read_text()),
        "matches_normal_evaluation": compared, **summarize(rows)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path("/projects/F202407648IACDCF2/mario/xrepotest/runs/qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2"))
    p.add_argument("--baseline", type=Path, default=Path("/projects/F202407648IACDCF2/mario/xrepotest/runs/qwen36_35b_thinking_bundle_loading_v4/evaluation/experiment.json"))
    p.add_argument("--modes", nargs="+", choices=MODES, default=["standard", "lsp_context"])
    a = p.parse_args()
    baseline = json.loads(a.baseline.read_text())
    for mode in a.modes:
        report = inspect(a.root, mode, baseline)
        print("\n=== " + mode + " ===")
        print(json.dumps({k: v for k, v in report.items() if k != "examples"}, indent=2))
        for label, example in list(report.get("examples", {}).items())[:8]:
            print("\nExample " + label + " | task " + str(example["task_id"]) + " | " + example["project"])
            print(example["log_excerpt"])


if __name__ == "__main__":
    main()

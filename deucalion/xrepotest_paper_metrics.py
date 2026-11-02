"""Paper-defined metrics over frozen, one-suite-per-task XRepoTest results.

No Ruby execution or model calls. The published weighted mutation aggregate is
reported separately; it is not the MS or MS@Pass defined in Appendix D.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

POLICY = "xrepotest-appendix-d-one-suite-v1"


def summarize(rows):
    ids = [row["task_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate task IDs")
    totals = dict(compiled=0, passed=0, invoked=0, coverage=0.0,
                  mutation_valid=0, mutation_sum=0.0, killed=0, mutants=0)
    missing = 0
    for row in rows:
        tests, checks = row.get("test", []), row.get("checks", [])
        if len(tests) > 1 or len(checks) > 1:
            raise ValueError("This protocol requires at most one final suite per task")
        if not tests:
            if checks:
                raise ValueError("A task without a suite cannot have successful checks")
            missing += 1
            continue
        check = checks[0] if checks else {}
        totals["compiled"] += bool(check.get("compilation"))
        totals["passed"] += bool(check.get("tests"))
        totals["invoked"] += bool(check.get("invocation"))
        coverage = row.get("coverage_stats", [])
        stat = coverage[0] if coverage and isinstance(coverage[0], dict) else {}
        covered, total = stat.get("covered_lines", 0), stat.get("total_lines", 0)
        if not 0 <= covered <= total:
            raise ValueError("Invalid focal coverage counts")
        totals["coverage"] += 100 * covered / total if total else 0
        scores = row.get("mutation_scores", [])
        score = scores[0] if scores and isinstance(scores[0], dict) else {}
        killed, mutants = score.get("killed_count", 0), score.get("total_count", 0)
        if not 0 <= killed <= mutants:
            raise ValueError("Invalid mutation counts")
        if check.get("tests") and check.get("mutation") and mutants > 0:
            totals["mutation_valid"] += 1
            totals["mutation_sum"] += killed / mutants
            totals["killed"] += killed
            totals["mutants"] += mutants
    count = len(rows)
    pct = lambda value, denominator: 100 * value / denominator if denominator else 0.0
    return {"total_tasks": count, "no_tests": missing,
            "compilation_pct": pct(totals["compiled"], count),
            "test_pass_pct": pct(totals["passed"], count),
            "invocation_pct": pct(totals["invoked"], count),
            "focal_line_coverage_macro_pct": totals["coverage"] / count if count else 0.0,
            "mutation": {"passing_tasks": totals["passed"],
                         "valid_measurements": totals["mutation_valid"],
                         "passing_without_valid_measurement": totals["passed"] - totals["mutation_valid"],
                         "MS_pct": pct(totals["mutation_sum"], count),
                         "MS_at_Pass_pct": pct(totals["mutation_sum"], totals["mutation_valid"]),
                         "pooled_killed_pct_diagnostic": pct(totals["killed"], totals["mutants"]),
                         "killed": totals["killed"], "mutants": totals["mutants"]}}


def report(evaluation, selected_ids=None):
    paths = sorted((evaluation / "tasks").glob("*.json"))
    rows = [json.loads(p.read_text()) for p in paths]
    ids = [row["task_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate evaluation task IDs")
    if selected_ids is not None:
        if len(selected_ids) != len(set(selected_ids)) or not set(selected_ids) <= set(ids):
            raise ValueError("Selection is duplicated or has missing evaluation results")
        chosen = set(selected_ids)
        paths = [p for p, row in zip(paths, rows) if row["task_id"] in chosen]
        rows = [row for row in rows if row["task_id"] in chosen]
    groups = defaultdict(list)
    for row in rows:
        groups[row["file_path"].split("/", 1)[0]].append(row)
    manifest = evaluation / "experiment.json"
    return {"policy": POLICY, "task_ids": sorted(row["task_id"] for row in rows),
            "evaluation_manifest": json.loads(manifest.read_text()) if manifest.exists() else None,
            "input_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            "mutation_validity": "UNVERIFIED: formulas alone do not validate subject/test isolation or Mutant execution",
            "summary": summarize(rows),
            "by_project": {name: summarize(values) for name, values in sorted(groups.items())}}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--evaluation", type=Path, required=True)
    p.add_argument("--task-ids", type=Path)
    args = p.parse_args()
    ids = json.loads(args.task_ids.read_text()) if args.task_ids else None
    print(json.dumps(report(args.evaluation, ids), indent=2))


if __name__ == "__main__":
    main()

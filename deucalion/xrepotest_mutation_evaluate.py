"""Measure frozen suites with the same validated mutation executor.

No core evaluations or generated suites are replaced. Terminal measurements,
including unavailable ones, are never repeated. Interrupted work is archived.
"""
import argparse
from collections import Counter, defaultdict
import copy
import json
from pathlib import Path
import tempfile

from benchmark.xrepotest.protocol import DATA_SHA256, atomic_json, load_tasks, locked_run
from benchmark.xrepotest.runtime import environment_manifest, project_environment, validate_evaluator
from benchmark.xrepotest.run import workspace
from benchmark.xrepotest.evaluate import load_responses
from deucalion.xrepotest_mutation_support import POLICY, run_mutant, sha
from deucalion.xrepotest_paper_metrics import summarize

NORMAL = "qwen36_35b_thinking_bundle_loading_v4"
OFFICIAL = "qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2"
ARMS = ("no_coverage", "no_repair", "no_method_retrieval", "no_type_hints", "no_graph")
MODES = ("standard", "lsp_context", "file_context", "rag_bm25", "rag_dense")
LABELS = ("marta",) + ARMS + MODES
SELECTION = "selections/xrepotest_ablation97_v1.json"


def inputs(root, label):
    root = Path(root)
    if label == "marta":
        run = root / "runs" / NORMAL
        return run, run / "generation/processed.jsonl", run / "evaluation", None
    if label in ARMS:
        run = root / "runs" / ("qwen36_35b_ablation97_" + label + "_v1")
        rel = "project_parallel/merged/processed.jsonl" if label == "no_graph" else "generation/processed.jsonl"
        return run, run / rel, run / "evaluation_core_v1", root / SELECTION
    if label in MODES:
        run = root / "runs" / OFFICIAL / "modes" / label
        return run, run / "generation/processed.jsonl", run / "evaluation_core_v1", None
    raise ValueError("Unknown cohort")


def evaluator_hashes():
    import base, ruby
    return {f"{package.__name__}/{f.name}": sha(f)
            for package in (base, ruby) for f in Path(package.__file__).parent.glob("*.py")}


def certificate(path, hashes, environment):
    from deucalion import xrepotest_mutation_support
    d = json.loads(Path(path).read_text())
    projects = {"capybara", "dotenv", "grape", "hanami", "hashie", "httparty", "pundit", "rom", "rspec-core", "shoryuken"}
    if (d.get("policy") != POLICY or d.get("diagnostic_only") is not True
            or d.get("included_in_benchmark") is not False
            or d.get("dataset_sha256") != DATA_SHA256
            or d.get("environment") != environment or not environment
            or d.get("evaluator_files") != hashes
            or d.get("support_sha256") != sha(xrepotest_mutation_support.__file__)
            or d.get("bootstrap_sha256") != sha(Path(__file__).parent / "rb/xrepotest_mutation_bootstrap.rb")
            or set(d.get("controls", {})) != projects
            or d.get("controls_passed") is not True):
        raise ValueError("Diagnostic certificate differs from the validated executor/environment")
    for case in d["controls"].values():
        a, b = case.get("positive", {}), case.get("negative", {})
        if (case.get("passed") is not True or not a.get("valid") or not b.get("valid")
                or not a.get("identity", {}).get("verified") or not b.get("identity", {}).get("verified")
                or a["counts"]["mutations"] != b["counts"]["mutations"]
                or not a["mutation_score"] > b["mutation_score"]):
            raise ValueError("Invalid positive/negative control proof")
    for tid in (4, 155, 220, 416):
        if not d.get("real_suites", {}).get(str(tid), {}).get("valid"):
            raise ValueError("Required real-suite validation missing: " + str(tid))
    return sha(path)


def load_core(core, tasks, responses, processed, hashes, environment):
    manifest = json.loads((core / "experiment.json").read_text())
    summary = json.loads((core / "summary.json").read_text())
    expected = {t["task_id"] for t in tasks}
    if (manifest.get("dataset") != DATA_SHA256 or manifest.get("responses") != sha(processed)
            or manifest.get("evaluator_files") != hashes or manifest.get("environment") != environment
            or summary.get("total_samples") != len(expected)):
        raise ValueError("Frozen core evaluation does not match inputs/evaluator/environment")
    if {p.name for p in (core / "tasks").glob("*.json")} != {str(i) + ".json" for i in expected}:
        raise ValueError("Core evaluation IDs incomplete or foreign")
    rows, row_hashes = {}, {}
    for task in tasks:
        tid = task["task_id"]
        path = core / "tasks" / (str(tid) + ".json")
        row = json.loads(path.read_text())
        if (row.get("task_id") != tid or row.get("file_path") != task["file_path"]
                or row.get("test") != responses[tid]
                or len(row.get("checks", [])) != len(responses[tid])):
            raise ValueError("Core task identity or supplied suite changed: " + str(tid))
        rows[tid], row_hashes[str(tid)] = row, sha(path)
    return rows, row_hashes


def fresh_row(core, status, measurement=None, reason=None):
    row = copy.deepcopy(core)
    row["mutation_scores"] = []  # Discard the old, unverified mutation measurement.
    for check in row.get("checks", []):
        check["mutation"] = status == "valid"
    if status == "valid":
        count = measurement["counts"]
        row["mutation_scores"] = [{"mutation_score": measurement["mutation_score"],
                                  "killed_count": count["kills"], "total_count": count["mutations"],
                                  "escaped_count": count["alive"], "timeout_count": count["timeouts"]}]
    row["mutation_execution"] = {"policy": POLICY, "status": status, "reason": reason,
                                 "measurement": measurement}
    return row


def classify(measurement):
    if measurement.get("valid"):
        return "valid", None
    identity = measurement.get("identity", {})
    if measurement.get("exit_code") is None:
        return "unavailable", "process_timeout"
    if identity and not identity.get("subjects"):
        return "unavailable", "no_mutant_subject"
    if not identity.get("verified"):
        return "unavailable", "startup_or_identity_or_suite_isolation_failure"
    return "unavailable", "incomplete_or_neutral_or_timeout_result"


def recover_measurement(folder, support_hash, bootstrap_hash, task_id):
    path = folder / "result.json"
    if not path.exists():
        return None
    d = json.loads(path.read_text())
    if (d.get("policy") != POLICY or d.get("task_id") != task_id or d.get("action") != "run"
            or d.get("support_sha256") != support_hash or d.get("bootstrap_sha256") != bootstrap_hash):
        raise ValueError("Interrupted measurement provenance differs")
    return d


def finish(output, rows):
    counts = Counter(row["mutation_execution"]["status"] for row in rows)
    reasons = Counter(row["mutation_execution"].get("reason") for row in rows
                      if row["mutation_execution"]["status"] == "unavailable")
    projects = defaultdict(list)
    for row in rows:
        projects[row["file_path"].split("/", 1)[0]].append(row)
    result = {"policy": POLICY, "total_samples": len(rows), "task_ids": [r["task_id"] for r in rows],
              "availability": dict(counts), "unavailable_reasons": dict(reasons),
              "metrics": summarize(rows),
              "by_project": {name: summarize(group) for name, group in sorted(projects.items())},
              "note": "MS uses all tasks, with missing measurements contributing zero; MS@Pass uses passing tasks with valid mutation. Unavailable is not a measured zero score. Pooled ratio is diagnostic only."}
    atomic_json(output / "summary.json", result)
    (output / "detailed_results.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    atomic_json(output / "complete.json", {"policy": POLICY, "tasks": len(rows),
                                         "summary_sha256": sha(output / "summary.json"),
                                         "task_sha256": {str(r["task_id"]): sha(output / "tasks" / (str(r["task_id"]) + ".json")) for r in rows}})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("/data/xrepo"))
    parser.add_argument("--cohort", required=True, choices=LABELS)
    parser.add_argument("--validation", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, default=Path("/app/xrepotest/ruby_functions.jsonl"))
    parser.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    args.root = args.root.resolve()
    run, processed, core, selection = inputs(args.root, args.cohort)
    output = run / "mutation_v1"
    tasks = load_tasks(args.dataset)
    if selection:
        ids = json.loads(selection.read_text())
        if len(ids) != 97 or len(set(ids)) != 97 or any(type(i) is not int for i in ids):
            raise ValueError("Expected the frozen 97-task ablation selection")
        # Compare the cluster selection to the source-controlled one, too.
        if selection.read_bytes() != (Path(__file__).parent / SELECTION).read_bytes():
            raise ValueError("Ablation selection differs from the frozen release")
        tasks = [t for t in tasks if t["task_id"] in set(ids)]
        if len(tasks) != 97:
            raise ValueError("Foreign selection IDs")
    responses = load_responses(processed, tasks)
    hashes, environment = evaluator_hashes(), environment_manifest()
    validate_evaluator(hashes)
    validation_hash = certificate(args.validation, hashes, environment)
    cores, row_hashes = load_core(core, tasks, responses, processed, hashes, environment)
    checked_sources = set()
    for task in tasks:
        path = args.repos / task["file_path"]
        if task["file_path"] not in checked_sources:
            if path.read_text() != task["file_content"]:
                raise ValueError("Benchmark source differs from frozen official task")
            checked_sources.add(task["file_path"])
    from deucalion import xrepotest_mutation_support
    support_hash = sha(xrepotest_mutation_support.__file__)
    bootstrap_hash = sha(Path(__file__).parent / "rb/xrepotest_mutation_bootstrap.rb")
    reference_ids = None
    if args.cohort == "marta":
        reference = args.root / SELECTION
        if reference.read_bytes() != (Path(__file__).parent / SELECTION).read_bytes():
            raise ValueError("Normal ablation reference selection differs from frozen release")
        reference_ids = sorted(json.loads(reference.read_text()))
    config = {"policy": POLICY, "normal_ablation_reference": reference_ids, "cohort": args.cohort, "task_ids": [t["task_id"] for t in tasks],
              "dataset": DATA_SHA256, "processed_sha256": sha(processed),
              "core_manifest_sha256": sha(core / "experiment.json"), "core_task_sha256": row_hashes,
              "core_summary_sha256": sha(core / "summary.json"), "validation_sha256": validation_hash,
              "support_sha256": support_hash, "bootstrap_sha256": bootstrap_hash,
              "runner_sha256": sha(__file__), "metrics_sha256": sha(Path(__file__).with_name("xrepotest_paper_metrics.py")),
              "environment": environment, "evaluator_files": hashes, "timeout": 900}
    print(args.cohort + ": preflight OK; " + str(len(tasks)) + " frozen tasks", flush=True)
    if args.preflight_only:
        return
    with locked_run(output, config):
        for task in tasks:
            for key, path in (("support_sha256", Path(xrepotest_mutation_support.__file__)),
                              ("bootstrap_sha256", Path(__file__).parent / "rb/xrepotest_mutation_bootstrap.rb"),
                              ("runner_sha256", Path(__file__)),
                              ("metrics_sha256", Path(__file__).with_name("xrepotest_paper_metrics.py"))):
                if sha(path) != config[key]:
                    raise ValueError("Executor source changed during the measurement")
            tid = task["task_id"]
            checkpoint = output / "tasks" / (str(tid) + ".json")
            if checkpoint.exists():
                continue
            row = cores[tid]
            if not responses[tid]:
                result = fresh_row(row, "no_tests")
            elif not row["checks"][0].get("tests"):
                result = fresh_row(row, "core_failed")
            else:
                folder = output / "measurements" / str(tid)
                saved = recover_measurement(folder, support_hash, bootstrap_hash, tid)
                if saved is not None:
                    status, reason = classify(saved)
                    result = fresh_row(row, status, saved, reason)
                else:
                    if folder.exists():
                        archive = output / "interrupted_measurements" / str(tid)
                        archive.mkdir(parents=True, exist_ok=True)
                        folder.rename(archive / str(len(list(archive.iterdir())) + 1))
                    name = task["file_path"].split("/", 1)[0]
                    with tempfile.TemporaryDirectory(prefix="xrepo-mutation-") as tmp:
                        repo = Path(tmp) / "repo_data" / name
                        workspace(args.repos / name, repo)
                        from ruby.test_utils import create_ruby_file
                        suite = create_ruby_file(str(repo / task["file_path"].split("/", 1)[1]), task["function_name"], responses[tid][0])
                        try:
                            with project_environment(repo, name):
                                measured = run_mutant(task, Path(suite), repo, folder)
                        except ValueError as exc:
                            # Source checks above exclude missing/changed benchmark files.
                            result = fresh_row(row, "unavailable", reason="subject_resolution: " + str(exc))
                        else:
                            status, reason = classify(measured)
                            result = fresh_row(row, status, measured, reason)
            atomic_json(checkpoint, result)
            print(args.cohort + " task " + str(tid) + ": " + result["mutation_execution"]["status"], flush=True)
        rows = [json.loads((output / "tasks" / (str(t["task_id"]) + ".json")).read_text()) for t in tasks]
        summary = finish(output, rows)
        if args.cohort == "marta":
            ids = set(config["normal_ablation_reference"])
            selected = [row for row in rows if row["task_id"] in ids]
            if len(selected) != 97:
                raise ValueError("Missing normal reference tasks for paired ablation")
            atomic_json(output / "ablation97_summary.json", {"policy": POLICY, "task_ids": sorted(ids),
                        "metrics": summarize(selected), "note": "Subset extracted from the same 675 frozen measurements; no additional execution."})
        print(json.dumps(summary["metrics"]["mutation"], indent=2), flush=True)
        print("Mutation complete: " + str(output / "summary.json"), flush=True)


if __name__ == "__main__":
    main()

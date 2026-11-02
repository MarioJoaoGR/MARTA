"""Offline mutation diagnostics: immutable inputs, disposable controls, no LLM.

Synthetic positive/negative controls are NEVER benchmark results. The report
also inspects exact real generated suites when --generation/--core are supplied.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import tempfile

from benchmark.xrepotest.protocol import atomic_json, load_tasks
from benchmark.xrepotest.run import workspace
from benchmark.xrepotest.runtime import environment_manifest, project_environment, validate_evaluator
from deucalion.xrepotest_mutation_support import POLICY, resolve_subject, run_mutant, sha

CONTROL = "module XRepoMutationControl\n  def self.value(x)\n    x + 1\n  end\nend\n"


def controls(name, source, out):
    results = {}
    with tempfile.TemporaryDirectory(prefix="xrepo-mutant-control-") as tmp:
        repo = Path(tmp) / "repo_data" / name
        workspace(source, repo)
        focal = repo / "xrepo_mutation_control.rb"
        focal.write_text(CONTROL)
        task = {"task_id": "control", "file_path": name + "/xrepo_mutation_control.rb",
                "file_content": CONTROL, "function_name": "value",
                "focal_code": "def self.value(x)\n    x + 1\n  end",
                "function_component": {"start_line": 2, "end_line": 4}}
        # If the integration discovers spec/ by default this fails immediately.
        (repo / "spec/xrepo_forbidden_spec.rb").write_text("raise 'HUMAN_SPEC_SENTINEL_LOADED'\n")
        suite = repo / "spec/temp_spec.rb"
        for label, assertion in (("positive", "expect(XRepoMutationControl.value(2)).to eq(3); expect(XRepoMutationControl.value(-1)).to eq(0)"),
                                  ("negative", "expect(true).to eq(true)")):
            suite.write_text("require " + json.dumps(str(focal)) + "\n"
                             "RSpec.describe 'arbitrary description unrelated to the focal name' do\n"
                             "it('checks the result') { " + assertion + " }\nend\n")
            with project_environment(repo, name):
                results[label] = run_mutant(task, suite, repo, out / label)
        results["passed"] = (results["positive"]["valid"] and results["negative"]["valid"]
            and results["positive"]["mutation_score"] > results["negative"]["mutation_score"]
            and results["positive"]["counts"]["mutations"] == results["negative"]["counts"]["mutations"])
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--dataset", type=Path, default=Path("/app/xrepotest/ruby_functions.jsonl"))
    parser.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    parser.add_argument("--projects", nargs="+")
    parser.add_argument("--generation", type=Path)
    parser.add_argument("--core", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Use a new diagnostic directory; never overwrite evidence")
    if bool(args.generation) != bool(args.core):
        parser.error("Pass generation and its frozen core evaluation together")
    args.output.mkdir(parents=True)
    import base, ruby
    hashes = {f"{package.__name__}/{f.name}": sha(f)
              for package in (base, ruby) for f in Path(package.__file__).parent.glob("*.py")}
    validate_evaluator(hashes)
    tasks = load_tasks(args.dataset)
    names = sorted({t["file_path"].split("/", 1)[0] for t in tasks})
    projects = args.projects or names
    if not set(projects) <= set(names) or len(projects) != len(set(projects)):
        parser.error("Unknown or duplicate project")
    report = {"policy": POLICY, "diagnostic_only": True, "included_in_benchmark": False,
              "dataset_sha256": sha(args.dataset), "environment": environment_manifest(),
              "evaluator_files": hashes, "script_sha256": sha(__file__),
              "support_sha256": sha(Path(__file__).with_name("xrepotest_mutation_support.py")),
              "bootstrap_sha256": sha(Path(__file__).parent / "rb/xrepotest_mutation_bootstrap.rb"),
              "subjects": {}, "controls": {}, "runtime_subjects": {}, "real_suites": {}}
    for task in tasks:
        name = task["file_path"].split("/", 1)[0]
        if name not in projects:
            continue
        try:
            resolved = resolve_subject(task, args.repos / name)
            report["subjects"][str(task["task_id"])] = {"resolved": True, **resolved}
        except (ValueError, OSError) as exc:
            report["subjects"][str(task["task_id"])] = {"resolved": False, "error": str(exc)}
    counts = Counter(r["resolved"] for r in report["subjects"].values())
    print("Static exact source selection: " + str(dict(counts)), flush=True)
    atomic_json(args.output / "report.json", report)
    for name in projects:
        try:
            result = controls(name, args.repos / name, args.output / "controls" / name)
        except Exception as exc:
            result = {"passed": False, "error": repr(exc)}
        report["controls"][name] = result
        print(name + ": controls passed=" + str(result["passed"]), flush=True)
        atomic_json(args.output / "report.json", report)
    # Inspect actual Mutant subjects without running mutation tests or scoring.
    # One source-selected case per project plus the known path/operator cases.
    chosen_subjects = {4, 155, 166, 172, 220, 379, 416}
    for name in projects:
        chosen_subjects.add(next(t["task_id"] for t in tasks if t["file_path"].split("/", 1)[0] == name))
    for task in tasks:
        tid = task["task_id"]
        name = task["file_path"].split("/", 1)[0]
        if tid not in chosen_subjects or name not in projects:
            continue
        with tempfile.TemporaryDirectory(prefix="xrepo-mutant-subject-") as tmp:
            repo = Path(tmp) / "repo_data" / name
            workspace(args.repos / name, repo)
            suite = repo / "spec/temp_spec.rb"
            suite.write_text("RSpec.describe 'subject inspection only' do\nit('is diagnostic') { expect(true).to eq(true) }\nend\n")
            try:
                with project_environment(repo, name):
                    result = run_mutant(task, suite, repo, args.output / "runtime_subjects" / str(tid), action="inspect")
            except Exception as exc:
                result = {"identity": {}, "error": repr(exc)}
            report["runtime_subjects"][str(tid)] = result
            print("Runtime subject " + str(tid) + ": verified=" + str(result.get("identity", {}).get("verified", False)), flush=True)
            atomic_json(args.output / "report.json", report)
    if args.generation:
        from benchmark.xrepotest.evaluate import load_responses
        from ruby.test_utils import create_ruby_file
        responses = load_responses(args.generation / "processed.jsonl", tasks)
        report["processed_sha256"] = sha(args.generation / "processed.jsonl")
        manifest = json.loads((args.core / "experiment.json").read_text())
        if manifest["responses"] != report["processed_sha256"] or manifest["evaluator_files"] != hashes or manifest["environment"] != report["environment"]:
            raise ValueError("Core input/evaluator/environment does not match this diagnostic")
        report["core_manifest_sha256"] = sha(args.core / "experiment.json")
        chosen = {4, 155, 220, 416}
        # First passing suite per project is a diagnostic case, never a new score.
        for name in projects:
            for task in tasks:
                tid = task["task_id"]
                path = args.core / "tasks" / (str(tid) + ".json")
                if task["file_path"].split("/", 1)[0] == name and path.exists():
                    row = json.loads(path.read_text())
                    if any(c.get("tests") for c in row.get("checks", [])):
                        chosen.add(tid)
                        break
        for task in tasks:
            tid = task["task_id"]
            name = task["file_path"].split("/", 1)[0]
            if tid not in chosen or name not in projects:
                continue
            row = json.loads((args.core / "tasks" / (str(tid) + ".json")).read_text())
            if row.get("test") != responses[tid]:
                raise ValueError("Core suite differs from generation for task " + str(tid))
            if not any(c.get("tests") for c in row.get("checks", [])):
                report["real_suites"][str(tid)] = {"skipped": "Core test suite did not pass"}
                continue
            with tempfile.TemporaryDirectory(prefix="xrepo-mutant-real-") as tmp:
                repo = Path(tmp) / "repo_data" / name
                workspace(args.repos / name, repo)
                # Use the same official file creation/path normalization as core.
                suite = create_ruby_file(str(repo / task["file_path"].split("/", 1)[1]),
                                         task["function_name"], responses[tid][0])
                try:
                    with project_environment(repo, name):
                        result = run_mutant(task, Path(suite), repo, args.output / "real_suites" / str(tid))
                except Exception as exc:
                    result = {"valid": False, "error": repr(exc)}
                report["real_suites"][str(tid)] = result
                print("Real task " + str(tid) + ": valid=" + str(result["valid"]), flush=True)
                atomic_json(args.output / "report.json", report)
    report["runtime_verified"] = sum(bool(r.get("identity", {}).get("verified")) for r in report["runtime_subjects"].values())
    report["runtime_checked"] = len(report["runtime_subjects"])
    report["real_valid"] = sum(bool(r.get("valid")) for r in report["real_suites"].values())
    report["controls_passed"] = all(r["passed"] for r in report["controls"].values())
    report["all_675_subjects_resolved"] = len(report["subjects"]) == 675 and all(r["resolved"] for r in report["subjects"].values())
    atomic_json(args.output / "report.json", report)
    print("Diagnostic complete: " + str(args.output / "report.json"), flush=True)
    if not report["controls_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

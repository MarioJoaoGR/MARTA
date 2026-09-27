"""Offline environment diagnostics; fixed tests, no LLM or benchmark results.

Run in the repaired image with /app and MARTA on PYTHONPATH. Every project
uses a disposable copy and its original RSpec configuration/spec helper.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

from benchmark.xrepotest.protocol import atomic_json, load_tasks
from benchmark.xrepotest.run import workspace
from benchmark.xrepotest.runtime import environment_manifest, project_environment, validate_evaluator
from benchmark.xrepotest.environment.repair_evaluator import evaluator_hashes


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report", type=Path, required=True)
    args = p.parse_args()
    from ruby.evaluator import RubyEvaluator
    validate_evaluator(evaluator_hashes(Path("/app")))
    tasks = load_tasks(Path("/app/xrepotest/ruby_functions.jsonl"))
    for task in tasks:
        if (Path("/app/repo_data") / task["file_path"]).read_text() != task["file_content"]:
            raise RuntimeError(f"Changed focal source: task {task['task_id']}")
    result = {"diagnostic_only": True, "environment": environment_manifest(),
              "tasks_verified": len(tasks),
              "focal_files_verified": len({t["file_path"] for t in tasks}),
              "rspec": {}, "official_evaluator": {}}
    original_cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="xrepo-environment-") as tmp:
        for name in sorted(result["environment"]["projects"]):
            task_root = Path(tmp) / name
            root = task_root / "repo_data" / name
            workspace(Path("/app/repo_data") / name, root)
            spec = root / "spec/temp_spec.rb"
            spec.parent.mkdir(exist_ok=True, parents=True)
            spec.write_text('require "rspec"\nRSpec.describe "environment diagnostic" do\n'
                            '  it("executes an example") { expect(1).to eq(1) }\nend\n')
            with project_environment(root, name):
                proc = subprocess.run(["bundle", "exec", "rspec", str(spec), "--format", "progress"],
                                      cwd=root, capture_output=True, text=True, timeout=120)
            result["rspec"][name] = {"exit": proc.returncode, "output": (proc.stdout + proc.stderr)[-6000:]}
            print(f"{name}: RSpec exit {proc.returncode}", flush=True)
            atomic_json(args.report, result)
        diagnostics = {
            172: ('require "rspec"\nrequire "hashie"\nRSpec.describe "Hashie::Hash#to_hash" do\n'
                  '  it("converts") { expect(Hashie::Hash.new.merge(a: 7).to_hash).to eq({a: 7}) }\nend\n'),
            596: ('require "rspec"\nrequire "hanami"\nRSpec.describe "Hanami.app" do\n'
                  '  it("requires configuration") { expect { Hanami.app }.to raise_error(Hanami::AppLoadError) }\nend\n'),
            468: ('require "rspec"\nrequire "rom/core"\nRSpec.describe "ROM::Relation::Loaded#one" do\n'
                  '  it("returns one tuple") { expect(ROM::Relation::Loaded.new(nil, [7]).one).to eq(7) }\nend\n'),
            379: ('require "rspec"\nrequire "shoryuken"\nRSpec.describe Shoryuken::Polling::QueueConfiguration do\n'
                  '  it("compares a queue name") { expect(described_class.new("q", {}) == "q").to eq(true) }\nend\n'),
        }
        # Regression: an earlier dependency with the same basename must never
        # replace the focal file. These only load code; they are not LLM tests.
        for tid, entry in ((413, "rom/core"), (461, "rom/core"), (492, "rom/repository")):
            diagnostics[tid] = (f'require "rspec"\nrequire "{entry}"\n'
                                'RSpec.describe "coverage file identity" do\n'
                                '  it("executes") { expect(1).to eq(1) }\nend\n')
        for tid, spec in diagnostics.items():
            task = next(dict(t) for t in tasks if t["task_id"] == tid)
            name = task["file_path"].split("/")[0]
            task_root = Path(tmp) / name
            root = task_root / "repo_data" / name
            task["test"] = [spec]
            try:
                os.chdir(task_root)
                failures = []
                original_run = subprocess.run

                def observe(*call_args, **kwargs):
                    proc = original_run(*call_args, **kwargs)
                    if proc.returncode:
                        failures.append({"command": call_args[0], "exit": proc.returncode,
                                         "stderr": (proc.stderr or "")[-6000:]})
                    return proc

                with project_environment(root, name):
                    try:
                        # Observe, without changing commands, outputs or scores.
                        subprocess.run = observe
                        detailed, _ = RubyEvaluator().evaluate_dataset([task], enable_mutation_testing=(tid == 172))
                    finally:
                        subprocess.run = original_run
                result["official_evaluator"][str(tid)] = {
                    key: detailed[0].get(key) for key in ("checks", "coverage_stats", "mutation_scores", "logs")}
                result["official_evaluator"][str(tid)]["subprocess_failures"] = failures
                print(f"task {tid}: {detailed[0]['checks']}", flush=True)
                atomic_json(args.report, result)
            finally:
                os.chdir(original_cwd)
    failed = [n for n, r in result["rspec"].items() if r["exit"]]
    for tid, r in result["official_evaluator"].items():
        if not all(c.get("compilation") and c.get("tests") and c.get("coverage") for c in r["checks"]):
            failed.append(tid)
        if not any(c and c["covered_lines"] > 0 for c in r["coverage_stats"]):
            failed.append(tid + ": no focal coverage")
    if result["official_evaluator"]["172"]["mutation_scores"][0]["total_count"] <= 0:
        failed.append("mutation")
    for tid, total in (("413", 7), ("461", 6), ("492", 8)):
        stats = result["official_evaluator"][tid]["coverage_stats"]
        if len(stats) != 1 or not stats[0] or stats[0]["total_lines"] != total:
            failed.append(tid + ": wrong focal file/range")
    result["ready"] = not failed
    atomic_json(args.report, result)
    if failed:
        raise SystemExit(f"Environment diagnostics failed: {failed}")


if __name__ == "__main__":
    main()

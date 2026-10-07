"""Observe the frozen evaluator on exact exported suites in disposable copies.

Run original and proposal separately. Never change benchmark/evaluation files,
reuse a measurement, generate tests, install packages, or select better answers.
The proposal changes configuration ONLY, not upstream mutation parsing/scoring.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import yaml

from benchmark.xrepotest.protocol import atomic_json, load_tasks
from benchmark.xrepotest.run import workspace
from benchmark.xrepotest.runtime import environment_manifest, project_environment, validate_evaluator

POLICY = "mutation-config-diagnostic-v1"


def guard_source(test, subject):
    # Bind every supplied example to the measured subject, independent of its
    # description. Disable examples from other files; never fabricate tests.
    return ("require 'rspec'\nRSpec.configure do |config|\n"
            "  config.define_derived_metadata do |metadata|\n"
            "    path = metadata[:absolute_file_path] || metadata[:file_path]\n"
            "    supplied = path && File.expand_path(path) == " + json.dumps(str(test.resolve())) + "\n"
            "    metadata[:mutant] = !!supplied\n"
            "    metadata[:mutant_expression] = " + json.dumps(subject) + " if supplied\n"
            "  end\nend\n")


def observe(task, response, source, name, mode):
    from ruby.evaluator import RubyEvaluator
    original_run, original_dump = subprocess.run, yaml.dump
    trace, configurations = [], []
    with tempfile.TemporaryDirectory(prefix="xrepo-mutation-diagnostic-") as tmp:
        target = Path(tmp) / "repo_data" / name
        workspace(source, target)
        sample = copy.deepcopy(task)
        sample["test"] = response
        old = Path.cwd()

        def run(*args, **kwargs):
            proc = original_run(*args, **kwargs)
            command = args[0] if args else kwargs.get("args")
            if isinstance(command, list) and "mutant" in command:
                trace.append({"command": command, "exit": proc.returncode,
                              "stdout": proc.stdout or "", "stderr": proc.stderr or ""})
            return proc

        def dump(value, *args, **kwargs):
            value = copy.deepcopy(value)
            if isinstance(value, dict) and "matcher" in value and "integration" in value:
                if mode == "isolation_proposal":
                    subject = value["matcher"]["subjects"][0]
                    helper = target / "spec/.xrepo_mutation_guard.rb"
                    helper.write_text(guard_source(target / "spec/temp_spec.rb", subject))
                    value["integration"] = {"name": "rspec", "arguments": ["--options", "/dev/null", "spec/temp_spec.rb"]}
                    # RSpec before spec_helper; the integration loads the suite
                    # exactly once. Explicit arguments stop default spec/ discovery.
                    value["requires"] = ["rspec", str(helper), "./spec/spec_helper.rb"]
                configurations.append(copy.deepcopy(value))
            return original_dump(value, *args, **kwargs)

        try:
            os.chdir(target.parent.parent)
            with project_environment(target, name):
                subprocess.run, yaml.dump = run, dump
                try:
                    result, _ = RubyEvaluator().evaluate_dataset([sample], enable_mutation_testing=True)
                finally:
                    subprocess.run, yaml.dump = original_run, original_dump
            row = result[0]
            return {"mode": mode, "checks": row["checks"],
                    "mutation_scores": row.get("mutation_scores", []),
                    "logs": [v.decode(errors="replace") if isinstance(v, bytes) else v for v in row.get("logs", [])],
                    "mutant_subprocesses": trace, "configurations": configurations}
        finally:
            os.chdir(old)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dataset", type=Path, default=Path("/app/xrepotest/ruby_functions.jsonl"))
    p.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    p.add_argument("--generation", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    p.add_argument("--ids", nargs="+", type=int, default=[155, 220, 4, 416])
    args = p.parse_args()
    if args.output.exists():
        raise ValueError("Use a new diagnostic output directory")
    if len(args.ids) != len(set(args.ids)):
        raise ValueError("Duplicate diagnostic IDs")
    args.output.mkdir(parents=True)
    import base, ruby
    hashes = {f"{package.__name__}/{f.name}": hashlib.sha256(f.read_bytes()).hexdigest()
              for package in (base, ruby) for f in Path(package.__file__).parent.glob("*.py")}
    validate_evaluator(hashes)
    tasks = {t["task_id"]: t for t in load_tasks(args.dataset)}
    processed = args.generation / "processed.jsonl"
    records = [json.loads(line) for line in processed.read_text().splitlines() if line.strip()]
    if len(records) != len({r["task_id"] for r in records}):
        raise ValueError("Duplicate exported suites")
    responses = {r["task_id"]: r["response"] for r in records}
    audit = {"policy": POLICY, "diagnostic_only": True, "environment": environment_manifest(),
             "evaluator_sha256": hashes, "processed_sha256": hashlib.sha256(processed.read_bytes()).hexdigest(),
             "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             "task_ids": args.ids, "cases": {}}
    for tid in args.ids:
        task = tasks[tid]
        name, rel = task["file_path"].split("/", 1)
        source = args.repos / name
        if (source / rel).read_text() != task["file_content"]:
            raise ValueError("Focal Ruby source differs from the official task")
        response = responses[tid]
        if not response or len(response) != 1 or not response[0].strip():
            raise ValueError("Diagnostic requires exactly one frozen generated suite")
        case = {"suite_sha256": hashlib.sha256(response[0].encode()).hexdigest(), "project": name}
        for mode in ("published", "isolation_proposal"):
            case[mode] = observe(task, response, source, name, mode)
            checks = case[mode]["checks"]
            print(f"task {tid} [{mode}]: {checks}", flush=True)
            for proc in case[mode]["mutant_subprocesses"]:
                print(f"Mutant exit {proc['exit']}; stderr: {proc['stderr'][:1200]}", flush=True)
        audit["cases"][str(tid)] = case
        atomic_json(args.output / "report.json", audit)
    print("Diagnostic saved: " + str(args.output / "report.json"), flush=True)


if __name__ == "__main__":
    main()

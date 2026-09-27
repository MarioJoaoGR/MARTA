"""Task-isolated execution of the pinned XRepoTest evaluator with recorded fixes.

Run under the official image's Python with the pinned environment source on
PYTHONPATH. Checkpoints allow CPU jobs to resume without redoing completed tasks.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil

from .protocol import (DATA_SHA256, IMAGE, UPSTREAM_COMMIT, atomic_json, digest,
                       load_tasks, locked_run)
from .run import workspace
from .runtime import environment_manifest, project_environment, validate_evaluator


def load_responses(path, tasks):
    rows = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    ids = [r["task_id"] for r in rows]
    if (any(type(i) is not int for i in ids) or len(set(ids)) != len(ids)
            or set(ids) != {t["task_id"] for t in tasks}):
        raise ValueError("Responses must contain every official task exactly once")
    for r in rows:
        response = r.get("response")
        if not isinstance(response, list) or len(response) > 1:
            raise ValueError("MARTA exports zero or one final suite per task")
        if any(not isinstance(s, str) or not s.strip() for s in response):
            raise ValueError("Use [] for no test, not an empty or invalid Ruby string")
    return {r["task_id"]: r["response"] for r in rows}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dataset", type=Path, required=True)
    p.add_argument("--processed", type=Path, required=True)
    p.add_argument("--repos", type=Path, default=Path("/app/repo_data"))
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    p.add_argument("--enable-mutation", action="store_true")
    args = p.parse_args()
    for key in ("dataset", "processed", "repos", "output", "work"):
        setattr(args, key, getattr(args, key).resolve())
    tasks = load_tasks(args.dataset)
    responses = load_responses(args.processed, tasks)
    from ruby.evaluator import RubyEvaluator
    from base.metrics import calculate_summary
    import base, ruby
    # Record the code actually imported, not just a claimed Git revision.
    evaluator_hashes = {f"{package.__name__}/{f.name}": hashlib.sha256(f.read_bytes()).hexdigest()
                        for package in (base, ruby)
                        for f in Path(package.__file__).parent.glob("*.py")}
    validate_evaluator(evaluator_hashes)
    config = {"dataset": DATA_SHA256, "image": IMAGE, "evaluator_commit": UPSTREAM_COMMIT,
              "environment": environment_manifest(),
              "evaluator_files": evaluator_hashes,
              "responses": hashlib.sha256(args.processed.read_bytes()).hexdigest(),
              "adapter": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "mutation": args.enable_mutation}
    if args.output == args.work or args.output in args.work.parents or args.work in args.output.parents:
        p.error("Evaluation outputs and work must be separate trees")
    with locked_run(args.output, config):
        for task in tasks:
            tid = task["task_id"]
            saved = args.output / "tasks" / f"{tid}.json"
            if saved.exists():
                continue
            name = task["file_path"].split("/", 1)[0]
            task_root = args.work / str(tid)
            target_repo = task_root / "repo_data" / name
            workspace(args.repos / name, target_repo)
            sample = copy.deepcopy(task)
            sample["test"] = responses[tid]
            old = Path.cwd()
            try:
                os.chdir(task_root)
                with project_environment(target_repo, name):
                    detailed, _ = RubyEvaluator().evaluate_dataset([sample],
                        enable_mutation_testing=args.enable_mutation)
                if len(detailed) != 1 or detailed[0]["task_id"] != tid:
                    raise RuntimeError(f"Official evaluator returned no result for task {tid}")
                if isinstance(detailed[0].get("logs"), list):
                    detailed[0]["logs"] = [x.decode("utf-8", errors="replace") if isinstance(x, bytes) else x
                                            for x in detailed[0]["logs"]]
                atomic_json(saved, detailed[0])
            finally:
                os.chdir(old)
                shutil.rmtree(target_repo)
        results = [json.loads((args.output / "tasks" / f"{t['task_id']}.json").read_text()) for t in tasks]
        summary = calculate_summary(results)
        if summary["total_samples"] != len(tasks):
            raise RuntimeError("Evaluation denominator changed")
        atomic_json(args.output / "summary.json", summary)
        (args.output / "detailed_results.jsonl").write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in results))
        print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

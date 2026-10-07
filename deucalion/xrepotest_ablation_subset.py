"""Fix a project-stratified task subset without reading experiment outcomes."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

from benchmark.xrepotest.protocol import DATA_SHA256, atomic_json, digest, load_tasks


def select(tasks, per_project, seed):
    groups = defaultdict(list)
    for task in tasks:
        groups[task["file_path"].split("/", 1)[0]].append(task["task_id"])
    ids = [tid for values in groups.values() for tid in values]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate task IDs")
    if not groups or type(per_project) is not int or per_project < 1:
        raise ValueError("Per-project quota must be a positive integer")
    allocation = {name: min(per_project, len(values)) for name, values in groups.items()}
    chosen = []
    for name in sorted(groups):
        ranked = sorted(groups[name], key=lambda tid: (
            hashlib.sha256(f"{seed}\0{name}\0{tid}".encode()).hexdigest(), tid))
        chosen.extend(ranked[:allocation[name]])
    return sorted(chosen), allocation


def save(path, value):
    if path.exists():
        if json.loads(path.read_text()) != value:
            raise ValueError("Refusing to change an existing selection: " + str(path))
        return
    atomic_json(path, value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--per-project", type=int, default=10)
    parser.add_argument("--seed", default="marta-xrepo-ablation-v1")
    parser.add_argument("--output", type=Path, required=True, help="JSON list of official task IDs")
    args = parser.parse_args()
    ids, allocation = select(load_tasks(args.dataset), args.per_project, args.seed)
    audit = {"policy": "project-balanced-sha256-v1", "dataset": DATA_SHA256,
             "seed": args.seed, "count": len(ids), "per_project": args.per_project, "task_ids": ids,
             "selection_digest": digest(ids), "by_project": allocation,
             "allocation": "Equal per-project quota capped by available official tasks; no redistribution",
             "ranking": "SHA256(seed, project, task_id); no generation or evaluation results read"}
    save(args.output.with_suffix(".audit.json"), audit)
    save(args.output, ids)
    print(json.dumps(audit, indent=2))
    print("Selection saved: " + str(args.output))


if __name__ == "__main__":
    main()

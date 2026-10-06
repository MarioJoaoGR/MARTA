"""Audit the single coverage-output repair before resuming an interrupted run.

Only the recorded predecessor and this exact repaired code are accepted.
All configuration fields other than marta_code and all saved results survive.
The existing runner archives/restarts incomplete tasks on its next invocation.
"""
import argparse
from collections import Counter
import fcntl
import hashlib
import json
from pathlib import Path

from benchmark.xrepotest.protocol import SCHEMA, atomic_json, code_fingerprint

LEGACY_CODE = "5f731f30e02f62264900a96b2c7efc5f33d4dfff08cbc33c41dab25eb0720d85"
REPAIRED_CODE = "a228546b373026930b1bfdb44bb8f4cd342a25da87a16ac99503496180529031"
AUDIT = "coverage_output_upgrade.json"


def snapshot(root):
    files = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("Unexpected symlink in saved results: " + str(path))
        if path.is_file() and path not in {root / "experiment.json", root / "run.lock", root / AUDIT}:
            h = hashlib.sha256()
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    h.update(chunk)
            files[str(path.relative_to(root))] = h.hexdigest()
    return files


def upgrade(root):
    root = Path(root).resolve()
    manifest = root / "experiment.json"
    if not manifest.is_file():
        raise ValueError("An existing experiment.json is required")
    # Match both locks held by the cluster wrapper and the Python runner.
    with (root.parent / "generation-job.lock").open("a") as job_lock, (root / "run.lock").open("a") as run_lock:
        fcntl.flock(job_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        fcntl.flock(run_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if code_fingerprint() != REPAIRED_CODE:
            raise ValueError("Code differs from the exact coverage-output repair")
        before = json.loads(manifest.read_text())
        audit_path = root / AUDIT
        previous = json.loads(audit_path.read_text()) if audit_path.exists() else None
        if previous:
            expected_after = {**previous["before"], "marta_code": REPAIRED_CODE}
            if (previous["before"].get("marta_code") != LEGACY_CODE
                    or previous["after"] != expected_after):
                raise ValueError("Invalid saved upgrade audit")
            if before == previous["after"]:
                return previous
            if before != previous["before"]:
                raise ValueError("Manifest differs from both audited versions")
        if before.get("schema") != SCHEMA or before.get("marta_code") != LEGACY_CODE:
            raise ValueError("Only the exact interrupted predecessor can be upgraded")
        if (root / "processed.jsonl").exists():
            raise ValueError("An exported experiment cannot be upgraded in place")
        states = {}
        for path in sorted(root.glob("tasks/*/state.json")):
            state = json.loads(path.read_text())
            status, tid = state.get("status"), state.get("task_id")
            if (type(tid) is not int or str(tid) != path.parent.name
                    or status not in {"complete", "no_tests", "running"}):
                raise ValueError("Invalid task state: " + str(path))
            final = path.parent / "final_spec.rb"
            if status == "complete" and (not final.is_file() or not final.read_text().strip()):
                raise ValueError("Completed task has no final suite: " + str(path))
            if status == "no_tests" and final.exists():
                raise ValueError("No-tests task has a final suite: " + str(path))
            states[str(tid)] = status
        if "running" not in states.values():
            raise ValueError("Expected an interrupted generation task")
        for path in root.glob("analysis/*/calls/*.json"):
            response = json.loads(path.read_text()).get("response")
            if not isinstance(response, str) or not response.strip():
                raise ValueError("Invalid summary checkpoint: " + str(path))
        files = snapshot(root)
        audit = {
            "reason": "Keep coverage JSON on the original pipe when application code redirects stdout",
            "before": before, "after": {**before, "marta_code": REPAIRED_CODE},
            "task_states": states, "preserved_files": files,
            "restart": "Existing policy: archive and restart only running tasks; skip complete/no_tests",
            "scope": "MARTA coverage feedback transport only; prompts, budgets, tasks and final evaluator unchanged",
        }
        if previous and previous != audit:
            raise ValueError("Saved results changed during an interrupted upgrade")
        if not previous:
            atomic_json(audit_path, audit)
        atomic_json(manifest, audit["after"])
        return audit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("generation", type=Path)
    args = parser.parse_args()
    audit = upgrade(args.generation)
    print("Upgrade verified: {} files preserved".format(len(audit["preserved_files"])))
    print("Task states: " + str(dict(Counter(audit["task_states"].values()))))
    print("Audit: " + str(args.generation / AUDIT))


if __name__ == "__main__":
    main()

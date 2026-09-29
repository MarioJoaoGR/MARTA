"""Audited recovery of the 74c02124a run after an empty generation response.

No model, dataset, environment, prompt budget or finished task is changed.
Only the known predecessor can opt into the corrected empty-length handling.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
from pathlib import Path

from .protocol import SCHEMA, atomic_json, code_fingerprint
from .run import GENERATION_EMPTY_LENGTH_POLICY

LEGACY_CODE = "a2ceb8a036474c9da88517d40b6bfdd7f05e568a6469e6c4832ec219fe3cc0f9"


def upgrade(root: Path) -> dict:
    root = root.resolve()
    manifest = root / "experiment.json"
    if not manifest.is_file():
        raise ValueError("No experiment.json: only existing guarded runs can be upgraded")
    with (root / "run.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        before = json.loads(manifest.read_text())
        audit_path = root / "generation_empty_upgrade.json"
        current_code = code_fingerprint()
        previous_audit = json.loads(audit_path.read_text()) if audit_path.exists() else None
        if previous_audit:
            if previous_audit["after"].get("marta_code") != current_code:
                raise ValueError("Code changed since upgrade")
            if before == previous_audit["after"]:
                return previous_audit
            if before != previous_audit["before"]:
                raise ValueError("Manifest differs from both audited versions")
        if before.get("schema") != SCHEMA or before.get("marta_code") != LEGACY_CODE:
            raise ValueError("Only the exact 74c02124a fingerprint can be upgraded")
        if before.get("summary_truncation_attempts") != 3 or "generation_empty_length_policy" in before:
            raise ValueError("Unexpected predecessor policy")
        if (root / "processed.jsonl").exists():
            raise ValueError("An exported experiment must not be upgraded in place")
        states = {}
        for path in sorted(root.glob("tasks/*/state.json")):
            state = json.loads(path.read_text())
            status = state.get("status")
            if status not in {"complete", "no_tests", "running"}:
                raise ValueError(f"Unexpected task state: {path}")
            if str(state.get("task_id")) != path.parent.name:
                raise ValueError(f"Task identity mismatch: {path}")
            final = path.parent / "final_spec.rb"
            if status == "complete" and (not final.is_file() or not final.read_text().strip()):
                raise ValueError(f"Completed task has no final suite: {path}")
            if status == "no_tests" and final.exists():
                raise ValueError(f"No-tests task has a final suite: {path}")
            states[path.parent.name] = status
        if not states or "running" not in states.values():
            raise ValueError("Expected an interrupted generation task")
        files = {}
        for folder in (root / "analysis", root / "tasks"):
            for path in sorted(folder.rglob("*")):
                if path.is_symlink():
                    raise ValueError(f"Unexpected symlink in saved results: {path}")
                if path.is_file():
                    if path.parent.name == "calls" and path.suffix == ".json":
                        response = json.loads(path.read_text()).get("response")
                        if not isinstance(response, str) or not response.strip():
                            raise ValueError(f"Invalid summary checkpoint: {path}")
                    files[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
        after = {**before, "marta_code": current_code,
                 "generation_empty_length_policy": GENERATION_EMPTY_LENGTH_POLICY}
        audit = {
            "reason": "Empty length responses consume existing generation attempts; record failed calls",
            "before": before, "after": after, "task_states": states, "preserved_files": files,
            "restart": "Only running tasks restart; their old files are archived on resume",
            "telemetry_note": "The predecessor did not record generation calls that raised. Historical LLM totals may be incomplete; retain Ollama/Slurm logs.",
            "context_note": "Full production analysis is now unconditional; XRepoTest already used full_context=True.",
        }
        if previous_audit and previous_audit != audit:
            raise ValueError("Saved results changed during an interrupted upgrade")
        if not previous_audit:
            atomic_json(audit_path, audit)
        atomic_json(manifest, after)
        return audit


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("generation", type=Path)
    args = p.parse_args()
    audit = upgrade(args.generation)
    print(f"Upgrade verified: {len(audit['preserved_files'])} files preserved")
    print(f"Task states: {audit['task_states']}")
    print(f"Audit: {args.generation / 'generation_empty_upgrade.json'}")


if __name__ == "__main__":
    main()

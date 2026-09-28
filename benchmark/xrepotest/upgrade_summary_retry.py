"""Explicit, audited upgrade of the pre-generation run from a7bfb697a.

Only the known old code fingerprint is accepted. No model/config/source fields
are relaxed by guard_run; the ordinary preflight checks still run on resume.
"""
from __future__ import annotations

import argparse
import fcntl
import json
from pathlib import Path

from .protocol import SCHEMA, atomic_json, code_fingerprint, digest
from .run import SUMMARY_TRUNCATION_ATTEMPTS

LEGACY_CODE = "af40b7a865fb55b433f998211b7f0617b789a8fc2650510fa5ccd6f8467f88ba"


def upgrade(root: Path) -> dict:
    root = root.resolve()
    manifest = root / "experiment.json"
    if not manifest.is_file():
        raise ValueError("No experiment.json: this command only upgrades an existing run")
    with (root / "run.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        before = json.loads(manifest.read_text())
        audit_path = root / "summary_retry_upgrade.json"
        current_code = code_fingerprint()
        if audit_path.exists():
            audit = json.loads(audit_path.read_text())
            if audit["after"].get("marta_code") != current_code:
                raise ValueError("Code changed since upgrade: refusing another migration")
            if before == audit["after"]:
                return audit
            if before != audit["before"]:
                raise ValueError("Manifest differs from both audited versions")
        if before.get("schema") != SCHEMA or before.get("marta_code") != LEGACY_CODE:
            raise ValueError("Only the exact a7bfb697a experiment fingerprint can be upgraded")
        if "summary_truncation_attempts" in before:
            raise ValueError("Unexpected retry policy in legacy manifest")
        if (root / "processed.jsonl").exists() or any((root / "tasks").glob("*/state.json")):
            raise ValueError("Generation has started: this migration only accepts analysis-only runs")
        checkpoints = {}
        for path in sorted(root.glob("analysis/*/calls/*.json")):
            content = json.loads(path.read_text())
            if not isinstance(content.get("response"), str) or not content["response"].strip():
                raise ValueError(f"Invalid summary checkpoint: {path}")
            checkpoints[str(path.relative_to(root))] = digest(content)
        if not checkpoints:
            raise ValueError("No valid summary checkpoints to preserve")
        after = {**before, "marta_code": current_code,
                 "summary_truncation_attempts": SUMMARY_TRUNCATION_ATTEMPTS}
        audit = {"reason": "Bounded retries of truncated summaries; per-attempt telemetry",
                 "before": before, "after": after, "checkpoints": checkpoints,
                 "checkpoint_count": len(checkpoints)}
        if audit_path.exists():
            if json.loads(audit_path.read_text()) != audit:
                raise ValueError("Checkpoints changed during an interrupted upgrade")
        else:
            # Retain the full original configuration before replacing it.
            atomic_json(audit_path, audit)
        atomic_json(manifest, after)
        return audit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("generation", type=Path)
    args = parser.parse_args()
    result = upgrade(args.generation)
    print(f"Upgrade verified: {result['checkpoint_count']} summary checkpoints preserved")
    print(f"Audit: {args.generation / 'summary_retry_upgrade.json'}")


if __name__ == "__main__":
    main()

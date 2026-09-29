"""Start a fresh generation experiment with audited, compatible analysis reuse.

Only the exact 9c3696d12 predecessor is accepted. Generated tests, task states
and generation telemetry are never copied. Existing analysis caches retain
their normal source/model/prompt validation when the new pipeline loads them.
"""
import argparse
import fcntl
import hashlib
import json
from pathlib import Path
import shutil

from .protocol import SCHEMA, atomic_json, code_fingerprint
from .report import summarize
from marta.ruby_backend.loading import LOADING_POLICY

SOURCE_CODE = "f72e37b8ed1b45de3e79751b79f0d774e26b75c48f9a1c1f92797f783d061506"


def fork(source: Path, destination: Path):
    source, destination = source.resolve(), destination.resolve()
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError("Old and new experiments must be separate directory trees")
    if not (source / "experiment.json").is_file():
        raise ValueError("Source is not a guarded experiment")
    destination.mkdir(parents=True, exist_ok=True)
    with (source / "run.lock").open("a") as old_lock, (destination / "run.lock").open("a") as new_lock:
        fcntl.flock(old_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        fcntl.flock(new_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        before = json.loads((source / "experiment.json").read_text())
        if before.get("schema") != SCHEMA or before.get("marta_code") != SOURCE_CODE:
            raise ValueError("Only the exact 9c3696d12 predecessor can supply this analysis")
        if before.get("context") != "production-project" or before.get("no_graph") is not False:
            raise ValueError("Expected the normal full-production analysis arm")
        after = {**before, "marta_code": code_fingerprint(), "generation_loading_policy": LOADING_POLICY}
        audit_path = destination / "analysis_reuse.json"
        manifest = destination / "experiment.json"
        if manifest.exists():
            if not audit_path.exists():
                raise ValueError("Destination is already an unrelated experiment")
            audit = json.loads(audit_path.read_text())
            if (json.loads(manifest.read_text()) != after or audit["source"] != str(source)
                    or audit["before"] != before or audit["after"] != after):
                raise ValueError("Destination configuration or reuse provenance differs")
            return audit
        if any(p.name not in {"run.lock", "analysis", "analysis_reuse.json"} for p in destination.iterdir()):
            raise ValueError("Destination contains unrelated outputs")
        files = {}
        checkpoints = 0
        for path in sorted((source / "analysis").rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Unexpected symlink in analysis: {path}")
            if not path.is_file() or path.name in {"events.jsonl", "analysis.json"} or path.suffix == ".tmp":
                continue
            if path.parent.name == "calls" and path.suffix == ".json":
                value = json.loads(path.read_text()).get("response")
                if not isinstance(value,str) or not value.strip():
                    raise ValueError(f"Invalid summary checkpoint: {path}")
                checkpoints += 1
            files[str(path.relative_to(source))] = hashlib.sha256(path.read_bytes()).hexdigest()
        if not checkpoints:
            raise ValueError("No summary checkpoints to reuse")
        for path in (destination / "analysis").rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Unexpected symlink in destination analysis: {path}")
            if path.is_file() and str(path.relative_to(destination)) not in files:
                if path.name.endswith(".reuse-partial") and str(path.relative_to(destination))[:-14] in files:
                    continue
                raise ValueError(f"Destination contains unrelated analysis: {path}")
        audit = {"source": str(source), "before": before, "after": after,
                 "files": files, "checkpoint_count": checkpoints,
                 "source_analysis_usage": summarize(source / "analysis"),
                 "reason": "Generation loading guidance corrected; summary prompts and identities unchanged",
                 "scope": "Only analysis caches/checkpoints/vectors; all generation tasks restart",
                 "note": "Inherited analysis cost is recorded separately and is not new GPU consumption."}
        if audit_path.exists() and json.loads(audit_path.read_text()) != audit:
            raise ValueError("Source analysis changed during interrupted copy")
        atomic_json(audit_path, audit)
        for rel, expected in files.items():
            output = destination / rel
            if output.exists():
                if hashlib.sha256(output.read_bytes()).hexdigest() != expected:
                    raise ValueError(f"Copied analysis differs: {rel}")
                continue
            output.parent.mkdir(parents=True, exist_ok=True)
            partial = output.with_name(output.name + ".reuse-partial")
            shutil.copy2(source / rel, partial)
            if hashlib.sha256(partial.read_bytes()).hexdigest() != expected:
                raise ValueError(f"Source analysis changed while copying: {rel}")
            partial.replace(output)
        atomic_json(manifest, after)
        return audit


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", type=Path)
    p.add_argument("destination", type=Path)
    args = p.parse_args()
    audit = fork(args.source,args.destination)
    print(f"Fresh generation prepared: {audit['checkpoint_count']} summary checkpoints reused")
    print(f"Audit: {args.destination / 'analysis_reuse.json'}")


if __name__ == "__main__":
    main()

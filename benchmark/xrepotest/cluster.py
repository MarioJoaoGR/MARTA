"""Offline cluster gates and local Ollama metadata; never requests inference."""
import argparse
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

from .protocol import atomic_json


def certified(root):
    preflight = json.loads((root / "reports/preflight.json").read_text())
    diagnostics = json.loads((root / "reports/environment-diagnostics.json").read_text())
    if not (preflight.get("ready") and preflight.get("runtime_checked")
            and preflight.get("mutation_ready") and diagnostics.get("ready")):
        raise ValueError("XRepoTest preparation and environment diagnostics must both pass")
    if preflight.get("environment") != diagnostics.get("environment"):
        raise ValueError("Diagnostic and preflight environments differ")


def model_metadata(host, model):
    def query(path, payload=None):
        data = json.dumps(payload).encode() if payload is not None else None
        request = Request(host + path, data=data, headers={"Content-Type": "application/json"})
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    tags = query("/api/tags")
    matches = [m for m in tags["models"] if m.get("name") == model or m.get("model") == model]
    if len(matches) != 1 or not matches[0].get("digest"):
        raise ValueError(f"Model {model!r} must already be installed; no automatic download")
    return {"model": matches[0], "show": query("/api/show", {"model": model}),
            "ollama": query("/api/version")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--model")
    parser.add_argument("--host", default="http://127.0.0.1:11434")
    parser.add_argument("--metadata", type=Path)
    args = parser.parse_args()
    certified(args.root)
    if args.model:
        if args.metadata is None:
            parser.error("--model requires --metadata")
        metadata = model_metadata(args.host, args.model)
        metadata["slurm_job_id"] = os.environ.get("SLURM_JOB_ID")
        atomic_json(args.metadata, metadata)
        print(metadata["model"]["digest"])
    else:
        print("Preflight and environment diagnostics: OK")


if __name__ == "__main__":
    main()

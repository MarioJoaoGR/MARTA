"""Offline cluster gates and local Ollama metadata; never requests inference."""
import argparse
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

from .protocol import atomic_json


def certified(root, require_loading=False):
    preflight = json.loads((root / "reports/preflight.json").read_text())
    diagnostics = json.loads((root / "reports/environment-diagnostics.json").read_text())
    if not (preflight.get("ready") and preflight.get("runtime_checked")
            and preflight.get("mutation_ready") and diagnostics.get("ready")):
        raise ValueError("XRepoTest preparation and environment diagnostics must both pass")
    if preflight.get("environment") != diagnostics.get("environment"):
        raise ValueError("Diagnostic and preflight environments differ")
    if require_loading:
        from .environment.verify_loading import loading_fingerprint
        from .protocol import DATA_SHA256
        from marta.ruby_backend.loading import LOADING_POLICY
        path = root / "reports/loading-diagnostics.json"
        if not path.is_file():
            raise ValueError("Run production loading diagnostics before allocating model inference")
        loading = json.loads(path.read_text())
        if (not loading.get("ready") or loading.get("dataset") != DATA_SHA256
                or loading.get("policy") != LOADING_POLICY
                or loading.get("loading_code") != loading_fingerprint()
                or loading.get("environment") != preflight.get("environment")
                or len(loading.get("checks", {})) != 302
                or not all(c.get("passed") for c in loading["checks"].values())
                or not loading.get("session_regression", {}).get("passed")):
            raise ValueError("Production loading diagnostics are missing, failed or stale")
        if set(loading.get("projects", {})) != set(preflight.get("projects", {})):
            raise ValueError("Loading certification must cover every project")
        for name, hashes in loading["projects"].items():
            if any(not hashes.get(k) or hashes.get(k) != preflight["projects"][name].get(k)
                   for k in ("source_digest", "runtime_digest")):
                raise ValueError(f"{name}: loading certification belongs to other sources")


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
    parser.add_argument("--require-loading", action="store_true")
    args = parser.parse_args()
    certified(args.root, args.require_loading)
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

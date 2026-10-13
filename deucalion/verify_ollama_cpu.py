"""Load-only CPU verification: no generated answer or benchmark sample."""
import argparse
import json
import os
from pathlib import Path
import re
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from deucalion.xrepotest_official_generate import MODEL_DIGEST, PARAMETERS, atomic


def confirm_threads(server_log, expected):
    matches = re.findall(r"system_info: n_threads =\s*(\d+) \(n_threads_batch =\s*(\d+)\)", server_log.read_text())
    if not matches or any((int(a), int(b)) != (expected, expected) for a, b in matches):
        raise ValueError("CPU runner thread count differs or cannot be verified")
    return expected


def verify(host, model, context, query, expected_threads=None, server_log=None):
    url = urlparse(host)
    if url.scheme != "http" or url.hostname != "127.0.0.1" or url.path:
        raise ValueError("Only the private local Ollama host is permitted")
    if model != PARAMETERS["model"] or context != 32768:
        raise ValueError("CPU model/context must match MARTA")
    version = query("/api/version")
    if version.get("version") != "0.30.7":
        raise ValueError("Ollama version differs from MARTA")
    tags = query("/api/tags")
    matches = [m for m in tags.get("models", []) if m.get("name") == model]
    if len(matches) != 1 or matches[0].get("digest") != MODEL_DIGEST:
        raise ValueError("Pinned model must already be present; no download")
    started = time.monotonic()
    load = query("/api/generate", {"model": model, "prompt": "", "stream": False,
                 "keep_alive": -1, "options": {"num_ctx": context}})
    if (load.get("done_reason") != "load" or load.get("response")
            or load.get("eval_count", 0) != 0):
        raise ValueError("Load-only call unexpectedly generated output")
    ps = query("/api/ps")
    loaded = [m for m in ps.get("models", []) if m.get("name") == model]
    if (len(loaded) != 1 or loaded[0].get("digest") != MODEL_DIGEST
            or loaded[0].get("size_vram") != 0
            or loaded[0].get("context_length") != context):
        raise ValueError("Runner is not a verified CPU-only model at the requested context")
    proof = {"backend": "cpu", "host": host, "model": model,
            "model_digest": MODEL_DIGEST, "ollama_version": version["version"],
            "context_length": context, "size_vram": 0,
            "loaded_model": loaded[0], "load_seconds": time.monotonic() - started,
            "slurm_job_id": os.getenv("SLURM_JOB_ID"),
            "cpu_affinity": sorted(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None,
            "note": "Empty prompt loads only; no benchmark answer generated."}
    if expected_threads is not None:
        if server_log is None:
            raise ValueError("Thread verification requires this server's log")
        proof["cpu_threads"] = confirm_threads(server_log, expected_threads)
        proof["thread_control"] = "LLAMA_ARG_THREADS"
    return proof


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--host", required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--context", type=int, default=32768)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--threads", type=int)
    p.add_argument("--server-log", type=Path)
    a = p.parse_args()
    def query(path, payload=None):
        data = json.dumps(payload).encode() if payload is not None else None
        request = Request(a.host + path, data=data, headers={"Content-Type": "application/json"})
        with urlopen(request, timeout=600 if path == "/api/generate" else 30) as response:
            return json.load(response)
    proof = verify(a.host, a.model, a.context, query, a.threads, a.server_log)
    atomic(a.output, proof)
    print("CPU-only runner verified; VRAM 0, context 32768, pinned weights, no inference sample", flush=True)


if __name__ == "__main__":
    main()

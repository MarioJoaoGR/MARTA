"""Pinned XRepoTest Ruby task contract. No LLM or optional dependencies."""
from __future__ import annotations

import hashlib
import json
import os
from contextlib import contextmanager
from pathlib import Path, PurePosixPath

UPSTREAM_COMMIT = "39fb6ab3173136d3dac2d38ed7c98baf6c470270"
DATA_REVISION = "cd694c00d20951aef189a406abac980a6b1c49d4"
DATA_SHA256 = "811639c4291d3bd14ff58d8b2976bfffbf4df08cbf7d7aab22080c88165747dd"
IMAGE = "dungxg502/xrepotest-ruby@sha256:e7e857ff5c73345a9492a5352a52262da9796a3cb29c5f18053e0be1e8b6924d"
SCHEMA = "marta-xrepotest-v1"


def digest(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def code_fingerprint() -> str:
    root = Path(__file__).resolve().parents[2]
    sources = {str(f.relative_to(root)): f.read_text()
               for folder in (root / "marta/ruby_backend", root / "benchmark/xrepotest")
               for f in folder.rglob("*") if f.is_file() and f.suffix in {".py", ".rb"}}
    for rel in ("marta/gptapi.py", "marta/embedding.py"):
        sources[rel] = (root / rel).read_text()
    return digest(sources)


def atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def load_tasks(path: Path, *, pinned: bool = True) -> list[dict]:
    raw = path.read_bytes()
    if pinned and hashlib.sha256(raw).hexdigest() != DATA_SHA256:
        raise ValueError("Dataset bytes differ from the pinned XRepoTest Ruby release")
    tasks = [json.loads(line) for line in raw.splitlines() if line.strip()]
    ids = [t["task_id"] for t in tasks]
    if any(type(i) is not int for i in ids) or len(set(ids)) != len(ids):
        raise ValueError("Task IDs must be unique integers")
    if pinned and set(ids) != set(range(675)):
        raise ValueError("Expected every official task ID 0..674")
    for t in tasks:
        p = PurePosixPath(t["file_path"])
        if p.is_absolute() or ".." in p.parts or len(p.parts) < 2:
            raise ValueError(f"Unsafe task path: {p}")
        c = t["function_component"]
        if not 1 <= c["start_line"] <= c["end_line"]:
            raise ValueError(f"Invalid one-based source range for task {t['task_id']}")
    return sorted(tasks, key=lambda t: t["task_id"])


def selectors(tasks: list[dict]) -> list[dict]:
    return [{"task_id": t["task_id"], "file": t["file_path"].split("/", 1)[1],
             "name": t["function_name"],
             "start_line": t["function_component"]["start_line"],
             "end_line": t["function_component"]["end_line"]} for t in tasks]


def source_inventory(root: Path, tasks: list[dict]) -> dict:
    """Only production lib trees, including sub-gems; never tests/vendor gems.

    Every focal file must be inside this policy, otherwise fail instead of
    silently dropping tasks. This policy covers this pinned ten-repo corpus.
    """
    blocked = {"vendor", "spec", "test", "tests", "fixtures", "examples", ".git",
               "marta_specs", ".marta_ruby_cache", "templates"}
    # Prune installed dependencies before walking; large vendor trees contain
    # thousands of irrelevant files and must never become prompt context.
    files = []
    for directory, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in {"vendor", ".git", "coverage", "marta_specs", ".marta_ruby_cache"})
        files.extend(Path(directory) / n for n in names)
    code = sorted(p for p in files if p.suffix == ".rb"
                  if "lib" in p.relative_to(root).parts[:-1]
                  and not blocked.intersection(p.relative_to(root).parts[:-1]))
    rels = {p.relative_to(root).as_posix() for p in code}
    mismatches = []
    for t in tasks:
        rel = t["file_path"].split("/", 1)[1]
        p = root / rel
        if rel not in rels or not p.is_file() or p.read_text() != t["file_content"]:
            mismatches.append(t["task_id"])
    if mismatches:
        raise ValueError(f"Sources unavailable, changed, or outside production scope: {mismatches}")
    # README files are also inputs to intent summaries and must invalidate a run.
    readmes = sorted(p for p in files if p.is_file()
                     and p.name.lower().startswith("readme")
                     and not blocked.intersection(p.relative_to(root).parts[:-1]))
    hashes = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in code + readmes}
    runtime_hashes = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in sorted(files) if p.is_file()}
    loads = sorted({str(PurePosixPath(r).parent) for r in rels
                    if PurePosixPath(r).parent.name == "lib"}, key=lambda x: (x.count("/"), x))
    return {"code_files": sorted(rels), "load_paths": loads,
            "input_hashes": hashes, "source_digest": digest(hashes),
            "runtime_digest": digest(runtime_hashes)}


def guard_run(root: Path, config: dict) -> None:
    """Refuse old results or incompatible resumes, even for the same model."""
    manifest = root / "experiment.json"
    expected = {"schema": SCHEMA, **config}
    if manifest.exists():
        if json.loads(manifest.read_text()) != expected:
            raise ValueError("Experiment configuration changed: use a new output directory")
        return
    if root.exists() and any(p.name != "run.lock" for p in root.iterdir()):
        raise ValueError("Output directory is not empty and has no matching XRepoTest manifest")
    atomic_json(manifest, expected)


@contextmanager
def locked_run(root: Path, config: dict):
    import fcntl
    root.mkdir(parents=True, exist_ok=True)
    with (root / "run.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        guard_run(root, config)
        yield


def export_responses(tasks: list[dict], run: Path, output: Path) -> None:
    """One accumulated final suite per task. No-output rows stay in denominator."""
    records = []
    for t in tasks:
        folder = run / "tasks" / str(t["task_id"])
        state_path = folder / "state.json"
        if not state_path.is_file():
            raise ValueError(f"Task {t['task_id']} unfinished; evaluation export refused")
        state = json.loads(state_path.read_text())
        if state.get("status") not in {"complete", "no_tests"}:
            raise ValueError(f"Task {t['task_id']} unfinished or infrastructure failure")
        suite = folder / "final_spec.rb"
        code = suite.read_text() if state["status"] == "complete" and suite.exists() else ""
        if state["status"] == "complete" and not code.strip():
            raise ValueError(f"Completed task {t['task_id']} has no final suite")
        records.append({"task_id": t["task_id"], "response": [code] if code.strip() else []})
    output.parent.mkdir(parents=True, exist_ok=True)
    tmp = output.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
    os.replace(tmp, output)

"""Analysis caching for the Ruby backend (item 8).

Mirrors MARTA's ``compute_source_hash`` + ``save/load_analysis_cache``: the
LLM-derived per-method analysis (done_what / what_todo / summary / judge) is
keyed on an MD5 of the source tree and the model name, so an unchanged project
skips the whole expensive summary phase on a re-run.

Stored under ``<root>/.marta_ruby_cache/analysis_<model>.json``.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from typing import Dict, List, Optional


def compute_source_hash(files: List[str]) -> str:
    """MD5 over the given source files (path + bytes), order-independent."""
    hasher = hashlib.md5()
    for path in sorted(files):
        hasher.update(path.encode())
        try:
            with open(path, "rb") as f:
                hasher.update(f.read())
        except OSError:
            continue
    return hasher.hexdigest()


def cache_path(root_dir: str, model: str) -> str:
    safe = re.sub(r"[^0-9A-Za-z_.-]", "_", model or "default")
    return os.path.join(root_dir, ".marta_ruby_cache", f"analysis_{safe}.json")


def call_graph_path(root_dir: str) -> str:
    return os.path.join(root_dir, ".marta_ruby_cache", "call_graph.json")


def save_call_graph(path: str, source_hash: str, graph_json: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"source_hash": source_hash, "graph": graph_json}, f, indent=2)


def load_call_graph(path: str, source_hash: str) -> Optional[dict]:
    """Return the cached call-graph JSON iff the source hash matches (the model
    is irrelevant — the graph is purely static)."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return None
    return data.get("graph") if data.get("source_hash") == source_hash else None


def save_analysis(path: str, source_hash: str, model: str, targets: Dict[str, dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            {"source_hash": source_hash, "model": model, "targets": targets},
            f, indent=2,
        )


def load_analysis(path: str, source_hash: str, model: str) -> Optional[Dict[str, dict]]:
    """Return the cached per-target analysis iff hash and model match, else None."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return None
    if data.get("source_hash") != source_hash or data.get("model") != model:
        return None
    return data.get("targets", {})

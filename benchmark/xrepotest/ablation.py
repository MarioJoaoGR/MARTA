"""Audited options and selection for component-removal experiments."""
import json
from pathlib import Path

from .protocol import SCHEMA, digest

# The existing v4 run. This compatibility exception allows only exact-prompt
# analysis reuse after compatibility checks; no tests or task states are copied.
FROZEN_NORMAL_CODE = "5f731f30e02f62264900a96b2c7efc5f33d4dfff08cbc33c41dab25eb0720d85"


def select_tasks(tasks, path=None):
    if path is None:
        return tasks, None
    raw = json.loads(Path(path).read_text())
    if (not isinstance(raw, list) or not raw or any(type(t) is not int for t in raw)
            or len(set(raw)) != len(raw)):
        raise ValueError("Task selection must be a nonempty JSON list of unique integer IDs")
    known = {t["task_id"] for t in tasks}
    if not set(raw) <= known:
        raise ValueError("Task selection contains IDs outside the official dataset")
    ids = sorted(raw)
    return [t for t in tasks if t["task_id"] in set(ids)], {
        "task_ids": ids, "digest": digest(ids), "scope": "official-task-subset"}


def verify_analysis_reference(path, config):
    reference = Path(path).resolve()
    previous = json.loads((reference / "experiment.json").read_text())
    if (previous.get("schema") != SCHEMA or previous.get("no_graph") is not False
            or previous.get("ablations")):
        raise ValueError("Analysis reference must be a guarded normal full-context experiment")
    if previous.get("marta_code") not in {config["marta_code"], FROZEN_NORMAL_CODE}:
        raise ValueError("Analysis reference uses an unverified MARTA code version")
    independent = {"marta_code", "no_graph", "rounds", "attempts", "effective_attempts",
                   "ablations", "task_selection", "analysis_reference", "input_hashes", "runtime_hashes"}
    for key, value in config.items():
        if key not in independent and previous.get(key) != value:
            raise ValueError(f"Analysis reference differs in {key}")
    for key in ("input_hashes", "runtime_hashes"):
        for project, value in config[key].items():
            if previous.get(key, {}).get(project) != value:
                raise ValueError(f"Analysis reference differs in {project} {key}")
    return {"source": str(reference), "manifest_digest": digest(previous),
            "source_code": previous["marta_code"],
            "scope": "exact-local-prompts-and-vectors" if config["no_graph"] else "compatible-production-analysis"}

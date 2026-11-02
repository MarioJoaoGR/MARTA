"""Paired round-zero reuse, never importing a reference's final test suite."""
import json
import math
from pathlib import Path

from .protocol import atomic_json, digest
from .reuse import _copy, _hash


def prepare_first_round(reference, output, target, project, recorder, *, expected_manifest):
    """The caller verifies identical round-zero options before entering here.

    A finished source task, completed round timer and coverage event are required
    even when round zero produced no spec. Missing evidence is an error, never
    an invitation to regenerate the baseline's failed round.
    """
    reference, output = Path(reference), Path(output)
    manifest = reference / "experiment.json"
    if digest(json.loads(manifest.read_text())) != expected_manifest:
        raise ValueError("First-round reference manifest changed")
    source = reference / "tasks" / str(target.task_id)
    inputs = [source / name for name in ("state.json", "generation.json", "events.jsonl")]
    before = {str(p.name): _hash(p) for p in inputs}
    state = json.loads(inputs[0].read_text())
    if (state.get("status") not in {"complete", "no_tests"}
            or state.get("task_id") != target.task_id or state.get("project") != project):
        raise ValueError("First-round reference task must be finished and match the official target")
    generation = json.loads(inputs[1].read_text())
    seconds = generation.get("times", {}).get("round_0")
    if (type(seconds) not in (int, float) or not math.isfinite(seconds) or seconds < 0):
        raise ValueError("First-round reference lacks a completed round-zero timer")
    events = [json.loads(line) for line in inputs[2].read_text().splitlines()]
    events = [e for e in events if type(e.get("ronda")) is int and e["ronda"] == 0]
    calls = [e for e in events if e.get("tipo") == "llm"]
    if (not any(e.get("tipo") == "cobertura" for e in events)
            or not {"plano", "dev_primeira"} <= {e.get("fase") for e in calls}
            or any(e.get("task_id") != target.task_id or e.get("project") != project
                   or e.get("metodo") != target.method.qualified_name for e in calls)):
        raise ValueError("First-round reference lacks matching completed generation evidence")
    phases = {}
    for event in calls:
        row = phases.setdefault(event["fase"], {"calls": 0, "input_tokens": 0,
                               "output_tokens": 0, "seconds": 0.0, "truncated": 0, "errors": 0})
        row["calls"] += 1
        row["input_tokens"] += event.get("prompt_tokens", 0)
        row["output_tokens"] += event.get("completion_tokens", 0)
        row["seconds"] += event.get("segundos", 0)
        row["truncated"] += bool(event.get("cortada"))
        row["errors"] += bool(event.get("erro"))
    spec_name = Path(target.spec_path_for_round(0)).name
    specs = list((source / "marta_specs").glob("*_r0_spec.rb"))
    if any(p.name != spec_name for p in specs):
        raise ValueError("First-round spec belongs to a different method/selector")
    spec = source / "marta_specs" / spec_name
    accepted = [e for e in events if e.get("tipo") == "generation_validation"
                and e.get("etapa") == "rspec" and e.get("valid") is True]
    if bool(accepted) != spec.is_file():
        raise ValueError("First-round spec presence contradicts its recorded validation")
    if accepted and spec.read_text() != accepted[-1]["code"] + "\n":
        raise ValueError("First-round spec differs from its recorded accepted code")
    spec_hash = None
    if spec.is_file():
        if not spec.read_text().strip():
            raise ValueError("Cannot reuse an empty first-round spec")
        destination = output / "marta_specs" / spec_name
        if destination.exists():
            raise ValueError("First-round destination must be fresh")
        spec_hash = _copy(spec, destination)
    if any(_hash(p) != before[p.name] for p in inputs):
        raise ValueError("First-round reference changed during reuse")
    audit = {"policy": "paired-first-round-v1", "source": str(source), "task_id": target.task_id,
             "round": 0, "manifest_digest": expected_manifest, "source_hashes": before,
             "spec_name": spec_name if spec_hash else None, "spec_sha256": spec_hash,
             "no_spec": spec_hash is None,
             "usage": {"generation_seconds": seconds, "llm_by_phase": phases},
             "note": "Round zero, including its repair attempts and failures, is shared. Only later rounds are new calls. Slurm billing is separate."}
    audit["reuse_id"] = digest(audit)
    atomic_json(output / "first_round_reuse.json", audit)
    recorder.evento(tipo="generation_round_reused", **audit)
    return audit

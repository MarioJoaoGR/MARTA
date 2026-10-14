"""CPU continuation provenance; never changes generation code or experiment.json."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shlex

from benchmark.xrepotest.protocol import SCHEMA, DATA_SHA256, atomic_json, code_fingerprint, digest
from deucalion.verify_marta_ollama_cpu import MODEL_DIGEST

COHORT = "qwen36_35b_ablation97_no_graph_v1"
ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    "MODEL": "model", "XREPO_THINKING": "thinking",
    "XREPO_MAX_TOKENS": "max_tokens", "XREPO_TEMPERATURE": "temperature",
    "XREPO_TOP_P": "top_p", "XREPO_PRESENCE_PENALTY": "presence_penalty",
    "XREPO_REQUEST_TIMEOUT": "request_timeout", "XREPO_ROUNDS": "rounds",
    "XREPO_ATTEMPTS": "attempts"
}


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(generation):
    d = json.loads((generation / "experiment.json").read_text())
    ids = json.loads((ROOT / "deucalion/selections/xrepotest_ablation97_v1.json").read_text())
    if (d.get("schema") != SCHEMA or d.get("dataset") != DATA_SHA256
            or d.get("marta_code") != code_fingerprint()
            or d.get("model") != "qwen3.6:35b" or d.get("model_digest") != MODEL_DIGEST
            or d.get("thinking") != "on" or d.get("no_graph") is not True
            or d.get("task_selection", {}).get("task_ids") != ids
            or d.get("task_selection", {}).get("digest") != digest(ids)
            or d.get("runtime_env", {}).get("OLLAMA_CTX") != "32768"):
        raise ValueError("CPU resume must match the pinned existing no-graph experiment and its 97 IDs")
    installed = generation.parents[2] / "selections/xrepotest_ablation97_v1.json"
    if json.loads(installed.read_text()) != ids:
        raise ValueError("Installed selection differs from the pinned 97 tasks")
    if (generation / "processed.jsonl").exists():
        raise ValueError("Generation already exported; do not allocate another model job")
    expected = {"max_tokens": 16384, "temperature": 0.6, "top_p": 0.95,
                "presence_penalty": 0, "request_timeout": 1800, "rounds": 3, "attempts": 3}
    if any(d.get(k) != v for k, v in expected.items()):
        raise ValueError("Saved sampling, budget, timeout or rounds differ from the approved experiment")
    if any(d.get("ablations", {}).get(flag, False) for flag in
           ("no_type_hints", "no_method_retrieval", "no_coverage_feedback", "no_repair")):
        raise ValueError("Only the no-graph arm can resume with this launcher")
    if any(k not in {"OLLAMA_CTX", "TRANSFORMER_PATH", "MARTA_MAX_CONTEXT_CHARS"}
           or not isinstance(v, str) for k, v in d["runtime_env"].items()):
        raise ValueError("Unexpected saved runtime environment")
    return d, ids


def environment(d):
    env = {k: str(d[field]) for k, field in FIELDS.items()}
    env.update(d["runtime_env"])
    env["XREPO_NO_GRAPH"] = "1"
    env["XREPO_TASK_IDS"] = "/data/xrepo/selections/xrepotest_ablation97_v1.json"
    for flag in ("NO_TYPE_HINTS", "NO_METHOD_RETRIEVAL", "NO_COVERAGE_FEEDBACK", "NO_REPAIR"):
        env["XREPO_" + flag] = "0"
    for key, field in (("XREPO_REUSE_ANALYSIS_FROM", "analysis_reference"),
                       ("XREPO_REUSE_FIRST_ROUND_FROM", "first_round_reference")):
        env[key] = d.get(field, {}).get("source", "")
    return env


def snapshot(generation, ids):
    states, preserved, events = {}, {}, {}
    for tid in ids:
        folder = generation / "tasks" / str(tid)
        p = folder / "state.json"
        if not p.exists():
            states[str(tid)] = "not_started"
            continue
        s = json.loads(p.read_text()).get("status")
        if s not in {"complete", "no_tests", "running"}:
            raise ValueError("Unexpected task status: " + str(tid))
        states[str(tid)] = s
        if s in {"complete", "no_tests"}:
            if s == "complete" and not (folder / "final_spec.rb").read_text().strip():
                raise ValueError("Completed task has no final suite: " + str(tid))
            for f in folder.rglob("*"):
                if f.is_file():
                    preserved[str(f.relative_to(generation))] = sha(f)
    for p in generation.rglob("events.jsonl"):
        events[str(p.relative_to(generation))] = {"bytes": p.stat().st_size, "sha256": sha(p)}
    return {"task_states": states, "terminal_file_hashes": preserved, "event_files": events}


def start(generation, audit, proof, job_id):
    d, ids = validate(generation)
    if audit.exists():
        raise ValueError("A CPU audit already exists for this Slurm job")
    if (proof.get("backend") != "cpu" or proof.get("cpu_threads") != 8
            or proof.get("size_vram") != 0 or proof.get("context_length") != 32768
            or proof.get("model_digest") != d["model_digest"]
            or proof.get("ollama_version") != "0.30.7" or proof.get("slurm_job_id") != job_id):
        raise ValueError("CPU proof does not belong to this pinned runner/job")
    record = {"policy": "same-experiment-cpu-continuation-v1", "job_id": job_id,
              "started_at": now(), "backend": "cpu", "cpu_proof": proof,
              "experiment_sha256": sha(generation / "experiment.json"),
              "generation_code": d["marta_code"], "before": snapshot(generation, ids),
              "note": "Earlier results are retained. Tasks unfinished at this boundary may mix GPU and CPU work; backend timings are not directly comparable."}
    atomic_json(audit, record)
    return record


def finish(generation, audit, exit_code):
    record = json.loads(audit.read_text())
    if sha(generation / "experiment.json") != record["experiment_sha256"]:
        raise ValueError("Experiment manifest changed during CPU continuation")
    for rel, expected in record["before"]["terminal_file_hashes"].items():
        if sha(generation / rel) != expected:
            raise ValueError("Previously terminal task was modified: " + rel)
    ids = [int(t) for t in record["before"]["task_states"]]
    after = snapshot(generation, ids)
    completed = [int(t) for t, s in after["task_states"].items()
                 if s in {"complete", "no_tests"}
                 and record["before"]["task_states"][t] not in {"complete", "no_tests"}]
    if exit_code == 0:
        rows = [json.loads(line) for line in (generation / "processed.jsonl").read_text().splitlines() if line.strip()]
        if len(rows) != len(ids) or {r["task_id"] for r in rows} != set(ids):
            raise ValueError("Generator returned without the complete 97-task export")
    record.update(finished_at=now(), exit_code=exit_code, after=after,
                  tasks_finished_in_cpu_job=completed, prior_terminal_files_preserved=True)
    atomic_json(audit, record)
    return record


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("stage", choices=("env", "start", "finish"))
    p.add_argument("--generation", type=Path, required=True)
    p.add_argument("--job-id", required=True)
    p.add_argument("--env-file", type=Path)
    p.add_argument("--proof", type=Path)
    p.add_argument("--exit-code", type=int)
    a = p.parse_args()
    if a.generation.parent.name != COHORT:
        p.error("This continuation is scoped to the existing no-graph cohort")
    audit = a.generation.parent / "metadata" / ("cpu_resume_" + a.job_id + ".json")
    with (a.generation / "run.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if a.stage == "env":
            if a.env_file is None:
                p.error("--env-file required")
            d, ids = validate(a.generation)
            a.env_file.write_text("".join("export " + k + "=" + shlex.quote(v) + "\n"
                                         for k, v in environment(d).items()))
            states = snapshot(a.generation, ids)["task_states"]
            print("Saved parameters restored; task states:", dict(Counter(states.values())))
        elif a.stage == "start":
            if a.proof is None:
                p.error("--proof required")
            start(a.generation, audit, json.loads(a.proof.read_text()), a.job_id)
            print("CPU boundary audited; original experiment unchanged")
        else:
            if a.exit_code is None:
                p.error("--exit-code required")
            record = finish(a.generation, audit, a.exit_code)
            print("CPU job audited; prior terminal files preserved; newly finished:",
                  len(record["tasks_finished_in_cpu_job"]))


if __name__ == "__main__":
    main()

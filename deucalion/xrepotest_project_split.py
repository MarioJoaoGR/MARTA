"""Project-only scheduling around the frozen MARTA runner; no prompt changes."""
import argparse
from contextlib import contextmanager
from copy import deepcopy
import fcntl
import json
import os
from pathlib import Path
import shlex
import shutil
import uuid

from benchmark.xrepotest.protocol import SCHEMA, atomic_json, digest, load_tasks
from deucalion import xrepotest_cpu_resume as cpu

POLICY = "no-graph-project-partition-v1"
GROUPS = json.loads((Path(__file__).parent / "selections/xrepotest_ablation97_projects_v1.json").read_text())
TERMINAL = {"complete", "no_tests"}


def child_name(project):
    if project not in GROUPS:
        raise ValueError("Unknown project")
    return cpu.COHORT + "_cpu_" + project.replace("-", "_")


def marker(parent):
    return parent / "metadata/project_split.json"


def project_config(original, project, ids):
    config = deepcopy(original)
    config["task_selection"] = {"task_ids": ids, "digest": digest(ids), "scope": "official-task-subset"}
    for field in ("input_hashes", "runtime_hashes"):
        config[field] = {project: original[field][project]}
    return config


def state(generation, tid):
    path = generation / "tasks" / str(tid) / "state.json"
    if not path.exists():
        return "not_started"
    record = json.loads(path.read_text())
    if record.get("task_id") != tid or record.get("status") not in TERMINAL | {"running"}:
        raise ValueError("Invalid task state: " + str(path))
    if record["status"] == "complete":
        suite = path.parent / "final_spec.rb"
        if not suite.is_file() or not suite.read_text().strip():
            raise ValueError("Completed task has no final suite")
    return record["status"]


def plan(parent, tasks):
    original, ids = cpu.validate(parent / "generation")
    actual = {}
    for t in tasks:
        if t["task_id"] in ids:
            actual.setdefault(t["file_path"].split("/", 1)[0], []).append(t["task_id"])
    actual = {p: sorted(v) for p, v in actual.items()}
    if actual != GROUPS or set(ids) != {i for v in actual.values() for i in v}:
        raise ValueError("Pinned project partition differs from the official 97 tasks")
    if len(ids) != sum(len(v) for v in actual.values()) or set(original["input_hashes"]) != set(actual):
        raise ValueError("Duplicate task allocation or missing project context")
    result = {"policy": POLICY, "parent": str(parent), "created_at": cpu.now(),
              "parent_experiment": original, "projects": {}}
    for p, tids in sorted(actual.items()):
        statuses = {str(i): state(parent / "generation", i) for i in tids}
        result["projects"][p] = {"task_ids": tids, "states": statuses,
            "pending": sum(s not in TERMINAL for s in statuses.values()),
            "run": child_name(p), "config": project_config(original, p, tids)}
    result["pending"] = sum(v["pending"] for v in result["projects"].values())
    result["worker_projects"] = [p for p, v in result["projects"].items() if v["pending"]]
    return result


def files(root):
    out = {}
    for p in sorted(root.rglob("*")):
        if p.is_symlink():
            raise ValueError("Symlinks are not allowed in project checkpoints: " + str(p))
        if p.is_file() and p.name != "run.lock":
            out[p.relative_to(root).as_posix()] = cpu.sha(p)
    return out


def verify_files(root, expected, exact=False):
    if exact:
        if files(root) != expected:
            raise ValueError("Frozen checkpoint tree changed: " + str(root))
    elif any(not (root / rel).is_file() or cpu.sha(root / rel) != h for rel, h in expected.items()):
        raise ValueError("Preserved checkpoint changed: " + str(root))


@contextmanager
def frozen_lock(parent):
    with (parent / "generation-job.lock").open("a") as job, (parent / "generation/run.lock").open("a") as run:
        fcntl.flock(job, fcntl.LOCK_EX | fcntl.LOCK_NB)
        fcntl.flock(run, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield


def verify_validation(parent, certificate):
    original, _ = cpu.validate(parent / "generation")
    checks = certificate.get("checks", {})
    if (certificate.get("ready") is not True or certificate.get("policy") != POLICY
            or certificate.get("tasks") != 97 or certificate.get("code_fingerprint") != cpu.code_fingerprint()
            or certificate.get("parent_manifest_digest") != digest(original)
            or set(checks) != set(GROUPS)
            or any(checks[p] != {"project": p, "exact_config_match": True,
                "config_digest": digest(project_config(original, p, GROUPS[p]))} for p in GROUPS)):
        raise ValueError("A successful ten-project validation for this exact frozen experiment is required")


def prepare(parent, tasks):
    # Must only be called AFTER the serial job has stopped and released both locks.
    with frozen_lock(parent):
        if marker(parent).exists():
            record = json.loads(marker(parent).read_text())
            verify_files(parent / "generation", record["frozen_files"], exact=True)
            return record
        record = plan(parent, tasks)
        if not record["pending"]:
            raise ValueError("All tasks already terminal; export serially instead")
        record["frozen_files"] = files(parent / "generation")
        record["frozen_at"] = cpu.now()
        stage = parent / "project_parallel" / ("staging_" + uuid.uuid4().hex)
        stage.mkdir(parents=True)
        # Publish children only after each copied tree has a checked seed and manifest.
        for project in record["worker_projects"]:
            item = record["projects"][project]
            destination = parent.parent / item["run"]
            if destination.exists():
                raise ValueError("Child directory already exists; refusing to overwrite " + str(destination))
            child = stage / item["run"]
            gen = child / "generation"
            gen.mkdir(parents=True)
            for rel in ["analysis/" + project] + [prefix + "/" + str(tid)
                    for prefix in ("tasks", "interrupted_tasks") for tid in item["task_ids"]]:
                source = parent / "generation" / rel
                if source.exists():
                    target = gen / rel
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copytree(source, target)
            atomic_json(gen / "experiment.json", item["config"])
            atomic_json(child / "selection.json", item["task_ids"])
            (child / "metadata").mkdir()
            item["seed_files"] = files(gen)
            item["seed_event_files"] = {p.relative_to(gen).as_posix(): {
                "sha256": cpu.sha(p), "bytes": p.stat().st_size} for p in gen.rglob("events.jsonl")}
            copied = {rel: h for rel, h in item["seed_files"].items() if rel != "experiment.json"}
            if any(record["frozen_files"].get(rel) != h for rel, h in copied.items()):
                raise ValueError("Copied project bytes differ from the frozen parent")
            provenance = {"policy": POLICY, "parent": str(parent), "project": project,
                          "parent_manifest_digest": digest(record["parent_experiment"]),
                          "seed_files": item["seed_files"]}
            atomic_json(child / "metadata/project_seed.json", provenance)
        verify_files(parent / "generation", record["frozen_files"], exact=True)
        # A failed preparation is left intact for inspection, never silently overwritten.
        for project in record["worker_projects"]:
            item = record["projects"][project]
            child = stage / item["run"]
            verify_files(child / "generation", item["seed_files"], exact=True)
            child.rename(parent.parent / item["run"])
        stage.rmdir()
        atomic_json(marker(parent), record)
        return record


def worker(parent, project):
    record = json.loads(marker(parent).read_text())
    if record.get("policy") != POLICY or project not in record["worker_projects"]:
        raise ValueError("Project is not an active partition")
    item = record["projects"][project]
    gen = parent.parent / item["run"] / "generation"
    if json.loads((gen / "experiment.json").read_text()) != item["config"]:
        raise ValueError("Project manifest changed")
    verify_files(parent / "generation", record["frozen_files"], exact=True)
    if cpu.code_fingerprint() != item["config"]["marta_code"]:
        raise ValueError("Generation code changed")
    selection = gen.parent / "selection.json"
    if json.loads(selection.read_text()) != item["task_ids"]:
        raise ValueError("Project selection changed")
    return record, item, gen


def check_config(original, project, candidate):
    expected = project_config(original, project, GROUPS[project])
    candidate = {"schema": SCHEMA, **candidate}
    if candidate != expected:
        differing = sorted(k for k in set(candidate) | set(expected) if candidate.get(k) != expected.get(k))
        raise ValueError("Frozen runner disagrees with partition config: " + str(differing))
    return {"project": project, "exact_config_match": True, "config_digest": digest(expected)}


def write_env(config, selection_path, env_path):
    env = cpu.environment(config)
    env["XREPO_TASK_IDS"] = str(selection_path)
    env_path.write_text("".join("export " + k + "=" + shlex.quote(v) + "\n" for k, v in env.items()))


def worker_start(parent, project, proof, job_id):
    record, item, gen = worker(parent, project)
    if (gen / "processed.jsonl").exists():
        raise ValueError("Project already exported")
    if (proof.get("backend") != "cpu" or proof.get("cpu_threads") != 8
            or proof.get("size_vram") != 0 or proof.get("context_length") != 32768
            or proof.get("model_digest") != item["config"]["model_digest"]
            or proof.get("ollama_version") != "0.30.7" or proof.get("slurm_job_id") != job_id):
        raise ValueError("CPU proof does not match this worker")
    audit = gen.parent / "metadata" / ("cpu_resume_" + job_id + ".json")
    if audit.exists():
        raise ValueError("CPU job audit already exists")
    terminal = cpu.snapshot(gen, item["task_ids"])
    for tid, s in item["states"].items():
        if s in TERMINAL:
            prefix = "tasks/" + tid + "/"
            verify_files(gen, {p: h for p, h in item["seed_files"].items() if p.startswith(prefix)})
    atomic_json(audit, {"policy": POLICY, "backend": "cpu", "project": project,
        "job_id": job_id, "started_at": cpu.now(), "cpu_proof": proof,
        "generation_code": item["config"]["marta_code"], "before": terminal,
        "experiment_sha256": cpu.sha(gen / "experiment.json")})


def worker_finish(parent, project, job_id, exit_code):
    record, item, gen = worker(parent, project)
    audit = gen.parent / "metadata" / ("cpu_resume_" + job_id + ".json")
    return cpu.finish(gen, audit, exit_code)


def merge(parent, tasks):
    with frozen_lock(parent):
        record = json.loads(marker(parent).read_text())
        verify_files(parent / "generation", record["frozen_files"], exact=True)
        output = parent / "project_parallel/merged"
        output.mkdir(parents=True, exist_ok=True)
        with (output / "run.lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            rows, sources = {}, {}
            # Gather and verify everything before publishing a merged export.
            for project, item in record["projects"].items():
                selected = [t for t in tasks if t["task_id"] in item["task_ids"]]
                if project in record["worker_projects"]:
                    _, _, gen = worker(parent, project)
                    path = gen / "processed.jsonl"
                    if not path.is_file():
                        raise ValueError("Project not finished: " + project)
                    data = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
                    if len(data) != len(selected) or {r["task_id"] for r in data} != set(item["task_ids"]):
                        raise ValueError("Duplicate/missing/foreign project task IDs")
                else:
                    gen = parent / "generation"
                    data = []
                expected = []
                for task in selected:
                    tid = task["task_id"]
                    status = state(gen, tid)
                    if status not in TERMINAL:
                        raise ValueError("Task unfinished: " + str(tid))
                    suite = gen / "tasks" / str(tid) / "final_spec.rb"
                    response = [suite.read_text()] if status == "complete" else []
                    if project in record["worker_projects"] and item["states"][str(tid)] in TERMINAL:
                        prefix = "tasks/" + str(tid) + "/"
                        verify_files(gen, {p: h for p, h in item["seed_files"].items() if p.startswith(prefix)})
                    expected.append({"task_id": tid, "response": response})
                if data and sorted(data, key=lambda r: r["task_id"]) != expected:
                    raise ValueError("Project export does not match saved final suites")
                sources[project] = {"generation": str(gen), "files": files(gen)}
                for row in expected:
                    if row["task_id"] in rows:
                        raise ValueError("Duplicated task in merge")
                    rows[row["task_id"]] = row
            ids = record["parent_experiment"]["task_selection"]["task_ids"]
            if sorted(rows) != ids or len(rows) != 97:
                raise ValueError("Final denominator must be the original 97 IDs")
            text = "".join(json.dumps(rows[i], ensure_ascii=False) + "\n" for i in ids)
            existing = output / "processed.jsonl"
            if existing.exists() and existing.read_text() != text:
                raise ValueError("Refusing to replace a different merged result")
            atomic_json(output / "experiment.json", record["parent_experiment"])
            atomic_json(output / "merge_audit.json", {"policy": POLICY, "merged_at": cpu.now(),
                "tasks": ids, "sources": sources, "parent_manifest": record["parent_experiment"],
                "note": "Copied historical events occur in both parent and children. Count parent cost once; only child events after the seed boundary are new. Do not sum all recursive logs."})
            tmp = output / "processed.jsonl.tmp"
            tmp.write_text(text)
            os.replace(tmp, existing)
            return {"tasks": len(rows), "output": str(existing)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("stage", choices=("plan", "prepare", "env", "start", "finish", "merge", "check-config", "validation-env", "certify"))
    p.add_argument("--parent", type=Path)
    p.add_argument("--generation", type=Path)
    p.add_argument("--dataset", type=Path, default=Path("/app/xrepotest/ruby_functions.jsonl"))
    p.add_argument("--project", choices=sorted(GROUPS))
    p.add_argument("--job-id")
    p.add_argument("--env-file", type=Path)
    p.add_argument("--proof", type=Path)
    p.add_argument("--exit-code", type=int)
    p.add_argument("--report", type=Path)
    p.add_argument("--candidate", type=Path)
    p.add_argument("--selection", type=Path)
    p.add_argument("--checks-dir", type=Path)
    p.add_argument("--validation", type=Path)
    a = p.parse_args()
    parent = a.parent or Path("/data/xrepo/runs") / cpu.COHORT
    if parent.name != cpu.COHORT:
        p.error("Only the fixed original cohort is supported")
    if a.stage in {"plan", "prepare", "merge", "check-config", "certify"}:
        tasks = load_tasks(a.dataset)
        if a.stage == "plan":
            result = plan(parent, tasks)
        elif a.stage == "prepare":
            if a.validation is None:
                p.error("--validation from the completed offline validation job is required")
            verify_validation(parent, json.loads(a.validation.read_text()))
            result = prepare(parent, tasks)
        elif a.stage == "merge":
            result = merge(parent, tasks)
        elif a.stage == "check-config":
            original, _ = cpu.validate(parent / "generation")
            result = check_config(original, a.project, json.loads(a.candidate.read_text()))
        else:
            live = plan(parent, tasks)
            checks = {project: check_config(live["parent_experiment"], project,
                        json.loads((a.checks_dir / ("config_" + project + ".json")).read_text()))
                      for project in GROUPS}
            result = {"ready": True, "policy": POLICY, "checked_at": cpu.now(),
                "parent_manifest_digest": digest(live["parent_experiment"]),
                "code_fingerprint": cpu.code_fingerprint(), "tasks": 97,
                "checks": checks, "provisional_pending": live["pending"],
                "note": "Offline validation only; source remains live. Preparation must acquire both source locks after the serial job stops."}
        if a.report:
            atomic_json(a.report, result)
        print(json.dumps(result if a.stage in {"merge", "check-config", "certify"} else {
            "policy": POLICY, "pending": result["pending"], "projects": {
                k: {"tasks": len(v["task_ids"]), "pending": v["pending"]}
                for k, v in result["projects"].items()}, "worker_projects": result["worker_projects"]}, indent=2))
        return
    if a.project is None or a.env_file is None and a.stage == "env":
        p.error("Project and env-file are required")
    if a.stage == "validation-env":
        d, _ = cpu.validate(parent / "generation")
        if a.selection is None:
            p.error("--selection required for offline validation")
        atomic_json(a.selection, GROUPS[a.project])
        write_env(project_config(d, a.project, GROUPS[a.project]), a.selection, a.env_file)
        return
    record, item, gen = worker(parent, a.project)
    if a.generation is not None and a.generation != gen:
        p.error("Worker generation path differs from the registered project")
    with (gen / "run.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        if a.stage == "env":
            if (gen / "processed.jsonl").exists():
                raise ValueError("Project already exported")
            write_env(item["config"], gen.parent / "selection.json", a.env_file)
        elif a.stage == "start":
            worker_start(parent, a.project, json.loads(a.proof.read_text()), a.job_id)
        else:
            result = worker_finish(parent, a.project, a.job_id, a.exit_code)
            print("Project audit finished:", a.project, result["exit_code"])


if __name__ == "__main__":
    main()

"""Submit each prepared project once. Host Python 3.6; no third-party packages."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import subprocess

COHORT = "qwen36_35b_ablation97_no_graph_v1"


def atomic(path, data):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n")
    os.replace(str(tmp), str(path))


def submit(parent, code, run_command=subprocess.check_output):
    record = json.loads((parent / "metadata/project_split.json").read_text())
    groups = json.loads((code / "deucalion/selections/xrepotest_ablation97_projects_v1.json").read_text())
    if (parent.name != COHORT or record.get("policy") != "no-graph-project-partition-v1"
            or not record.get("worker_projects") or set(record["projects"]) != set(groups)):
        raise ValueError("Invalid prepared project partition")
    for project in record["worker_projects"]:
        item = record["projects"][project]
        expected = COHORT + "_cpu_" + project.replace("-", "_")
        if (item["run"] != expected or item["task_ids"] != groups[project]
                or json.loads((parent.parent / expected / "generation/experiment.json").read_text()) != item["config"]):
            raise ValueError("Child differs from the validated partition")
    ledger = parent / "metadata/project_jobs.json"
    # Shared account: protect the submission ledger from concurrent invocations.
    with (parent / "metadata/project_submission.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        jobs = json.loads(ledger.read_text()) if ledger.exists() else {}
        for project in record["worker_projects"]:
            item = record["projects"][project]
            if (parent.parent / item["run"] / "generation/processed.jsonl").exists():
                print(project + ": already exported; no new generation")
                continue
            if project in jobs:
                print(project + ": already submitted as " + jobs[project])
                continue
            env = dict(os.environ, MARTA_CLUSTER_BASE=str(parent.parents[2]),
                MARTA_CLUSTER_CODE=str(code), XREPO_RUN=item["run"],
                XREPO_PROJECT_SHARD=project, XREPO_CPU_CHAIN="1")
            output = run_command(["sbatch", "--parsable", "--export=ALL",
                "--time=48:00:00", "--job-name=abl_" + project,
                str(code / "deucalion/run_xrepotest_generate_cpu.sh")],
                env=env, universal_newlines=True).strip()
            job = output.split(";", 1)[0]
            if not job.isdigit():
                raise RuntimeError("Unexpected sbatch response: " + output)
            jobs[project] = job
            atomic(ledger, jobs)  # retain successful submissions even if a later sbatch fails
            print(project + ": " + job, flush=True)
        return jobs


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parent", type=Path, required=True)
    p.add_argument("--code", type=Path, required=True)
    a = p.parse_args()
    jobs = submit(a.parent, a.code)
    if jobs:
        subprocess.call(["squeue", "-j", ",".join(jobs.values())])


if __name__ == "__main__":
    main()

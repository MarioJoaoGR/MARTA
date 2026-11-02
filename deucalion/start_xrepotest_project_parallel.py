"""Queue CPU preparation, then stop only the named serial job. Host Python 3.6."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess

COHORT = "qwen36_35b_ablation97_no_graph_v1"


def launch(base, code, validation_job, serial_job, command=subprocess.check_output, cancel=subprocess.check_call):
    parent = base / "xrepotest/runs" / COHORT
    generation = parent / "generation"
    certificate_path = base / "xrepotest/reports" / ("project_split_" + validation_job) / "validation.json"
    certificate = json.loads(certificate_path.read_text())
    manifest = json.loads((generation / "experiment.json").read_text())
    def digest(value):
        return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    identity = digest(manifest)
    groups = json.loads((code / "deucalion/selections/xrepotest_ablation97_projects_v1.json").read_text())
    expected_checks = {}
    for project, ids in groups.items():
        config = dict(manifest, task_selection={"task_ids": ids, "digest": digest(ids), "scope": "official-task-subset"},
            input_hashes={project: manifest["input_hashes"][project]},
            runtime_hashes={project: manifest["runtime_hashes"][project]})
        expected_checks[project] = {"project": project, "exact_config_match": True, "config_digest": digest(config)}
    if (certificate.get("ready") is not True or certificate.get("tasks") != 97
            or certificate.get("parent_manifest_digest") != identity
            or certificate.get("code_fingerprint") != manifest.get("marta_code")
            or certificate.get("policy") != "no-graph-project-partition-v1"
            or certificate.get("checks") != expected_checks):
        raise ValueError("Successful validation does not match the current experiment")
    if (generation / "processed.jsonl").exists():
        raise ValueError("Serial generation is already complete; evaluate it instead")
    if (parent / "metadata/project_split.json").exists():
        raise ValueError("Project split already prepared; inspect existing workers")
    active = set(command(["squeue", "-h", "-u", os.environ["USER"], "-o", "%i"],
                         universal_newlines=True).split())
    if serial_job in active:
        audit = json.loads((parent / "metadata" / ("cpu_resume_" + serial_job + ".json")).read_text())
        if audit.get("job_id") != serial_job:
            raise ValueError("Serial job does not belong to this cohort")
    env = dict(os.environ, MARTA_CLUSTER_BASE=str(base), MARTA_CLUSTER_CODE=str(code),
        XREPO_SPLIT_VALIDATION="/data/xrepo/reports/project_split_" + validation_job + "/validation.json")
    args = ["sbatch", "--parsable", "--export=ALL"]
    if serial_job in active:
        args.append("--dependency=afterany:" + serial_job)
    args.append(str(code / "deucalion/run_xrepotest_project_split_prepare_cpu.sh"))
    prep = command(args, env=env, universal_newlines=True).strip().split(";", 1)[0]
    if not prep.isdigit():
        raise RuntimeError("Unexpected preparation job ID")
    print("Preparação e arranque dos projetos CPU: " + prep, flush=True)
    print("Log: " + str(code / "logs" / ("xrepo_split_prepare_" + prep + ".out")), flush=True)
    if serial_job in active:
        # TERM runs the existing cleanup/audit trap and does not trigger continuation.
        # Preparation waits for the whole allocation to end, including child processes.
        cancel(["scancel", "--batch", "--signal=TERM", serial_job])
        print("Paragem da execução sequencial solicitada: " + serial_job, flush=True)
    else:
        print("O job sequencial indicado já não está ativo; a preparação verificará os locks.", flush=True)
    return prep


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--validation-job", required=True)
    p.add_argument("--serial-job", required=True)
    p.add_argument("--base", type=Path, default=Path("/projects/F202407648IACDCF2/mario"))
    p.add_argument("--code", type=Path, default=Path(__file__).resolve().parents[1])
    a = p.parse_args()
    if not a.validation_job.isdigit() or not a.serial_job.isdigit():
        p.error("Slurm job IDs must be numeric")
    launch(a.base, a.code, a.validation_job, a.serial_job)


if __name__ == "__main__":
    main()

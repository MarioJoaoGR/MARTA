import ast
import json
from pathlib import Path
import subprocess

import pytest

from benchmark.xrepotest.protocol import digest
from deucalion import start_xrepotest_project_parallel as starter
from deucalion import submit_xrepotest_project_workers as submitter
from deucalion import xrepotest_project_split as split
from deucalion.tests.test_xrepotest_project_split import prepared_source, saved

CODE = Path(__file__).resolve().parents[2]


def certificate(parent):
    manifest = json.loads((parent / "generation/experiment.json").read_text())
    path = parent.parents[1] / "reports/project_split_2061566/validation.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"ready": True, "tasks": 97,
        "parent_manifest_digest": digest(manifest), "code_fingerprint": manifest["marta_code"],
        "policy": split.POLICY,
        "checks": {p: split.check_config(manifest, p, split.project_config(manifest, p, ids))
                   for p, ids in split.GROUPS.items()}}))
    return path


def test_starter_queues_dependency_before_stopping_only_the_recorded_serial_job(prepared_source):
    parent, _, tasks = prepared_source
    certificate(parent)
    (parent / "metadata/cpu_resume_2039852.json").write_text('{"job_id":"2039852"}')
    calls = []
    def command(args, **kwargs):
        calls.append((args, kwargs))
        return "2039852\n2029390\n" if args[0] == "squeue" else "2070001\n"
    def cancel(args):
        calls.append((args, {}))
    job = starter.launch(parent.parents[2], CODE, "2061566", "2039852", command, cancel)
    assert job == "2070001"
    assert calls[1][0][0] == "sbatch" and "--dependency=afterany:2039852" in calls[1][0]
    assert calls[1][1]["env"]["XREPO_SPLIT_VALIDATION"] == "/data/xrepo/reports/project_split_2061566/validation.json"
    assert calls[2][0] == ["scancel", "--batch", "--signal=TERM", "2039852"]


@pytest.mark.parametrize("case", ["invalid-certificate", "submission-fails", "already-exported"])
def test_starter_does_not_stop_generation_when_validation_or_submission_fails(prepared_source, case):
    parent, _, tasks = prepared_source
    path = certificate(parent)
    if case == "invalid-certificate":
        path.write_text('{"ready":false}')
    elif case == "already-exported":
        (parent / "generation/processed.jsonl").write_text("finished")
    (parent / "metadata/cpu_resume_2039852.json").write_text('{"job_id":"2039852"}')
    def command(args, **kwargs):
        if args[0] == "squeue":
            return "2039852\n"
        raise subprocess.CalledProcessError(1, args)
    with pytest.raises((ValueError, subprocess.CalledProcessError)):
        starter.launch(parent.parents[2], CODE, "2061566", "2039852", command,
            lambda args: pytest.fail("Serial job must keep running"))


def test_starter_handles_a_serial_job_that_has_already_ended(prepared_source):
    parent, _, tasks = prepared_source
    certificate(parent)
    calls = []
    def command(args, **kwargs):
        calls.append(args)
        return "2029390\n" if args[0] == "squeue" else "2070001\n"
    starter.launch(parent.parents[2], CODE, "2061566", "2039852", command,
        lambda args: pytest.fail("Must not cancel another job"))
    assert not any(a.startswith("--dependency") for a in calls[-1])


def test_submission_is_project_specific_idempotent_and_preserves_all_checkpoints(prepared_source):
    parent, _, tasks = prepared_source
    record = split.prepare(parent, tasks)
    before = split.files(parent / "generation")
    calls = []
    def command(args, **kwargs):
        calls.append((args, kwargs))
        return str(2071000 + len(calls)) + "\n"
    jobs = submitter.submit(parent, CODE, command)
    assert len(jobs) == 6 and set(jobs) == set(record["worker_projects"])
    for args, kwargs in calls:
        env = kwargs["env"]
        p = env["XREPO_PROJECT_SHARD"]
        assert env["XREPO_RUN"] == record["projects"][p]["run"]
        assert env["XREPO_CPU_CHAIN"] == "1"
        assert env["MARTA_CLUSTER_BASE"] == str(parent.parents[2])
        assert args[-1] == str(CODE / "deucalion/run_xrepotest_generate_cpu.sh")
        assert "--time=48:00:00" in args
    submitter.submit(parent, CODE, lambda *a, **kw: pytest.fail("Duplicate submission"))
    assert before == split.files(parent / "generation")


def test_partial_submission_keeps_recorded_ids_and_only_submits_missing_projects_on_retry(prepared_source):
    parent, _, tasks = prepared_source
    split.prepare(parent, tasks)
    count = []
    def command(args, **kwargs):
        count.append(kwargs["env"]["XREPO_PROJECT_SHARD"])
        if len(count) == 3:
            raise subprocess.CalledProcessError(1, args)
        return str(2071000 + len(count))
    with pytest.raises(subprocess.CalledProcessError):
        submitter.submit(parent, CODE, command)
    ledger = json.loads((parent / "metadata/project_jobs.json").read_text())
    assert len(ledger) == 2
    retried = []
    def retry(args, **kwargs):
        retried.append(kwargs["env"]["XREPO_PROJECT_SHARD"])
        return str(2072000 + len(retried))
    jobs = submitter.submit(parent, CODE, retry)
    assert len(jobs) == 6 and len(retried) == 4
    assert not set(retried) & set(ledger)


def test_host_entrypoints_have_python36_compatible_syntax():
    for name in ("start_xrepotest_project_parallel.py", "submit_xrepotest_project_workers.py"):
        ast.parse((CODE / "deucalion" / name).read_text(), feature_version=(3, 6))

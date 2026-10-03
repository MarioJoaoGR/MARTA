"""Cluster option forwarding with fake Slurm and no model/container calls."""
import json
import subprocess

import pytest
from benchmark.xrepotest.tests.test_cluster import fake_cluster


def test_normal_job_keeps_three_rounds_three_attempts_and_no_ablation_flags(fake_cluster):
    root, tmp, env = fake_cluster
    result = subprocess.run(["bash", str(root/"deucalion/run_xrepotest_generate_gpu.sh")],
                            env=env, capture_output=True, text=True, timeout=20)
    assert result.returncode == 0, result.stderr
    calls = [json.loads(line) for line in (tmp/"calls.jsonl").read_text().splitlines()]
    invocation = next(c for c in calls if "benchmark.xrepotest.run" in c)
    assert invocation[invocation.index("--rounds")+1] == "3"
    assert invocation[invocation.index("--attempts")+1] == "3"
    assert not any(arg in invocation for arg in (
        "--no-type-hints", "--no-method-retrieval", "--no-coverage-feedback", "--no-repair", "--task-ids"))


def test_cluster_forwards_explicit_modes_and_the_same_subset_to_evaluation(fake_cluster):
    root, tmp, env = fake_cluster
    selection = tmp/"xrepotest/selections/ids.json"
    selection.parent.mkdir(parents=True)
    selection.write_text("[0,155]")
    env.update(XREPO_NO_TYPE_HINTS="1", XREPO_NO_METHOD_RETRIEVAL="1",
               XREPO_NO_COVERAGE_FEEDBACK="1", XREPO_NO_REPAIR="1",
               XREPO_TASK_IDS="/data/xrepo/selections/ids.json",
               XREPO_REUSE_ANALYSIS_FROM="/data/xrepo/runs/reference/generation")
    generate = subprocess.run(["bash", str(root/"deucalion/run_xrepotest_generate_gpu.sh")],
                              env=env, capture_output=True, text=True, timeout=20)
    assert generate.returncode == 0, generate.stderr
    export = tmp/"xrepotest/runs/new-experiment/generation/processed.jsonl"
    export.parent.mkdir(parents=True, exist_ok=True)
    export.write_text("fake export")
    evaluate = subprocess.run(["bash", str(root/"deucalion/run_xrepotest_evaluate_cpu.sh")],
                              env=env, capture_output=True, text=True, timeout=20)
    assert evaluate.returncode == 0, evaluate.stderr
    calls = [json.loads(line) for line in (tmp/"calls.jsonl").read_text().splitlines()]
    gen = next(c for c in calls if "benchmark.xrepotest.run" in c)
    ev = next(c for c in calls if "benchmark.xrepotest.evaluate" in c)
    for flag in ("--no-type-hints", "--no-method-retrieval", "--no-coverage-feedback", "--no-repair"):
        assert flag in gen
    assert gen[gen.index("--task-ids")+1] == ev[ev.index("--task-ids")+1] == env["XREPO_TASK_IDS"]


@pytest.mark.parametrize("value", ["yes", "2", "-1"])
def test_cluster_rejects_invalid_ablation_switches(fake_cluster, value):
    root, tmp, env = fake_cluster
    env["XREPO_NO_TYPE_HINTS"] = value
    result = subprocess.run(["bash", str(root/"deucalion/run_xrepotest_generate_gpu.sh")],
                            env=env, capture_output=True, text=True, timeout=20)
    assert result.returncode != 0
    calls = [json.loads(line) for line in (tmp/"calls.jsonl").read_text().splitlines()]
    assert not any("benchmark.xrepotest.run" in call for call in calls)

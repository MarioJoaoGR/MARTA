import json
from pathlib import Path
import os
import signal
import subprocess
import sys
import time

import pytest

from benchmark.xrepotest import cluster


def test_certification_requires_both_reports(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    preflight = {"ready": True, "runtime_checked": True, "mutation_ready": True, "environment": {"id": 1}}
    (reports / "preflight.json").write_text(json.dumps(preflight))
    diagnostics = {"ready": False, "environment": {"id": 1}}
    (reports / "environment-diagnostics.json").write_text(json.dumps(diagnostics))
    with pytest.raises(ValueError, match="both pass"):
        cluster.certified(tmp_path)
    diagnostics["ready"] = True
    (reports / "environment-diagnostics.json").write_text(json.dumps(diagnostics))
    cluster.certified(tmp_path)
    diagnostics["environment"] = {"id": 2}
    (reports / "environment-diagnostics.json").write_text(json.dumps(diagnostics))
    with pytest.raises(ValueError, match="differ"):
        cluster.certified(tmp_path)


def test_model_metadata_never_pulls_or_generates(monkeypatch):
    import io
    calls = []
    def reply(request, timeout):
        calls.append((request.full_url, request.data))
        responses = {"tags": {"models": [{"name": "qwen3.6:35b", "digest": "sha256:abc"}]},
                     "show": {"capabilities": ["thinking"]}, "version": {"version": "0.30.7"}}
        return io.BytesIO(json.dumps(responses[request.full_url.rsplit("/", 1)[1]]).encode())
    monkeypatch.setattr(cluster, "urlopen", reply)
    assert cluster.model_metadata("http://localhost:9999", "qwen3.6:35b")["model"]["digest"] == "sha256:abc"
    assert [url.rsplit("/", 1)[1] for url, _ in calls] == ["tags", "show", "version"]
    with pytest.raises(ValueError, match="already be installed"):
        cluster.model_metadata("http://localhost:9999", "missing:1b")


def test_gpt_passes_thinking_and_returns_only_final_content(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    import httpx
    from openai import OpenAI
    from marta.gptapi import MyGPT
    client = MyGPT.__new__(MyGPT)
    client.model_type, client.temperature, client.max_tokens = "qwen3.6:35b", 0.6, 16384
    client.reasoning_effort, client.top_p, client.presence_penalty = "high", 0.95, 0
    client.request_timeout = 1800
    requests = []
    def reply(request):
        requests.append(json.loads(request.content))
        return httpx.Response(200, json={"id": "mock", "object": "chat.completion", "created": 0,
            "model": "qwen3.6:35b", "choices": [{"index": 0, "finish_reason": "stop",
                "message": {"role": "assistant", "content": "RSpec.describe {}", "reasoning": "separate thinking"}}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 80, "total_tokens": 90}})
    client.client = OpenAI(api_key="test", base_url="http://local.invalid/v1",
                          http_client=httpx.Client(transport=httpx.MockTransport(reply)))
    assert client.chat([]) == "RSpec.describe {}"
    kwargs = requests[-1]
    assert kwargs["reasoning_effort"] == "high"
    assert kwargs["max_tokens"] == 16384
    assert kwargs["presence_penalty"] == 0 and kwargs["top_p"] == 0.95
    assert client.last_call["completion_tokens"] == 80
    client.reasoning_effort = "none"
    client.chat([])
    assert requests[-1]["reasoning_effort"] == "none"
    client.reasoning_effort = None
    client.chat([])
    assert "reasoning_effort" not in requests[-1]
    client.client.close()


@pytest.fixture
def fake_cluster(tmp_path):
    # Exercise actual Bash job wrappers without Slurm, containers or any LLM.
    root = Path(__file__).resolve().parents[3]
    (tmp_path / "MARTA").symlink_to(root, target_is_directory=True)
    binaries = tmp_path / "bin"
    binaries.mkdir()
    dispatcher = f'''#!{sys.executable}
import json, os, pathlib, sys, time
name = pathlib.Path(sys.argv[0]).name
with open(os.environ["CALLS"], "a") as f:
    f.write(json.dumps([name, *sys.argv[1:]]) + "\\n")
if name == "singularity":
    if "serve" in sys.argv: time.sleep(60)
    elif "benchmark.xrepotest.cluster" in sys.argv:
        print("sha256:abc" if "--model" in sys.argv else "OK")
    else:
        pathlib.Path(os.environ["STARTED"]).touch()
        if os.environ.get("HOLD") == "1": time.sleep(60)
        sys.exit(int(os.environ.get("RESULT", "0")))
elif name == "sbatch": print("456")
'''
    for name in ("singularity", "curl", "ml", "flock", "sbatch"):
        file = binaries / name
        file.write_text(dispatcher)
        file.chmod(0o755)
    env = dict(os.environ, PATH=str(binaries) + ":" + os.environ["PATH"],
               MARTA_CLUSTER_BASE=str(tmp_path), XREPO_RUN="new-experiment",
               MODEL="qwen3.6:35b", XREPO_THINKING="on", SLURM_JOB_ID="123",
               CALLS=str(tmp_path / "calls.jsonl"), STARTED=str(tmp_path / "started"))
    return root, tmp_path, env


def test_generation_wrapper_keeps_old_results_out_and_failure_does_not_chain(fake_cluster):
    root, tmp, env = fake_cluster
    env["RESULT"] = "7"
    proc = subprocess.run(["bash", str(root / "deucalion/run_xrepotest_generate_gpu.sh")],
                          env=env, capture_output=True, text=True, timeout=20)
    assert proc.returncode == 7, proc.stderr
    calls = [json.loads(l) for l in (tmp / "calls.jsonl").read_text().splitlines()]
    assert not any(c[0] == "sbatch" for c in calls)
    invocation = next(c for c in calls if "benchmark.xrepotest.run" in c)
    loading_gate = next(c for c in calls if "--require-loading" in c)
    server = next(c for c in calls if "serve" in c)
    assert calls.index(loading_gate) < calls.index(server) < calls.index(invocation)
    assert invocation[invocation.index("--model-digest") + 1] == "sha256:abc"
    assert invocation[invocation.index("--thinking") + 1] == "on"
    assert "/data/xrepo/runs/new-experiment/generation" in invocation
    assert not any("results_ruby" in arg or "ruby_projects" in arg for arg in invocation)


def test_loading_cpu_wrapper_only_runs_diagnostics(fake_cluster):
    root, tmp, env = fake_cluster
    proc = subprocess.run(["bash", str(root / "deucalion/run_xrepotest_loading_cpu.sh")],
                          env=env, capture_output=True, text=True, timeout=20)
    assert proc.returncode == 0, proc.stderr
    calls = [json.loads(l) for l in (tmp / "calls.jsonl").read_text().splitlines()]
    assert len(calls) == 2
    assert "benchmark.xrepotest.environment.verify_loading" in calls[0]
    assert "--require-loading" in calls[1]
    assert not any("serve" in c or "benchmark.xrepotest.run" in c for c in calls)


@pytest.mark.parametrize("sig,chains", [(signal.SIGTERM, False), (signal.SIGUSR1, True)])
def test_only_walltime_signal_chains_evaluation(fake_cluster, sig, chains):
    root, tmp, env = fake_cluster
    processed = tmp / "xrepotest/runs/new-experiment/generation/processed.jsonl"
    processed.parent.mkdir(parents=True)
    processed.write_text("placeholder: fake evaluator does not read responses\n")
    env["HOLD"] = "1"
    proc = subprocess.Popen(["bash", str(root / "deucalion/run_xrepotest_evaluate_cpu.sh")],
                            env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        for _ in range(100):
            if Path(env["STARTED"]).exists(): break
            if proc.poll() is not None: pytest.fail(str(proc.communicate()))
            time.sleep(.05)
        assert Path(env["STARTED"]).exists()
        proc.send_signal(sig)
        proc.communicate(timeout=10)
        calls = [json.loads(l) for l in (tmp / "calls.jsonl").read_text().splitlines()]
        submissions = [c for c in calls if c[0] == "sbatch"]
        assert bool(submissions) == chains
        if chains:
            assert "--dependency=afterany:123" in submissions[0]
            assert submissions[0][-1] == str(tmp / "MARTA/deucalion/run_xrepotest_evaluate_cpu.sh")
    finally:
        if proc.poll() is None:
            proc.terminate()
            proc.communicate(timeout=10)

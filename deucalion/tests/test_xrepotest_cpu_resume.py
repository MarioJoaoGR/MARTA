import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

import pytest

from benchmark.xrepotest.protocol import SCHEMA, DATA_SHA256, code_fingerprint, digest
from deucalion import xrepotest_cpu_resume as resume
from deucalion import verify_marta_ollama_cpu as cpu

CODE = Path(__file__).resolve().parents[2]


@pytest.fixture
def saved(tmp_path):
    ids = json.loads((CODE / "deucalion/selections/xrepotest_ablation97_v1.json").read_text())
    root = tmp_path / "xrepotest"
    selection = root / "selections/xrepotest_ablation97_v1.json"
    selection.parent.mkdir(parents=True)
    selection.write_text(json.dumps(ids))
    generation = root / "runs" / resume.COHORT / "generation"
    generation.mkdir(parents=True)
    (generation.parent / "metadata").mkdir()
    d = {"schema": SCHEMA, "dataset": DATA_SHA256, "marta_code": code_fingerprint(),
         "model": "qwen3.6:35b", "model_digest": resume.MODEL_DIGEST,
         "thinking": "on", "no_graph": True, "max_tokens": 16384,
         "temperature": 0.6, "top_p": 0.95, "presence_penalty": 0,
         "request_timeout": 1800, "rounds": 3, "attempts": 3,
         "runtime_env": {"OLLAMA_CTX": "32768", "TRANSFORMER_PATH": "BAAI/bge-large-en-v1.5",
                         "MARTA_MAX_CONTEXT_CHARS": ""},
         "task_selection": {"task_ids": ids, "digest": digest(ids)}}
    (generation / "experiment.json").write_text(json.dumps(d))
    for i, tid in enumerate(ids[:39]):
        folder = generation / "tasks" / str(tid)
        folder.mkdir(parents=True)
        status = "running" if i == 38 else ("no_tests" if i < 5 else "complete")
        (folder / "state.json").write_text(json.dumps({"status": status}))
        if status == "complete":
            (folder / "final_spec.rb").write_text("RSpec.describe { it { expect(1).to eq(1) } }\n")
        (folder / "events.jsonl").write_text('{"tipo":"llm"}\n')
    return generation, d, ids


def proof(job="123"):
    return {"backend": "cpu", "cpu_threads": 8, "size_vram": 0,
            "context_length": 32768, "model_digest": resume.MODEL_DIGEST,
            "ollama_version": "0.30.7", "slurm_job_id": job}


def test_preserved_38_tasks_and_exact_manifest_survive_a_cpu_boundary(saved):
    generation, d, ids = saved
    audit = generation.parent / "metadata/cpu_resume_123.json"
    manifest = (generation / "experiment.json").read_bytes()
    before = resume.start(generation, audit, proof(), "123")
    assert len(before["before"]["terminal_file_hashes"]) > 38
    running = generation / "tasks" / str(ids[38]) / "state.json"
    running.write_text('{"status":"no_tests"}')
    end = resume.finish(generation, audit, 143)
    assert end["tasks_finished_in_cpu_job"] == [ids[38]]
    assert end["prior_terminal_files_preserved"]
    assert (generation / "experiment.json").read_bytes() == manifest
    assert resume.environment(d)["XREPO_MAX_TOKENS"] == "16384"
    assert resume.environment(d)["XREPO_THINKING"] == "on"


@pytest.mark.parametrize("field,value", [("marta_code", "changed"), ("model_digest", "changed"),
    ("max_tokens", 32768), ("request_timeout", 3600), ("thinking", "off")])
def test_incompatible_cpu_resume_is_refused(saved, field, value):
    generation, d, ids = saved
    d[field] = value
    (generation / "experiment.json").write_text(json.dumps(d))
    with pytest.raises(ValueError):
        resume.validate(generation)


def test_wrong_selection_finished_export_and_changed_terminal_files_are_refused(saved):
    generation, d, ids = saved
    selection = generation.parents[2] / "selections/xrepotest_ablation97_v1.json"
    selection.write_text(json.dumps(ids[:-1]))
    with pytest.raises(ValueError, match="selection differs"):
        resume.validate(generation)
    selection.write_text(json.dumps(ids))
    exported = generation / "processed.jsonl"
    exported.write_text("{}\n")
    with pytest.raises(ValueError, match="already exported"):
        resume.validate(generation)
    exported.unlink()
    audit = generation.parent / "metadata/cpu_resume_123.json"
    resume.start(generation, audit, proof(), "123")
    (generation / "tasks" / str(ids[5]) / "final_spec.rb").write_text("changed")
    with pytest.raises(ValueError, match="Previously terminal"):
        resume.finish(generation, audit, 143)


def test_wrong_job_or_gpu_proof_is_refused(saved):
    generation, d, ids = saved
    audit = generation.parent / "metadata/cpu_resume_123.json"
    with pytest.raises(ValueError, match="proof"):
        resume.start(generation, audit, proof("other-job"), "123")
    p = proof()
    p["size_vram"] = 100
    with pytest.raises(ValueError, match="proof"):
        resume.start(generation, audit, p, "123")


def test_cpu_load_verifies_real_threads_vram_and_weights_without_answer(tmp_path):
    log = tmp_path / "ollama.log"
    log.write_text("system_info: n_threads = 8 (n_threads_batch = 8)\n")
    calls = []
    def query(path, payload=None):
        calls.append((path, payload))
        return {"/api/version": {"version": "0.30.7"},
                "/api/tags": {"models": [{"name": "qwen3.6:35b", "digest": cpu.MODEL_DIGEST}]},
                "/api/generate": {"done_reason": "load", "response": "", "eval_count": 0},
                "/api/ps": {"models": [{"name": "qwen3.6:35b", "digest": cpu.MODEL_DIGEST,
                                          "context_length": 32768, "size_vram": 0}]}}[path]
    p = cpu.verify("http://127.0.0.1:12345", "qwen3.6:35b", 32768, query, 8, log)
    assert p["cpu_threads"] == 8 and p["size_vram"] == 0
    assert calls[2][1]["prompt"] == ""
    assert calls[2][1]["options"] == {"num_ctx": 32768}
    log.write_text("system_info: n_threads = 128 (n_threads_batch = 128)\n")
    with pytest.raises(ValueError, match="thread count"):
        cpu.verify("http://127.0.0.1:12345", "qwen3.6:35b", 32768, query, 8, log)


def fake_commands(saved, tmp_path):
    generation, d, ids = saved
    binaries = tmp_path / "bin"
    binaries.mkdir()
    fake = binaries / "fake"
    fake.write_text("#!" + sys.executable + "\n" + r'''
import fcntl, json, os, pathlib, subprocess, sys, time
name = pathlib.Path(sys.argv[0]).name
args = sys.argv[1:]
base = pathlib.Path(os.environ['MARTA_CLUSTER_BASE'])
code = pathlib.Path(os.environ['MARTA_CLUSTER_CODE'])
with (base / 'calls.jsonl').open('a') as out:
    out.write(json.dumps({'name': name, 'args': args}) + '\n')
if name == 'flock':
    try:
        fcntl.flock(int(args[-1]), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit(1)
if name == 'curl':
    print('{"version":"0.30.7"}')
if name == 'sbatch':
    print('45678')
if name == 'singularity':
    if args[-2:] == ['ollama', 'serve']:
        while True:
            time.sleep(.05)
    if 'benchmark.xrepotest.cluster' in args:
        print('096fdbd02fe620fc10cbeb6537e080f8041aece851e5d696aed024d4f70f2e47' if '--model' in args else 'OK')
    elif '/opt/marta/deucalion/xrepotest_cpu_resume.py' in args:
        offset = args.index('/opt/marta/deucalion/xrepotest_cpu_resume.py')
        mapped = [a.replace('/data/xrepo/', str(base / 'xrepotest') + '/') for a in args[offset+1:]]
        sys.exit(subprocess.call([sys.executable, '-B', str(code / 'deucalion/xrepotest_cpu_resume.py')] + mapped))
    elif '/opt/marta/deucalion/verify_marta_ollama_cpu.py' in args:
        path = pathlib.Path(args[args.index('--output')+1].replace('/data/xrepo/', str(base / 'xrepotest') + '/'))
        path.write_text(json.dumps({'backend': 'cpu', 'cpu_threads': 8, 'size_vram': 0,
            'context_length': 32768, 'model_digest': '096fdbd02fe620fc10cbeb6537e080f8041aece851e5d696aed024d4f70f2e47',
            'ollama_version': '0.30.7', 'slurm_job_id': os.environ['SLURM_JOB_ID']}))
    elif 'benchmark.xrepotest.run' in args:
        (base / 'started').touch()
        if os.environ.get('HOLD') == '1':
            while True:
                time.sleep(.05)
        if os.environ.get('RESULT'):
            sys.exit(int(os.environ['RESULT']))
        gen = base / 'xrepotest/runs' / os.environ['XREPO_RUN'] / 'generation'
        ids = json.loads((base / 'xrepotest/selections/xrepotest_ablation97_v1.json').read_text())
        for tid in ids:
            folder = gen / 'tasks' / str(tid)
            if not (folder / 'state.json').exists() or json.loads((folder / 'state.json').read_text())['status'] == 'running':
                folder.mkdir(parents=True, exist_ok=True)
                (folder / 'state.json').write_text('{"status":"no_tests"}')
        (gen / 'processed.jsonl').write_text(''.join(json.dumps({'task_id': t, 'response': []}) + '\n' for t in ids))
''')
    fake.chmod(0o755)
    for name in ('singularity', 'curl', 'flock', 'sbatch', 'scontrol', 'lscpu'):
        (binaries / name).symlink_to(fake)
    env = dict(os.environ, MARTA_CLUSTER_BASE=str(tmp_path), MARTA_CLUSTER_CODE=str(CODE),
               XREPO_RUN=resume.COHORT, SLURM_JOB_ID='123', SLURM_GPUS_ON_NODE='0',
               XREPO_CPU_CHAIN='1', PYTHONPATH=str(CODE), PYTHONDONTWRITEBYTECODE='1',
               PATH=str(binaries) + ':' + os.environ['PATH'])
    env.pop('SLURM_JOB_GPUS', None)
    return env


def test_shell_resume_restores_parameters_preserves_tasks_and_uses_cpu(saved, tmp_path):
    env = fake_commands(saved, tmp_path)
    # Inherited settings must not override the saved experiment.
    env.update(MODEL='wrong-model', XREPO_MAX_TOKENS='32768', XREPO_NO_REPAIR='1')
    child = subprocess.run(['bash', str(CODE / 'deucalion/run_xrepotest_generate_cpu.sh')],
        env=env, capture_output=True, text=True, timeout=20)
    assert child.returncode == 0, child.stdout + child.stderr
    calls = [json.loads(l) for l in (tmp_path / 'calls.jsonl').read_text().splitlines()]
    server = next(c['args'] for c in calls if c['name'] == 'singularity' and 'serve' in c['args'])
    generation = next(c['args'] for c in calls if 'benchmark.xrepotest.run' in c['args'])
    assert '--nv' not in server and 'LLAMA_ARG_THREADS=8' in server
    assert 'CUDA_VISIBLE_DEVICES=-1' in server
    assert generation[generation.index('--model') + 1] == 'qwen3.6:35b'
    assert generation[generation.index('--max-tokens') + 1] == '16384'
    assert generation[generation.index('--request-timeout') + 1] == '1800'
    assert '--no-graph' in generation and '--no-repair' not in generation
    assert not any(a.startswith('MARTA_MAX_CONTEXT_CHARS=') for a in generation)
    assert 'TRANSFORMER_PATH=BAAI/bge-large-en-v1.5' in generation
    assert not any(c['name'] == 'sbatch' for c in calls)
    audit = json.loads((saved[0].parent / 'metadata/cpu_resume_123.json').read_text())
    assert len(audit['tasks_finished_in_cpu_job']) == 59
    assert audit['prior_terminal_files_preserved'] and audit['exit_code'] == 0


@pytest.mark.parametrize('sig,chains', [(signal.SIGTERM, False), (signal.SIGUSR1, True)])
def test_shell_walltime_chains_same_cpu_job_but_cancel_does_not(saved, tmp_path, sig, chains):
    env = fake_commands(saved, tmp_path)
    env['HOLD'] = '1'
    child = subprocess.Popen(['bash', str(CODE / 'deucalion/run_xrepotest_generate_cpu.sh')],
        env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        end = time.monotonic() + 10
        while not (tmp_path / 'started').exists() and child.poll() is None and time.monotonic() < end:
            time.sleep(.05)
        assert (tmp_path / 'started').exists()
        child.send_signal(sig)
        out, err = child.communicate(timeout=10)
        assert child.returncode == 143, out + err
        calls = [json.loads(l) for l in (tmp_path / 'calls.jsonl').read_text().splitlines()]
        queued = [c for c in calls if c['name'] == 'sbatch']
        assert bool(queued) == chains
        if chains:
            assert '--dependency=afterany:123' in queued[0]['args']
            assert queued[0]['args'][-1] == str(CODE / 'deucalion/run_xrepotest_generate_cpu.sh')
        audit = json.loads((saved[0].parent / 'metadata/cpu_resume_123.json').read_text())
        assert audit['exit_code'] == 143 and audit['prior_terminal_files_preserved']
    finally:
        if child.poll() is None:
            child.terminate()
        child.communicate(timeout=10)


def test_transport_failure_is_audited_and_not_automatically_resubmitted(saved, tmp_path):
    env = fake_commands(saved, tmp_path)
    env['RESULT'] = '7'
    child = subprocess.run(['bash', str(CODE / 'deucalion/run_xrepotest_generate_cpu.sh')],
        env=env, capture_output=True, text=True, timeout=20)
    assert child.returncode == 7, child.stdout + child.stderr
    calls = [json.loads(l) for l in (tmp_path / 'calls.jsonl').read_text().splitlines()]
    assert not any(c['name'] == 'sbatch' for c in calls)
    audit = json.loads((saved[0].parent / 'metadata/cpu_resume_123.json').read_text())
    assert audit['exit_code'] == 7 and audit['prior_terminal_files_preserved']
    assert audit['tasks_finished_in_cpu_job'] == []

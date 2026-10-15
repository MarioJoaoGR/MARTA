import asyncio
from copy import deepcopy
import fcntl
import json
import os
import signal
import subprocess
import time
from pathlib import Path
import shutil
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from benchmark.xrepotest import protocol, run
from deucalion import xrepotest_project_split as split
from deucalion.tests.test_xrepotest_cpu_resume import saved, fake_commands, proof
from marta.ruby_backend.tests import test_full_context as context_tests


@pytest.fixture
def prepared_source(saved):
    gen, d, ids = saved
    shutil.rmtree(gen / "tasks")
    finished = {tid for p in ("capybara", "dotenv", "grape", "hanami") for tid in split.GROUPS[p]}
    for n, tid in enumerate(sorted(finished)):
        folder = gen / "tasks" / str(tid)
        folder.mkdir(parents=True)
        status = "no_tests" if n < 5 else "complete"
        (folder / "state.json").write_text(json.dumps({"task_id": tid, "status": status}))
        if status == "complete":
            (folder / "final_spec.rb").write_text("RSpec.describe 'old-" + str(tid) + "' do; end\n")
    folder = gen / "tasks/168"
    folder.mkdir(parents=True)
    (folder / "state.json").write_text('{"task_id":168,"status":"running"}')
    (folder / "unfinished_spec.rb").write_text("never accept this unfinished output")
    d["input_hashes"] = {p: "source-" + p for p in split.GROUPS}
    d["runtime_hashes"] = {p: "runtime-" + p for p in split.GROUPS}
    d["context"], d["generation"] = "production-project", "independent-task"
    (gen / "experiment.json").write_text(json.dumps(d))
    tasks = []
    for p, tids in split.GROUPS.items():
        calls = gen / "analysis" / p / "calls"
        calls.mkdir(parents=True)
        (calls / "cached.json").write_text('{"response":"preserved summary"}')
        (calls.parent / "events.jsonl").write_text('{"tipo":"llm","completion_tokens":12}\n')
        tasks.extend({"task_id": tid, "file_path": p + "/lib/context.rb"} for tid in tids)
    return gen.parent, d, sorted(tasks, key=lambda t: t["task_id"])


def finish_children(parent, record, tasks):
    for project in record["worker_projects"]:
        item = record["projects"][project]
        gen = parent.parent / item["run"] / "generation"
        for tid in item["task_ids"]:
            status = split.state(gen, tid)
            if status not in split.TERMINAL:
                folder = gen / "tasks" / str(tid)
                folder.mkdir(parents=True, exist_ok=True)
                (folder / "state.json").write_text(json.dumps({"task_id": tid, "status": "complete"}))
                (folder / "final_spec.rb").write_text("RSpec.describe 'new-" + str(tid) + "' do; end\n")
        selected = [t for t in tasks if t["task_id"] in item["task_ids"]]
        protocol.export_responses(selected, gen, gen / "processed.jsonl")


def test_partition_is_exactly_97_ids_and_preserves_every_other_config_field(prepared_source):
    parent, original, tasks = prepared_source
    before = split.files(parent / "generation")
    plan = split.plan(parent, tasks)
    assert plan["pending"] == 57
    assert set(plan["worker_projects"]) == {"hashie", "httparty", "pundit", "rom", "rspec-core", "shoryuken"}
    assert sum(len(p["task_ids"]) for p in plan["projects"].values()) == 97
    for p, entry in plan["projects"].items():
        changed = {k for k in original if original[k] != entry["config"][k]}
        assert changed == {"task_selection", "input_hashes", "runtime_hashes"}
        assert set(entry["config"]["input_hashes"]) == {p}
        assert entry["config"]["input_hashes"][p] == original["input_hashes"][p]
        assert entry["config"]["runtime_hashes"][p] == original["runtime_hashes"][p]
    assert before == split.files(parent / "generation")
    assert not split.marker(parent).exists()


def test_prepare_refuses_a_running_serial_job(prepared_source):
    parent, _, tasks = prepared_source
    for path in (parent / "generation-job.lock", parent / "generation/run.lock"):
        with path.open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with pytest.raises(BlockingIOError):
                split.prepare(parent, tasks)
        assert not split.marker(parent).exists()


def test_copy_keeps_checkpoints_and_partial_attempts_in_isolated_trees(prepared_source):
    parent, _, tasks = prepared_source
    before = split.files(parent / "generation")
    record = split.prepare(parent, tasks)
    assert before == split.files(parent / "generation")
    for p in record["worker_projects"]:
        item = record["projects"][p]
        gen = parent.parent / item["run"] / "generation"
        split.verify_files(gen, item["seed_files"], exact=True)
        calls = gen / "analysis" / p / "calls/cached.json"
        assert calls.read_text() == '{"response":"preserved summary"}'
        calls.write_text('{"response":"new child content"}')
        assert (parent / "generation/analysis" / p / "calls/cached.json").read_text() == '{"response":"preserved summary"}'
    gen = parent.parent / record["projects"]["hashie"]["run"] / "generation"
    run.archive_incomplete_task(gen, 168)
    assert (gen / "interrupted_tasks/168/1/unfinished_spec.rb").exists()
    assert (parent / "generation/tasks/168/unfinished_spec.rb").exists()
    assert split.prepare(parent, tasks) == record  # idempotent; never replaces progressed children


def test_real_summary_cache_and_full_analysis_survive_output_relocation(tmp_path):
    case = context_tests.FullContextTests(methodName="test_full_pool_context_reaches_selected_generation")
    case.setUp()
    try:
        original = case.make(target_selectors=[case.selector()], output_root=str(tmp_path / "original"))
        case.analyze(original, enrich=False)
        before = {t.analysis_id: (t.done_what, t.what_todo, t.summary) for t in original.analysis_targets}
        relocated = tmp_path / "relocated"
        shutil.copytree(tmp_path / "original", relocated)
        child = case.make(target_selectors=[case.selector()], output_root=str(relocated))
        case.calls.clear()
        case.analyze(child, enrich=False)
        assert not case.calls
        assert {t.analysis_id: (t.done_what, t.what_todo, t.summary) for t in child.analysis_targets} == before
        assert child._analysis_fingerprint(child.analysis_targets) == original._analysis_fingerprint(original.analysis_targets)
        assert len(child.analysis_targets) == 3 and len(child.targets) == 1
    finally:
        case.doCleanups()


def test_exact_prompt_checkpoint_is_reused_after_copy_without_llm(tmp_path):
    source = tmp_path / "source"
    key = protocol.digest(["what_todo_raiz", "same system", "same source"])
    protocol.atomic_json(source / (key + ".json"), {"response": "cached result"})
    destination = tmp_path / "copy"
    shutil.copytree(source, destination)
    client = SimpleNamespace(aask=AsyncMock(side_effect=AssertionError("Unexpected model call")), last_call={})
    recorder = SimpleNamespace(fase_atual="what_todo_raiz", evento=Mock())
    checkpoint = run.SummaryCheckpoints(destination, client, recorder)
    assert asyncio.run(checkpoint("same system", "same source")) == "cached result"
    client.aask.assert_not_awaited()


def test_merge_keeps_97_outputs_including_no_tests_and_refuses_incomplete_children(prepared_source):
    parent, _, tasks = prepared_source
    before = split.files(parent / "generation")
    record = split.prepare(parent, tasks)
    with pytest.raises(ValueError, match="not finished"):
        split.merge(parent, tasks)
    assert not (parent / "project_parallel/merged/processed.jsonl").exists()
    finish_children(parent, record, tasks)
    result = split.merge(parent, tasks)
    rows = [json.loads(l) for l in Path(result["output"]).read_text().splitlines()]
    assert len(rows) == 97 and [r["task_id"] for r in rows] == [t["task_id"] for t in tasks]
    assert sum(not r["response"] for r in rows) == 5
    for row in rows:
        original = parent / "generation/tasks" / str(row["task_id"]) / "final_spec.rb"
        if original.exists():
            assert row["response"] == [original.read_text()]
    assert before == split.files(parent / "generation")
    assert split.merge(parent, tasks)["output"] == result["output"]


@pytest.mark.parametrize("change", ["duplicate", "foreign", "suite", "frozen"])
def test_merge_rejects_duplicate_foreign_changed_suites_or_mutated_parent(prepared_source, change):
    parent, _, tasks = prepared_source
    record = split.prepare(parent, tasks)
    finish_children(parent, record, tasks)
    gen = parent.parent / record["projects"]["hashie"]["run"] / "generation"
    path = gen / "processed.jsonl"
    rows = [json.loads(l) for l in path.read_text().splitlines()]
    if change == "duplicate":
        rows.append(rows[0])
    elif change == "foreign":
        rows[0]["task_id"] = 999
    elif change == "suite":
        rows[0]["response"] = ["changed answer"]
    else:
        (parent / "generation/experiment.json").write_text("{}")
    path.write_text("".join(json.dumps(r) + "\n" for r in rows))
    with pytest.raises(ValueError):
        split.merge(parent, tasks)
    assert not (parent / "project_parallel/merged/processed.jsonl").exists()


def test_child_cpu_audit_and_finished_project_are_bound_to_its_own_ids(prepared_source):
    parent, _, tasks = prepared_source
    record = split.prepare(parent, tasks)
    _, item, gen = split.worker(parent, "hashie")
    split.worker_start(parent, "hashie", proof(), "123")
    # A checkpointed task may finish in this CPU job; the serial source must stay frozen.
    (gen / "tasks/168/state.json").write_text('{"task_id":168,"status":"no_tests"}')
    result = split.worker_finish(parent, "hashie", "123", 143)
    assert result["tasks_finished_in_cpu_job"] == [168]
    assert len(result["before"]["task_states"]) == 10
    assert split.state(parent / "generation", 168) == "running"
    with pytest.raises(ValueError, match="not an active"):
        split.worker(parent, "capybara")


def test_validate_only_config_without_schema_matches_frozen_child_config(prepared_source):
    parent, original, tasks = prepared_source
    for p in split.GROUPS:
        candidate = split.project_config(original, p, split.GROUPS[p])
        candidate.pop("schema")  # --validate-only returns config before guard_run adds schema.
        assert split.check_config(original, p, candidate)["exact_config_match"]
        candidate["max_tokens"] *= 2
        with pytest.raises(ValueError, match="max_tokens"):
            split.check_config(original, p, candidate)


def test_actual_cpu_wrappers_run_distinct_projects_but_reject_duplicate_and_serial(prepared_source, saved, tmp_path):
    parent, _, tasks = prepared_source
    record = split.prepare(parent, tasks)
    env = fake_commands(saved, tmp_path)
    fake = tmp_path / "bin/fake"
    text = fake.read_text()
    text = text.replace("fcntl.LOCK_EX | fcntl.LOCK_NB", "(fcntl.LOCK_SH if 's' in args[0] else fcntl.LOCK_EX) | fcntl.LOCK_NB")
    text = text.replace("{'name': name, 'args': args}", "{'name': name, 'args': args, 'project': os.environ.get('XREPO_PROJECT_SHARD')}")
    text = text.replace("elif '/opt/marta/deucalion/xrepotest_cpu_resume.py' in args:",
        "elif '/opt/marta/deucalion/xrepotest_cpu_resume.py' in args or '/opt/marta/deucalion/xrepotest_project_split.py' in args:")
    text = text.replace("offset = args.index('/opt/marta/deucalion/xrepotest_cpu_resume.py')",
        "offset = next(i for i, a in enumerate(args) if a in ('/opt/marta/deucalion/xrepotest_cpu_resume.py', '/opt/marta/deucalion/xrepotest_project_split.py'))")
    text = text.replace("str(code / 'deucalion/xrepotest_cpu_resume.py')] + mapped",
        "str(code / 'deucalion' / pathlib.Path(args[offset]).name)] + mapped + ['--parent', str(base / 'xrepotest/runs/qwen36_35b_ablation97_no_graph_v1')]")
    text = text.replace("(base / 'started').touch()", "(base / ('started_' + os.environ['SLURM_JOB_ID'])).touch()")
    text = text.replace("sys.exit(subprocess.call([sys.executable, '-B', str(code / 'deucalion' / pathlib.Path(args[offset]).name)] + mapped + ['--parent', str(base / 'xrepotest/runs/qwen36_35b_ablation97_no_graph_v1')]))",
        "result = subprocess.call([sys.executable, '-B', str(code / 'deucalion' / pathlib.Path(args[offset]).name)] + mapped + ['--parent', str(base / 'xrepotest/runs/qwen36_35b_ablation97_no_graph_v1')])\n        if 'env' in mapped and result == 0:\n            envfile = pathlib.Path(mapped[mapped.index('--env-file') + 1])\n            envfile.write_text(envfile.read_text().replace(str(base / 'xrepotest'), '/data/xrepo'))\n        sys.exit(result)")
    fake.write_text(text)
    env['HOLD'] = '1'
    script = Path(__file__).resolve().parents[2] / 'deucalion/run_xrepotest_generate_cpu.sh'
    children = []
    try:
        for n, project in enumerate(('hashie', 'httparty')):
            job = str(123 + n)
            child = subprocess.Popen(['bash', str(script)], env=dict(env,
                SLURM_JOB_ID=job, XREPO_RUN=record['projects'][project]['run'], XREPO_PROJECT_SHARD=project),
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            children.append(child)
            end = time.monotonic() + 10
            while not (tmp_path / ('started_' + job)).exists() and child.poll() is None and time.monotonic() < end:
                time.sleep(.02)
            if not (tmp_path / ('started_' + job)).exists():
                child.terminate()
                out, err = child.communicate(timeout=10)
                pytest.fail(out + err)
        duplicate = subprocess.run(['bash', str(script)], env=dict(env,
            SLURM_JOB_ID='333', XREPO_RUN=record['projects']['hashie']['run'], XREPO_PROJECT_SHARD='hashie'),
            capture_output=True, text=True, timeout=10)
        assert duplicate.returncode == 2 and 'already running' in duplicate.stdout
        serial = subprocess.run(['bash', str(script)], env=dict(env, XREPO_PROJECT_SHARD=''),
            capture_output=True, text=True, timeout=10)
        assert serial.returncode == 2 and 'frozen' in serial.stdout
        children[0].send_signal(signal.SIGUSR1)
        out, err = children[0].communicate(timeout=10)
        assert children[0].returncode == 143, out + err
        children[1].send_signal(signal.SIGTERM)
        out, err = children[1].communicate(timeout=10)
        assert children[1].returncode == 143, out + err
        calls = [json.loads(l) for l in (tmp_path / 'calls.jsonl').read_text().splitlines()]
        queued = [c for c in calls if c['name'] == 'sbatch']
        assert len(queued) == 1 and queued[0]['project'] == 'hashie'
        assert queued[0]['args'][-1] == str(script)
        assert '--dependency=afterany:123' in queued[0]['args']
    finally:
        for child in children:
            if child.poll() is None:
                child.terminate()
            child.communicate(timeout=10)


def test_frozen_runner_itself_builds_the_same_per_project_configs_without_generation(prepared_source, tmp_path, monkeypatch, capsys):
    from benchmark.xrepotest import runtime
    import sys
    parent, old, tasks = prepared_source
    environment = {"fixture": "same certified image"}
    monkeypatch.setattr(run, 'load_tasks', lambda path: tasks)
    monkeypatch.setattr(runtime, 'environment_manifest', lambda: environment)
    monkeypatch.setattr(run, 'source_inventory', lambda root, rows: {
        'source_digest': old['input_hashes'][root.name],
        'runtime_digest': old['runtime_hashes'][root.name]})
    monkeypatch.setattr(run, 'pipeline', lambda *a, **kw: pytest.fail('Validation invoked generation'))
    for key, value in old['runtime_env'].items():
        if value:
            monkeypatch.setenv(key, value)
        else:
            monkeypatch.delenv(key, raising=False)
    preflight = tmp_path / 'preflight.json'
    preflight.write_text(json.dumps({'ready': True, 'runtime_checked': True,
        'environment': environment, 'dataset_sha256': protocol.DATA_SHA256, 'image': protocol.IMAGE,
        'projects': {p: {'source_digest': old['input_hashes'][p],
                         'runtime_digest': old['runtime_hashes'][p]} for p in split.GROUPS}}))
    selection = tmp_path / 'selected.json'
    base = ['run', '--validate-only', '--dataset', str(tmp_path / 'unused.jsonl'),
        '--preflight', str(preflight), '--output', str(tmp_path / 'not_created/generation'),
        '--work', str(tmp_path / 'not_created/work'), '--task-ids', str(selection),
        '--model', old['model'], '--model-digest', old['model_digest'], '--thinking', 'on',
        '--max-tokens', '16384', '--temperature', '0.6', '--top-p', '0.95',
        '--presence-penalty', '0', '--request-timeout', '1800', '--rounds', '3', '--attempts', '3', '--no-graph']
    selection.write_text(json.dumps(old['task_selection']['task_ids']))
    monkeypatch.setattr(sys, 'argv', base)
    run.main()
    original = {'schema': protocol.SCHEMA, **json.loads(capsys.readouterr().out)}
    certificate = {'ready': True, 'policy': split.POLICY, 'tasks': 97,
        'code_fingerprint': protocol.code_fingerprint(),
        'parent_manifest_digest': protocol.digest(original), 'checks': {}}
    for p, tids in split.GROUPS.items():
        selection.write_text(json.dumps(tids))
        monkeypatch.setattr(sys, 'argv', base)
        run.main()
        candidate = json.loads(capsys.readouterr().out)
        certificate['checks'][p] = split.check_config(original, p, candidate)
    assert not (tmp_path / 'not_created').exists()
    (parent / 'generation/experiment.json').write_text(json.dumps(original))
    split.verify_validation(parent, certificate)
    certificate['checks']['rom']['config_digest'] = 'changed'
    with pytest.raises(ValueError, match='successful ten-project validation'):
        split.verify_validation(parent, certificate)

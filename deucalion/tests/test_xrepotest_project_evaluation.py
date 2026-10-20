import ast
import json
from pathlib import Path
import subprocess

import pytest

from benchmark.xrepotest.tests.test_cluster import fake_cluster
from deucalion import xrepotest_official_failure_audit as audit


@pytest.mark.parametrize("result", [0, 7])
def test_merge_must_pass_before_same_core_evaluator_runs_without_mutation(fake_cluster, result):
    code, tmp, env = fake_cluster
    name = "qwen36_35b_ablation97_no_graph_v1"
    env.update(MARTA_CLUSTER_CODE=str(code), XREPO_RUN=name, RESULT=str(result))
    merged = tmp / "xrepotest/runs" / name / "project_parallel/merged/processed.jsonl"
    merged.parent.mkdir(parents=True)
    merged.write_text("simulated sealed export; fake evaluator does not parse it")
    child = subprocess.run(["bash", str(code / "deucalion/run_xrepotest_project_merge_evaluate_cpu.sh")],
        env=env, capture_output=True, text=True, timeout=20)
    assert child.returncode == result, child.stdout + child.stderr
    calls = [json.loads(l) for l in (tmp / "calls.jsonl").read_text().splitlines()]
    merge = next(c for c in calls if "/opt/marta/deucalion/xrepotest_project_split.py" in c)
    evaluations = [c for c in calls if "benchmark.xrepotest.evaluate" in c]
    assert bool(evaluations) == (result == 0)
    if evaluations:
        call = evaluations[0]
        assert calls.index(merge) < calls.index(call)
        assert call[call.index("--processed")+1].endswith("/project_parallel/merged/processed.jsonl")
        assert call[call.index("--task-ids")+1] == "/data/xrepo/selections/xrepotest_ablation97_v1.json"
        assert "--enable-mutation" not in call
    assert not any("ollama" in c or "benchmark.xrepotest.run" in c for c in calls)


def test_audit_preserves_missing_responses_and_identifies_saved_log_signatures():
    rows = [
        {"task_id": 0, "file_path": "repo/lib/a.rb", "test": [], "checks": [], "logs": []},
        {"task_id": 1, "file_path": "repo/lib/a.rb", "test": ["suite"],
         "checks": [{"compilation": True, "tests": False, "invocation": True}],
         "logs": ["An error occurred while loading file.\n  LoadError:\n    cannot load such file -- spec_helper"]},
        {"task_id": 2, "file_path": "repo/lib/b.rb", "test": ["suite"],
         "checks": [{"compilation": True, "tests": True, "invocation": False}], "logs": ["1 example, 0 failures"]}]
    report = audit.summarize(rows)
    assert report["counts"] == {"tasks": 3, "compilation": 2, "tests": 1, "invocation": 1, "no_response": 1}
    assert report["log_signatures_heuristic"] == {"no_response": 1, "LoadError": 1}
    assert report["examples"]["LoadError"]["task_id"] == 1
    assert "cannot load such file" in report["examples"]["LoadError"]["log_excerpt"]
    assert rows[0]["checks"] == []


@pytest.mark.parametrize("text,label", [("  NameError:\n    uninitialized constant X", "NameError"),
    ("Test execution timeout", "test_execution_timeout"),
    ("Failure/Error: expect(value).to eq(3)\nexpected 3, got 2", "rspec_failure_unclassified")])
def test_log_signature_is_only_a_description(text, label):
    assert audit.signature(text) == label


def test_audit_uses_python36_compatible_syntax():
    ast.parse(Path(audit.__file__).read_text(), feature_version=(3, 6))


def test_saved_mode_audit_requires_675_ids_and_compares_actual_environment(tmp_path):
    folder = tmp_path / 'modes/standard/evaluation_core_v1'
    (folder / 'tasks').mkdir(parents=True)
    manifest = {'dataset': 'pinned', 'evaluator_commit': 'fixed',
                'evaluator_files': {'ruby/evaluator.py': 'sha256'}, 'environment': {'id': 'A'}}
    (folder / 'experiment.json').write_text(json.dumps(manifest))
    (folder / 'summary.json').write_text('{"total_samples":675}')
    for tid in range(675):
        (folder / 'tasks' / (str(tid) + '.json')).write_text(json.dumps({
            'task_id': tid, 'file_path': 'repo/lib/file.rb', 'test': [], 'checks': [], 'logs': []}))
    compared = dict(manifest, environment={'id': 'B'})
    report = audit.inspect(tmp_path, 'standard', compared)
    assert report['counts']['tasks'] == 675 and report['counts']['no_response'] == 675
    assert report['matches_normal_evaluation']['dataset'] is True
    assert report['matches_normal_evaluation']['environment'] is False
    (folder / 'tasks/674.json').unlink()
    with pytest.raises(ValueError, match='675 IDs'):
        audit.inspect(tmp_path, 'standard', compared)

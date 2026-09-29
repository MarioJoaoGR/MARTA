"""Loading certification and audited reuse into a fresh experiment."""
import json

import pytest

from benchmark.xrepotest import cluster, fork_loading_run as migration, protocol, report
from benchmark.xrepotest.environment.verify_loading import loading_fingerprint
from marta.ruby_backend.loading import LOADING_POLICY


def test_nested_only_lib_still_supplies_a_load_path(tmp_path):
    path = tmp_path / "lib/rspec/core.rb"
    path.parent.mkdir(parents=True)
    path.write_text("module RSpec; end")
    task = {"task_id": 1, "file_path": "rspec-core/lib/rspec/core.rb", "file_content": path.read_text()}
    inventory = protocol.source_inventory(tmp_path, [task])
    assert inventory["load_paths"] == ["lib"]
    assert inventory["code_files"] == ["lib/rspec/core.rb"]


@pytest.fixture
def certified_root(tmp_path):
    projects = {"sample": {"source_digest": "source", "runtime_digest": "runtime"}}
    preflight = {"ready": True, "runtime_checked": True, "mutation_ready": True,
                 "environment": {"id": 1}, "projects": projects}
    protocol.atomic_json(tmp_path / "reports/preflight.json", preflight)
    protocol.atomic_json(tmp_path / "reports/environment-diagnostics.json",
                         {"ready": True, "environment": {"id": 1}})
    loading = {"ready": True, "environment": {"id": 1}, "dataset": protocol.DATA_SHA256,
               "policy": LOADING_POLICY, "loading_code": loading_fingerprint(), "projects": projects,
               "checks": {str(i): {"passed": True} for i in range(302)},
               "session_regression": {"passed": True}}
    protocol.atomic_json(tmp_path / "reports/loading-diagnostics.json", loading)
    return tmp_path, loading


def test_complete_loading_gate_passes(certified_root):
    root, _ = certified_root
    cluster.certified(root, require_loading=True)


@pytest.mark.parametrize("change", ["missing", "failed", "code", "environment", "dataset", "partial", "source", "regression", "project"])
def test_loading_gate_rejects_failed_partial_or_stale_reports(certified_root, change):
    root, loading = certified_root
    path = root / "reports/loading-diagnostics.json"
    if change == "missing": path.unlink()
    elif change == "failed": loading["checks"]["0"]["passed"] = False
    elif change == "code": loading["loading_code"] = "old-code"
    elif change == "environment": loading["environment"] = {"id": 2}
    elif change == "dataset": loading["dataset"] = "other-dataset"
    elif change == "partial": loading["checks"].pop("0")
    elif change == "source": loading["projects"]["sample"]["source_digest"] = "changed"
    elif change == "regression": loading["session_regression"]["passed"] = False
    elif change == "project": loading["projects"] = {}
    if change != "missing": protocol.atomic_json(path, loading)
    with pytest.raises(ValueError): cluster.certified(root, require_loading=True)


@pytest.fixture
def predecessor(tmp_path, monkeypatch):
    monkeypatch.setattr(migration, "code_fingerprint", lambda: "new-code")
    root, new = tmp_path / "old", tmp_path / "new"
    config = {"schema": protocol.SCHEMA, "marta_code": migration.SOURCE_CODE,
              "context": "production-project", "no_graph": False, "model": "qwen3.6:35b",
              "thinking": "on", "max_tokens": 16384, "input_hashes": {"sample": "hash"}}
    protocol.atomic_json(root / "experiment.json", config)
    protocol.atomic_json(root / "analysis/sample/calls/exact.json", {"response": "valid summary"})
    protocol.atomic_json(root / "analysis/sample/.marta_ruby_cache/cache.full_context.json", {"summary": "cache"})
    events = root / "analysis/sample/events.jsonl"
    events.write_text(json.dumps({"tipo": "llm", "fase": "sumarios_passagem1", "completion_tokens": 50,
                                 "prompt_tokens": 10, "segundos": 2}) + "\n")
    protocol.atomic_json(root / "analysis/sample/analysis.json", {"old_totals": True})
    protocol.atomic_json(root / "tasks/0/state.json", {"status": "complete"})
    (root / "tasks/0/final_spec.rb").write_text("old answer")
    return root, new, config


def test_fork_keeps_analysis_but_no_old_generation_or_cost_events(predecessor):
    root, new, original = predecessor
    before = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}
    audit = migration.fork(root, new)
    assert audit["checkpoint_count"] == 1
    assert audit["before"] == original
    assert audit["after"] == {**original, "marta_code": "new-code", "generation_loading_policy": LOADING_POLICY}
    assert (new / "analysis/sample/calls/exact.json").read_bytes() == before["analysis/sample/calls/exact.json"]
    assert not (new / "tasks").exists()
    assert not list(new.rglob("events.jsonl"))
    assert not (new / "analysis/sample/analysis.json").exists()
    assert migration.fork(root, new) == audit
    stats = report.summarize(new)
    assert not stats["tasks"] and not stats["llm_by_phase"]
    assert stats["inherited_analysis"]["usage"]["llm_by_phase"]["sumarios_passagem1"]["output_tokens"] == 50
    for rel, content in before.items(): assert (root / rel).read_bytes() == content


@pytest.mark.parametrize("change", ["unknown-code", "no-graph", "empty", "unrelated-output", "extra-analysis", "symlink"])
def test_fork_refuses_incompatible_or_contaminated_inputs(predecessor, change):
    root, new, config = predecessor
    if change == "unknown-code": protocol.atomic_json(root / "experiment.json", {**config, "marta_code": "other"})
    elif change == "no-graph": protocol.atomic_json(root / "experiment.json", {**config, "no_graph": True})
    elif change == "empty": protocol.atomic_json(root / "analysis/sample/calls/exact.json", {"response": ""})
    elif change == "unrelated-output": protocol.atomic_json(new / "tasks/0/state.json", {"status": "complete"})
    elif change == "extra-analysis": protocol.atomic_json(new / "analysis/extra.json", {})
    elif change == "symlink": (root / "analysis/link").symlink_to(root / "tasks/0/final_spec.rb")
    with pytest.raises(ValueError): migration.fork(root, new)
    assert not (new / "experiment.json").exists()


def test_fork_recovers_interrupted_copy(predecessor, monkeypatch):
    root, new, config = predecessor
    copy = migration.shutil.copy2
    def interrupted(source, destination):
        destination.write_text("partial")
        raise OSError("interrupted")
    monkeypatch.setattr(migration.shutil, "copy2", interrupted)
    with pytest.raises(OSError): migration.fork(root, new)
    assert not (new / "experiment.json").exists()
    monkeypatch.setattr(migration.shutil, "copy2", copy)
    audit = migration.fork(root, new)
    assert json.loads((new / "experiment.json").read_text()) == audit["after"]


def test_fork_refuses_active_source(predecessor):
    import fcntl
    root, new, _ = predecessor
    with (root / "run.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises(BlockingIOError): migration.fork(root, new)

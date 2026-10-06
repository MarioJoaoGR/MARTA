import fcntl
import json

import pytest

from benchmark.xrepotest import protocol
from deucalion import upgrade_xrepotest_coverage_output as migration


@pytest.fixture
def interrupted(tmp_path, monkeypatch):
    root = tmp_path / "run/generation"
    monkeypatch.setattr(migration, "code_fingerprint", lambda: migration.REPAIRED_CODE)
    before = {"schema": protocol.SCHEMA, "marta_code": migration.LEGACY_CODE,
              "max_tokens": 16384, "temperature": 0.6, "thinking": "on"}
    protocol.atomic_json(root / "experiment.json", before)
    protocol.atomic_json(root / "analysis/example/calls/key.json", {"response": "saved summary"})
    for tid, status in [(0, "complete"), (1, "no_tests"), (376, "running")]:
        protocol.atomic_json(root / f"tasks/{tid}/state.json", {"task_id": tid, "status": status})
    (root / "tasks/0/final_spec.rb").write_text("# saved suite")
    (root / "tasks/376/saved_spec.rb").write_text("# interrupted suite")
    (root / "tasks/376/events.jsonl").write_text('{"tipo":"llm","completion_tokens":100}\n')
    protocol.atomic_json(root / "interrupted_tasks/376/1/state.json", {"status": "running"})
    return root, before


def test_upgrade_changes_only_code_and_preserves_every_saved_file(interrupted):
    root, before = interrupted
    saved = migration.snapshot(root)
    audit = migration.upgrade(root)
    assert audit["before"] == before
    assert audit["after"] == {**before, "marta_code": migration.REPAIRED_CODE}
    assert audit["preserved_files"] == saved == migration.snapshot(root)
    assert audit["task_states"] == {"0": "complete", "1": "no_tests", "376": "running"}
    assert json.loads((root / "experiment.json").read_text()) == audit["after"]
    assert migration.upgrade(root) == audit


@pytest.mark.parametrize("change", ["old-code", "new-code", "missing-suite", "bad-state", "empty-summary", "export"])
def test_upgrade_refuses_unknown_code_or_broken_state(interrupted, monkeypatch, change):
    root, before = interrupted
    if change == "old-code":
        protocol.atomic_json(root / "experiment.json", {**before, "marta_code": "unknown"})
    elif change == "new-code":
        monkeypatch.setattr(migration, "code_fingerprint", lambda: "other-code")
    elif change == "missing-suite":
        (root / "tasks/0/final_spec.rb").unlink()
    elif change == "bad-state":
        protocol.atomic_json(root / "tasks/376/state.json", {"task_id": 377, "status": "running"})
    elif change == "empty-summary":
        protocol.atomic_json(root / "analysis/example/calls/key.json", {"response": ""})
    else:
        (root / "processed.jsonl").write_text("exported")
    original = (root / "experiment.json").read_bytes()
    with pytest.raises(ValueError):
        migration.upgrade(root)
    assert (root / "experiment.json").read_bytes() == original
    assert not (root / migration.AUDIT).exists()


@pytest.mark.parametrize("which", ["wrapper", "runner"])
def test_upgrade_refuses_active_generation(interrupted, which):
    root, _ = interrupted
    path = root.parent / "generation-job.lock" if which == "wrapper" else root / "run.lock"
    with path.open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises(BlockingIOError):
            migration.upgrade(root)


def test_interrupted_upgrade_recovers_but_detects_changed_results(interrupted, monkeypatch):
    root, _ = interrupted
    write = migration.atomic_json
    def fail_manifest(path, value):
        if path.name == "experiment.json":
            raise OSError("interrupted")
        write(path, value)
    monkeypatch.setattr(migration, "atomic_json", fail_manifest)
    with pytest.raises(OSError):
        migration.upgrade(root)
    monkeypatch.setattr(migration, "atomic_json", write)
    saved = root / "tasks/376/saved_spec.rb"
    original = saved.read_text()
    saved.write_text("changed")
    with pytest.raises(ValueError, match="changed"):
        migration.upgrade(root)
    saved.write_text(original)
    assert migration.upgrade(root)["after"] == json.loads((root / "experiment.json").read_text())

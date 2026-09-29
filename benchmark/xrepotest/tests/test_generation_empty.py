"""Output exhaustion, bounded Dev attempts, and preservation on recovery."""
import asyncio
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from benchmark.xrepotest import protocol, report, run, upgrade_generation_empty as migration
from marta.ruby_backend import generate, prompts
from marta.ruby_backend.recorder import RubyRecorder, token_tracking_ask
from marta.ruby_backend.runner import RSpecResult


def client_with(replies):
    client = SimpleNamespace(last_call={})
    async def ask(system, user):
        out, client.last_call = replies.pop(0)
        return out
    client.aask = AsyncMock(side_effect=ask)
    return client


@pytest.mark.parametrize("answer", [None, "", "   "])
def test_empty_length_is_one_counted_attempt_without_hidden_retry(tmp_path, answer):
    client = client_with([(answer, {"finish_reason": "length", "prompt_tokens": 1905,
                                    "completion_tokens": 16384})])
    rec = RubyRecorder(str(tmp_path / "events.jsonl"))
    request = token_tracking_ask(run.GenerationRequests(client, rec), rec.score, rec)
    with rec.fase("dev_reparacao"), rec.contexto(tentativa=3):
        assert asyncio.run(request("system", "user")) == ""
    assert client.aask.await_count == 1
    stats = report.summarize(tmp_path)["llm_by_phase"]["dev_reparacao"]
    assert (stats["calls"], stats["output_tokens"], stats["truncated"], stats["errors"]) == (1,16384,1,0)
    event = json.loads((tmp_path / "events.jsonl").read_text().splitlines()[0])
    assert event["tentativa"] == 3 and event["finish_reason"] == "length"


@pytest.mark.parametrize("detail", [{"erro": "timeout"}, {"finish_reason": "stop"}])
def test_real_failure_is_recorded_before_aborting(tmp_path, detail):
    client = client_with([(None, {"completion_tokens": 12, **detail})])
    rec = RubyRecorder(str(tmp_path / "events.jsonl"))
    with pytest.raises(RuntimeError):
        asyncio.run(run.GenerationRequests(client, rec)("sys", "user"))
    assert rec.score.llm_calls == 1 and rec.score.llm_erros == 1
    assert rec.score.completion_tokens == 12


def test_raised_exception_has_an_event(tmp_path):
    client = SimpleNamespace(aask=AsyncMock(side_effect=TimeoutError("offline")))
    rec = RubyRecorder(str(tmp_path / "events.jsonl"))
    with pytest.raises(TimeoutError):
        asyncio.run(run.GenerationRequests(client, rec)("sys", "user"))
    assert "offline" in json.loads((tmp_path / "events.jsonl").read_text())["erro"]


def test_nonempty_truncated_code_keeps_existing_validation_policy():
    client = client_with([("partial code", {"finish_reason": "length"})])
    assert asyncio.run(run.GenerationRequests(client, RubyRecorder())("s", "u")) == "partial code"


@pytest.mark.parametrize("recovers", [True, False])
def test_real_generation_loop_keeps_three_attempt_budget(tmp_path, recovers):
    limit = (None, {"finish_reason": "length", "completion_tokens": 16384})
    code = 'RSpec.describe("x") { it("x") { expect(1).to eq(1) } }'
    replies = [limit, limit, limit, (code, {"finish_reason": "stop"}) if recovers else limit]
    client = client_with(replies)
    rec = RubyRecorder(str(tmp_path / "events.jsonl"))
    backend = SimpleNamespace(prompts=prompts, syntax_check=Mock(return_value=None),
                              run_tests=Mock(return_value=RSpecResult(all_passed=True, output="ok")))
    result = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="A.x", describe_subject="A", method_source="def self.x; 1; end",
        require_target="a", load_paths=[], spec_path="answer.rb", cwd=str(tmp_path),
        ask=run.GenerationRequests(client,rec), recorder=rec, backend=backend, max_attempts=3))
    assert client.aask.await_count == 4  # One Planner call plus three Dev attempts.
    assert result.attempts == 3 and result.success is recovers
    assert (tmp_path / "answer.rb").exists() is recovers
    assert backend.run_tests.call_count == int(recovers)
    assert rec.score.llm_calls == 4
    assert "No test code" in client.aask.call_args_list[2].args[1]


@pytest.fixture
def interrupted(tmp_path, monkeypatch):
    monkeypatch.setattr(migration, "code_fingerprint", lambda: "new-code")
    before = {"schema": protocol.SCHEMA, "marta_code": migration.LEGACY_CODE,
              "summary_truncation_attempts": 3, "thinking": "on", "max_tokens": 16384}
    protocol.atomic_json(tmp_path / "experiment.json", before)
    protocol.atomic_json(tmp_path / "analysis/capybara/calls/key.json", {"response": "cached summary"})
    for tid, status in [(0,"complete"), (8,"no_tests"), (14,"running")]:
        protocol.atomic_json(tmp_path / f"tasks/{tid}/state.json", {"task_id":tid,"status":status})
    (tmp_path / "tasks/0/final_spec.rb").write_text("# preserved final suite")
    spec = tmp_path / "tasks/14/marta_specs/round_1.rb"
    spec.parent.mkdir()
    spec.write_text("# unfinished, possibly invalid")
    (tmp_path / "tasks/14/events.jsonl").write_text(json.dumps(
        {"tipo":"llm", "completion_tokens":100, "segundos":1})+"\n")
    return tmp_path, before


def snapshot(root):
    return {str(p.relative_to(root)):p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_upgrade_and_restart_preserve_finished_outcomes_and_total_cost(interrupted):
    root, before = interrupted
    files = snapshot(root / "tasks")
    audit = migration.upgrade(root)
    assert audit["before"] == before
    assert audit["after"] == {**before, "marta_code":"new-code",
                              "generation_empty_length_policy":run.GENERATION_EMPTY_LENGTH_POLICY}
    assert snapshot(root / "tasks") == files
    assert migration.upgrade(root) == audit
    run.archive_incomplete_task(root,14)
    assert not (root / "tasks/14").exists()
    assert (root / "interrupted_tasks/14/1/marta_specs/round_1.rb").read_bytes() == files["14/marta_specs/round_1.rb"]
    assert (root / "tasks/0/final_spec.rb").read_bytes() == files["0/final_spec.rb"]
    assert (root / "tasks/8/state.json").read_bytes() == files["8/state.json"]
    stats = report.summarize(root)
    assert stats["llm_by_phase"]["unlabelled"]["output_tokens"] == 100
    assert stats["historical_telemetry_note"]
    assert stats["tasks"] == {"complete":1,"no_tests":1}


@pytest.mark.parametrize("change", ["unknown-code", "missing-final", "bad-state", "empty-cache", "export"])
def test_upgrade_refuses_incompatible_or_damaged_run(interrupted, change):
    root, before = interrupted
    if change == "unknown-code":
        protocol.atomic_json(root / "experiment.json", {**before,"marta_code":"unknown"})
    elif change == "missing-final":
        (root / "tasks/0/final_spec.rb").unlink()
    elif change == "bad-state":
        protocol.atomic_json(root / "tasks/14/state.json", {"task_id":14,"status":"unexpected"})
    elif change == "empty-cache":
        protocol.atomic_json(root / "analysis/capybara/calls/key.json", {"response":""})
    else:
        (root / "processed.jsonl").write_text("exported")
    original = (root / "experiment.json").read_bytes()
    with pytest.raises(ValueError):
        migration.upgrade(root)
    assert (root / "experiment.json").read_bytes() == original
    assert not (root / "generation_empty_upgrade.json").exists()


def test_interrupted_upgrade_is_recoverable(interrupted, monkeypatch):
    root, before = interrupted
    write = migration.atomic_json
    def fail(path, value):
        if path.name == "experiment.json":
            raise OSError("interrupted")
        write(path,value)
    monkeypatch.setattr(migration,"atomic_json",fail)
    with pytest.raises(OSError): migration.upgrade(root)
    assert json.loads((root / "experiment.json").read_text()) == before
    monkeypatch.setattr(migration,"atomic_json",write)
    assert migration.upgrade(root)["after"] == json.loads((root / "experiment.json").read_text())


@pytest.mark.parametrize("status", ["complete", "no_tests"])
def test_restart_never_archives_a_finalized_task(interrupted, status):
    root, _ = interrupted
    tid = 0 if status == "complete" else 8
    before = snapshot(root / "tasks")
    with pytest.raises(ValueError): run.archive_incomplete_task(root,tid)
    assert snapshot(root / "tasks") == before

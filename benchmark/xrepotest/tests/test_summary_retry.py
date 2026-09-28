"""Offline tests: truncated thinking, exact cache resume, accounting and upgrade."""
import asyncio
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from benchmark.xrepotest import protocol, report, run, upgrade_summary_retry as migration
from marta.ruby_backend.recorder import RubyRecorder, token_tracking_ask


def client_with(replies):
    client = SimpleNamespace(last_call={}, prompts=[])
    async def ask(system, user):
        client.prompts.append((system, user))
        text, detail = replies.pop(0)
        client.last_call = dict(detail)
        return text
    client.aask = ask
    return client


def test_empty_thinking_truncation_retries_same_prompt_and_counts_each_call_once(tmp_path):
    client = client_with([
        (None, {"prompt_tokens": 356, "completion_tokens": 16384, "finish_reason": "length"}),
        ("valid summary", {"prompt_tokens": 356, "completion_tokens": 500, "finish_reason": "stop"}),
    ])
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    checkpoints = run.SummaryCheckpoints(tmp_path / "calls", client, recorder)
    wrapped = token_tracking_ask(checkpoints, recorder.score, recorder)
    with recorder.fase("what_todo_raiz"), recorder.contexto(metodo="Driver#go_back"):
        assert asyncio.run(wrapped("system", "source")) == "valid summary"
        assert asyncio.run(wrapped("system", "source")) == "valid summary"
    assert client.prompts == [("system", "source")] * 2
    assert recorder.score.llm_calls == 2
    assert recorder.score.llm_cortadas == 1
    assert recorder.score.llm_erros == 0
    assert recorder.score.completion_tokens == 16884
    events = [json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    assert [e["tipo"] for e in events] == ["llm", "summary_truncated", "llm", "llm_cache_hit"]
    assert events[1]["retry"] is True
    assert all(e["metodo"] == "Driver#go_back" for e in events)
    assert json.loads(next((tmp_path / "calls").glob("*.json")).read_text()) == {"response": "valid summary"}
    stats = report.summarize(tmp_path)["llm_by_phase"]["what_todo_raiz"]
    assert (stats["calls"], stats["output_tokens"], stats["truncated"], stats["cache_hits"]) == (2,16884,1,1)


@pytest.mark.parametrize("answer", [None, "", "partial summary"])
def test_persistent_truncation_stops_after_three_without_cache(tmp_path, answer):
    client = client_with([(answer, {"completion_tokens": 16384, "finish_reason": "length"})] * 3)
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    checkpoints = run.SummaryCheckpoints(tmp_path / "calls", client, recorder)
    with pytest.raises(RuntimeError, match="all 3 attempts"):
        asyncio.run(checkpoints("system", "source"))
    assert len(client.prompts) == 3
    assert recorder.score.llm_calls == 3
    assert not list((tmp_path / "calls").glob("*.json"))
    assert json.loads((tmp_path / "events.jsonl").read_text().splitlines()[-1])["retry"] is False


def test_legacy_cache_key_still_reuses_exact_response(tmp_path):
    key = protocol.digest(["what_todo_raiz", "system", "source"])
    path = tmp_path / "calls" / (key + ".json")
    protocol.atomic_json(path, {"response": "old valid summary"})
    before = path.read_bytes()
    client = SimpleNamespace(aask=AsyncMock(side_effect=AssertionError("No LLM allowed")))
    rec = RubyRecorder()
    with rec.fase("what_todo_raiz"):
        assert asyncio.run(run.SummaryCheckpoints(path.parent,client,rec)("system","source")) == "old valid summary"
    assert before == path.read_bytes()
    client.aask.assert_not_awaited()


def test_old_failure_usage_is_recovered_but_no_timing_is_invented(tmp_path):
    event = {"tipo":"llm_infrastructure_failure", "detail":{
        "prompt_tokens":356,"completion_tokens":16384,"finish_reason":"length","erro":None}}
    (tmp_path / "events.jsonl").write_text(json.dumps(event)+"\n")
    stats = report.summarize(tmp_path)["llm_by_phase"]["unlabelled"]
    assert (stats["calls"],stats["output_tokens"],stats["truncated"],stats["errors"]) == (1,16384,1,0)
    assert stats["calls_without_timing"] == 1
    assert stats["seconds"] == 0


@pytest.fixture
def legacy(tmp_path, monkeypatch):
    monkeypatch.setattr(migration,"code_fingerprint",lambda:"new-code")
    config = {"schema":protocol.SCHEMA,"marta_code":migration.LEGACY_CODE,
              "model":"qwen3.6:35b","max_tokens":16384,"thinking":"on"}
    protocol.atomic_json(tmp_path / "experiment.json",config)
    protocol.atomic_json(tmp_path / "analysis/capybara/calls/exact.json",{"response":"valid"})
    return tmp_path,config


def test_upgrade_audits_preserves_cache_and_is_idempotent(legacy):
    root,before=legacy
    checkpoint=root / "analysis/capybara/calls/exact.json"
    original=checkpoint.read_bytes()
    audit=migration.upgrade(root)
    assert audit["before"] == before
    assert audit["after"] == {**before,"marta_code":"new-code","summary_truncation_attempts":3}
    assert audit["checkpoint_count"] == 1
    assert json.loads((root/"experiment.json").read_text()) == audit["after"]
    assert migration.upgrade(root) == audit
    assert checkpoint.read_bytes() == original


@pytest.mark.parametrize("change",["unknown-code","task-started","export","empty-checkpoint"])
def test_upgrade_refuses_unrelated_or_generated_run(legacy, change):
    root,original=legacy
    if change == "unknown-code":
        protocol.atomic_json(root/"experiment.json",{**original,"marta_code":"different-code"})
    elif change == "task-started":
        protocol.atomic_json(root/"tasks/0/state.json",{"status":"running"})
    elif change == "export":
        (root/"processed.jsonl").write_text("{}\n")
    else:
        protocol.atomic_json(root/"analysis/capybara/calls/exact.json",{"response":""})
    before=(root/"experiment.json").read_bytes()
    with pytest.raises(ValueError):migration.upgrade(root)
    assert (root/"experiment.json").read_bytes() == before
    assert not (root/"summary_retry_upgrade.json").exists()


def test_upgrade_recovers_if_interrupted_after_audit(legacy, monkeypatch):
    root,original=legacy
    write=migration.atomic_json
    def interrupted(path,value):
        if path.name == "experiment.json":raise OSError("interrupted")
        write(path,value)
    monkeypatch.setattr(migration,"atomic_json",interrupted)
    with pytest.raises(OSError):migration.upgrade(root)
    assert json.loads((root/"experiment.json").read_text()) == original
    monkeypatch.setattr(migration,"atomic_json",write)
    audit=migration.upgrade(root)
    assert json.loads((root/"experiment.json").read_text()) == audit["after"]

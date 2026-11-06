"""Exact-prefix recovery: no resampling complete runs, no model usage for hits."""
import asyncio
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from marta.ruby_backend import project, start_react
from marta.ruby_backend.analysis_state import AnalysisArchive
from marta.ruby_backend.analysis_replay import AnalysisReplay, AnalysisRecoveryError
from marta.ruby_backend.tests.test_analysis_provenance import Client, make_project, analyze, needs_ruby


def snapshot(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def journal(tmp_path, responses=("first",), *, metadata=None):
    expected = metadata or {"fingerprint": "fixture", "analysis_order": ["id"]}
    archive = AnalysisArchive(tmp_path, use_cache=True, enrich=True)
    recorder = SimpleNamespace(fase_atual="phase", _contexto={"metodo": "C#x"})
    with pytest.raises(ConnectionError):
        with archive:
            archive.annotate(**expected)
            for response in responses:
                archive.request("system", "user", recorder, response=response)
            raise ConnectionError("interrupted fixture")
    return archive.root, expected, recorder


def test_prefix_preserves_duplicate_requests_and_different_recorded_answers(tmp_path):
    source, expected, recorder = journal(tmp_path, ("first", "second"))
    before = snapshot(source)
    replay = AnalysisReplay(source, expected)
    assert replay.take("system", "user", recorder)["response"] == "first"
    assert replay.take("system", "user", recorder)["response"] == "second"
    assert replay.take("system", "user", recorder) is None
    replay.verify_consumed()
    assert snapshot(source) == before


@pytest.mark.parametrize("change", ["system", "user", "phase", "context"])
def test_exact_request_order_and_context_are_required(tmp_path, change):
    source, expected, recorder = journal(tmp_path)
    replay = AnalysisReplay(source, expected)
    system, user = "system", "user"
    if change == "system": system = "different"
    if change == "user": user = "different"
    if change == "phase": recorder.fase_atual = "other"
    if change == "context": recorder._contexto = {"metodo": "D#x"}
    with pytest.raises(AnalysisRecoveryError, match="differs"):
        replay.take(system, user, recorder)
    with pytest.raises(AnalysisRecoveryError, match="before consuming"):
        replay.verify_consumed()


@pytest.mark.parametrize("change", ["response", "sequence", "accepted", "middle-json", "after-failure"])
def test_corrupt_complete_records_are_not_a_recovery_source(tmp_path, change):
    source, expected, _ = journal(tmp_path, ("first", "second"))
    path = source / "responses.jsonl"
    lines = path.read_text().splitlines()
    entry = json.loads(lines[0])
    if change == "response": entry["response"] = "edited answer"
    if change == "sequence": entry["sequence"] = 2
    if change == "accepted": entry.pop("response_accepted")
    if change == "middle-json": lines[0] = "broken JSON"
    elif change == "after-failure":
        entry.update(response="", response_accepted=False, response_sha256=None)
        lines[0] = json.dumps(entry)
    else: lines[0] = json.dumps(entry)
    path.write_text("\n".join(lines) + "\n")
    with pytest.raises(AnalysisRecoveryError, match="Malformed"):
        AnalysisReplay(source, expected)


def test_only_the_final_incomplete_record_can_be_discarded(tmp_path):
    source, expected, recorder = journal(tmp_path)
    with (source / "responses.jsonl").open("ab") as stream:
        stream.write(b'{"sequence":2')
    manifest = json.loads((source / "manifest.json").read_text())
    manifest.update(status="running", requests=0)  # Simulate a killed writer's stale manifest counter.
    (source / "manifest.json").write_text(json.dumps(manifest))
    replay = AnalysisReplay(source, expected)
    assert replay.take("system", "user", recorder)["response"] == "first"
    replay.verify_consumed()


def test_live_source_is_refused_and_lock_is_released_after_failure(tmp_path):
    archive = AnalysisArchive(tmp_path, use_cache=True, enrich=True)
    expected = {"fingerprint": "fixture"}
    with pytest.raises(ConnectionError):
        with archive:
            archive.annotate(**expected)
            with pytest.raises(AnalysisRecoveryError, match="writer"):
                AnalysisReplay(archive.root, expected)
            raise ConnectionError("stop")
    AnalysisReplay(archive.root, expected).verify_consumed()


@pytest.mark.parametrize("change", [{"status": "complete"}, {"archive_policy": "legacy"},
                                   {"use_cache": False}, {"fingerprint": "other"},
                                   {"error": {"type": "AnalysisRecoveryError"}}])
def test_complete_legacy_no_cache_and_incompatible_archives_are_refused(tmp_path, change):
    source, expected, _ = journal(tmp_path)
    path = source / "manifest.json"
    path.write_text(json.dumps(json.loads(path.read_text()) | change))
    with pytest.raises(AnalysisRecoveryError):
        AnalysisReplay(source, expected)


@pytest.fixture
def partial(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "provenance:test")
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib/calc.rb").write_text("class Calc; def a; 1; end; def b; 2; end; end")
    obj, client = make_project(tmp_path), Client()
    client.fail_at = 2
    with pytest.raises(ConnectionError):
        analyze(obj, client)
    return Path(obj.last_analysis_archive), client


@needs_ruby
def test_native_recovery_saves_the_accepted_call_and_records_only_fresh_usage(tmp_path, partial):
    source, client = partial
    before = snapshot(source)
    obj = make_project(tmp_path)
    destination, manifest = analyze(obj, client, resume_analysis=str(source))
    assert manifest["replayed_requests"] == 1
    assert manifest["requests"] == len(client.calls) - 2
    assert manifest["status"] == "complete" and not manifest["cache_hit"]
    rows = [json.loads(line) for line in (destination / "responses.jsonl").read_text().splitlines()]
    assert len(rows) == manifest["requests"] + manifest["replayed_requests"]
    assert rows[0]["replayed_from"] == {"archive": str(source), "sequence": 1}
    assert obj._recorder().score.por_fase["sumarios_passagem1"]["chamadas"] == 1  # Only method b.
    assert snapshot(source) == before
    calls = len(client.calls)
    _, cached = analyze(make_project(tmp_path), client)
    assert cached["cache_hit"] and len(client.calls) == calls


@needs_ruby
@pytest.mark.parametrize("change", ["source", "readme", "model", "order", "reference"])
def test_native_recovery_refuses_changed_inputs_before_any_new_request(tmp_path, partial, change):
    source, client = partial
    obj = make_project(tmp_path)
    kwargs = {}
    if change == "source":
        with (tmp_path / "lib/calc.rb").open("a") as stream: stream.write("\n# changed")
    if change == "readme": (tmp_path / "README.md").write_text("changed requirements")
    if change == "model": client.temperature = 0.8
    if change == "order": obj.analysis_targets.reverse()
    if change == "reference": kwargs["reaproveitar_passagem1_de"] = str(tmp_path / "other.json")
    with pytest.raises(AnalysisRecoveryError, match="differ"):
        analyze(obj, client, resume_analysis=str(source), **kwargs)
    assert len(client.calls) == 2
    assert not (Path(obj.last_analysis_archive) / "bundle.json").exists()


@needs_ruby
def test_recovery_can_itself_be_interrupted_without_losing_the_logical_prefix(tmp_path, partial):
    source, client = partial
    obj = make_project(tmp_path)
    client.fail_at = len(client.calls) + 2
    with pytest.raises(ConnectionError):
        analyze(obj, client, resume_analysis=str(source))
    second = Path(obj.last_analysis_archive)
    _, final = analyze(make_project(tmp_path), client, resume_analysis=str(second))
    assert final["replayed_requests"] == 2  # One inherited and one fresh successful response.
    assert final["recovery"]["source"] == str(second)


@needs_ruby
def test_no_cache_conflict_fails_before_reading_or_creating_an_archive(tmp_path):
    obj = make_project(tmp_path)
    with pytest.raises(ValueError, match="use_cache=False"):
        analyze(obj, Client(), use_cache=False, resume_analysis=str(tmp_path / "absent"))
    assert not (tmp_path / "run_results/analysis_runs").exists()


@pytest.mark.parametrize("flag", ["--no_cache", "--evaluate_only"])
def test_cli_rejects_conflicting_recovery_modes(monkeypatch, flag):
    monkeypatch.setattr("sys.argv", ["marta", "--project_path", ".", "--source_path", "lib",
                                    "--resume_analysis", "archive", flag])
    with pytest.raises(SystemExit) as error:
        start_react.main()
    assert error.value.code == 2


@needs_ruby
def test_cli_forwards_explicit_recovery_without_loading_a_model(tmp_path, monkeypatch):
    make_project(tmp_path)
    resume = AsyncMock()
    monkeypatch.setattr(project.RubyProject, "analyze_summaries", resume)
    monkeypatch.setattr(project.RubyProject, "generate_rounds", AsyncMock(return_value=[]))
    monkeypatch.setattr("sys.argv", ["marta", "--project_path", str(tmp_path), "--source_path", "lib",
                                    "--resume_analysis", "archive", "--no_rag"])
    start_react.main()
    assert resume.await_args.kwargs["resume_analysis"] == "archive"


@needs_ruby
def test_first_pass_reference_and_recovery_compose_without_repaying_source_summaries(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "provenance:test")
    normal, client = make_project(tmp_path), Client()
    analyze(normal, client)
    reference = normal._analysis_path("provenance:test", True)
    def ablated():
        return project.RubyProject(str(tmp_path), "lib", output_root=str(tmp_path / "ablated")).discover()
    obj = ablated()
    client.fail_at = len(client.calls) + 2
    with pytest.raises(ConnectionError):
        analyze(obj, client, enrich=False, reaproveitar_passagem1_de=reference)
    source = obj.last_analysis_archive
    resumed = ablated()
    _, result = analyze(resumed, client, enrich=False, reaproveitar_passagem1_de=reference,
                        resume_analysis=source)
    assert result["replayed_requests"] == 1
    assert resumed._recorder().score.por_fase["sumarios_passagem1"]["chamadas"] == 0


@needs_ruby
def test_no_cache_does_not_even_hash_an_explicit_first_pass_reference(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    reference = tmp_path / "reference.json"
    reference.write_text("not a reusable bundle")
    original = project.file_hash
    def guarded(path):
        assert Path(path) != reference, "no_cache must not read the reference"
        return original(path)
    monkeypatch.setattr(project, "file_hash", guarded)
    _, result = analyze(obj, Client(), use_cache=False, reaproveitar_passagem1_de=str(reference))
    assert result["status"] == "complete" and result["first_pass_reference"] is None


@needs_ruby
def test_failed_bundle_write_can_replay_the_whole_prefix_with_zero_new_requests(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "provenance:test")
    obj, client = make_project(tmp_path), Client()
    original = project.atomic_json
    def fail_bundle(path, data):
        if Path(path).name == "bundle.json": raise OSError("fixture disk error")
        return original(path, data)
    with monkeypatch.context() as scoped:
        scoped.setattr(project, "atomic_json", fail_bundle)
        with pytest.raises(OSError, match="disk error"):
            analyze(obj, client)
    source, calls = obj.last_analysis_archive, len(client.calls)
    _, manifest = analyze(make_project(tmp_path), client, resume_analysis=source)
    assert len(client.calls) == calls and manifest["requests"] == 0
    assert manifest["replayed_requests"] == calls and manifest["status"] == "complete"


@needs_ruby
def test_empty_analysis_response_is_not_replayed_as_a_success(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "provenance:test")
    class EmptyOnce(Client):
        async def aask(self, system, user):
            self.calls.append((system, user))
            return "" if len(self.calls) == 2 else "nonempty fixture summary"
    client = EmptyOnce()
    obj = make_project(tmp_path)
    with pytest.raises(project.AnalysisResponseError):
        analyze(obj, client)
    _, result = analyze(make_project(tmp_path), client, resume_analysis=obj.last_analysis_archive)
    assert result["replayed_requests"] == 1 and result["status"] == "complete"
    assert result["requests"] == len(client.calls) - 2


def test_interruption_during_prefix_replay_requires_the_intact_original_source(tmp_path):
    original, expected, recorder = journal(tmp_path, ("first", "second"))
    new = AnalysisArchive(tmp_path, use_cache=True, enrich=True)
    with pytest.raises(ConnectionError):
        with new:
            new.annotate(**expected)
            new.configure_replay(original, expected)
            entry = new.replay.take("system", "user", recorder)
            new.request("system", "user", recorder, response=entry["response"],
                        replayed_from={"archive": str(original), "sequence": entry["sequence"]})
            raise ConnectionError("interrupted before replaying the second response")
    with pytest.raises(AnalysisRecoveryError, match="original source"):
        AnalysisReplay(new.root, expected)
    assert AnalysisReplay(original, expected).audit["eligible_prefix"] == 2

"""Observable cache validity and persistent evidence; scripted clients only."""
import asyncio
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import analysis_state, cache, project, prompts, summaries
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok


class Client:
    model_type = "provenance:test"
    temperature = 0.2
    max_tokens = 512
    reasoning_effort = "high"
    top_p = 0.95
    presence_penalty = 0
    request_timeout = 500
    model_digest = "sha256:fixed-weights"

    def __init__(self, label="original"):
        self.calls = []
        self.label = label
        self.fail_at = None

    async def aask(self, system, user):
        self.calls.append((system, user))
        if len(self.calls) == self.fail_at:
            raise ConnectionError("fixture connection failure")
        return self.label + " summary"


def make_project(tmp_path):
    (tmp_path / "lib").mkdir(exist_ok=True)
    source = tmp_path / "lib/calc.rb"
    if not source.exists():
        source.write_text("class Calc\n  def add(a, b); a + b; end\nend\n")
    return project.RubyProject(str(tmp_path), "lib").discover()


def analyze(obj, client, **kwargs):
    asyncio.run(obj.analyze_summaries(ask=client.aask, **kwargs))
    root = Path(obj.last_analysis_archive)
    return root, json.loads((root / "manifest.json").read_text())


needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


@pytest.fixture(autouse=True)
def declared_model(monkeypatch):
    monkeypatch.setenv("MODEL", "provenance:test")


def test_provenance_never_loads_a_client_or_embedding_model(monkeypatch):
    monkeypatch.delitem(sys.modules, "marta.gptapi", raising=False)
    monkeypatch.delitem(sys.modules, "marta.embedding", raising=False)
    data = analysis_state.analysis_provenance()
    assert data["model"]["digest_status"] == "unavailable"
    assert data["client_parameters"] == {}
    assert "marta.gptapi" not in sys.modules and "marta.embedding" not in sys.modules
    assert cache.embedding_key("unloaded-provider")
    assert "marta.embedding" not in sys.modules


def test_client_configuration_has_no_api_key_or_rotating_endpoint(monkeypatch):
    client = Client()
    client.openai_api_key = "fixture-secret-key"
    client.openai_api_base = "http://secret-user:secret-pass@localhost:1001/v1?token=secret-token"
    first = analysis_state.analysis_provenance(client.aask)
    serialized = json.dumps(first)
    assert all(secret not in serialized for secret in
               ("fixture-secret-key", "secret-user", "secret-pass", "secret-token"))
    client.openai_api_base = "http://localhost:2002/v1"
    assert analysis_state.analysis_provenance(client.aask) == first


@needs_ruby
def test_cache_hit_gets_an_independent_archive_without_model_calls(tmp_path):
    obj, client = make_project(tmp_path), Client()
    first, initial = analyze(obj, client)
    assert initial["status"] == "complete" and not initial["cache_hit"]
    calls = len(client.calls)
    second, resumed = analyze(make_project(tmp_path), client)
    assert first != second and first.is_dir()
    assert resumed["cache_hit"] and resumed["requests"] == 0
    assert len(client.calls) == calls
    bundle = json.loads((second / "bundle.json").read_text())
    assert all(entry["summary"] == "original summary" for entry in bundle["targets"].values())
    assert bundle["provenance"]["model"]["digest"] == client.model_digest
    assert bundle["provenance"]["client_parameters"]["max_tokens"] == client.max_tokens
    assert not (second / "responses.jsonl").exists()


@needs_ruby
def test_no_cache_preserves_old_reusable_cache_and_archives_new_complete_results(tmp_path):
    obj, client = make_project(tmp_path), Client()
    first, _ = analyze(obj, client)
    reusable = Path(obj._analysis_path("provenance:test", True))
    before, modified = reusable.read_bytes(), reusable.stat().st_mtime_ns
    calls = len(client.calls)
    client.label = "fresh"
    second, manifest = analyze(make_project(tmp_path), client, use_cache=False)
    assert manifest["status"] == "complete" and not manifest["use_cache"] and not manifest["cache_hit"]
    assert len(client.calls) > calls
    assert reusable.read_bytes() == before and reusable.stat().st_mtime_ns == modified
    assert (first / "bundle.json").exists()
    fresh = json.loads((second / "bundle.json").read_text())
    assert all(entry["summary"] == "fresh summary" for entry in fresh["targets"].values())
    responses = [json.loads(line) for line in (second / "responses.jsonl").read_text().splitlines()]
    assert len(responses) == manifest["requests"] == len(client.calls) - calls
    assert all(row["response"] == "fresh summary" and len(row["request_sha256"]) == 64 for row in responses)
    resumed = make_project(tmp_path)
    before_resume = len(client.calls)
    _, manifest = analyze(resumed, client)
    assert manifest["cache_hit"] and len(client.calls) == before_resume
    assert resumed.targets[0].summary == "original summary"


@needs_ruby
def test_no_cache_on_fresh_output_writes_evidence_but_no_reusable_bundle(tmp_path):
    obj = make_project(tmp_path)
    root, manifest = analyze(obj, Client(), use_cache=False)
    assert manifest["status"] == "complete" and (root / "bundle.json").exists()
    assert not Path(obj._analysis_path("provenance:test", True)).exists()


@needs_ruby
def test_no_cache_also_ignores_explicit_source_only_reference(tmp_path):
    normal = make_project(tmp_path)
    client = Client()
    analyze(normal, client)
    other = make_project(tmp_path)
    _, manifest = analyze(other, client, use_cache=False, enrich=False,
        reaproveitar_passagem1_de=normal._analysis_path("provenance:test", True))
    assert manifest["status"] == "complete"
    assert other._recorder().score.por_fase["sumarios_passagem1"]["chamadas"] == 1


@needs_ruby
@pytest.mark.parametrize("field,value", [
    ("temperature", 0.7), ("max_tokens", 2048), ("reasoning_effort", "none"),
    ("top_p", 0.8), ("presence_penalty", 0.4), ("request_timeout", 900),
    ("model_digest", "sha256:different-weights"), ("model_type", "actual-other-model"),
])
def test_same_tag_different_effective_client_settings_cannot_reuse_summaries(tmp_path, field, value):
    client = Client()
    first, _ = analyze(make_project(tmp_path), client)
    before = len(client.calls)
    setattr(client, field, value)
    second, manifest = analyze(make_project(tmp_path), client)
    assert len(client.calls) > before and not manifest["cache_hit"]
    assert json.loads((first / "bundle.json").read_text())["fingerprint"] != json.loads((second / "bundle.json").read_text())["fingerprint"]


@needs_ruby
def test_changed_context_window_invalidates_but_generation_prompt_does_not(tmp_path, monkeypatch):
    client = Client()
    analyze(make_project(tmp_path), client)
    before = len(client.calls)
    monkeypatch.setattr(prompts, "DEV_SYS", "temporary generation-only instruction")
    _, manifest = analyze(make_project(tmp_path), client)
    assert len(client.calls) == before and manifest["cache_hit"]
    monkeypatch.setenv("OLLAMA_CTX", "65536")
    _, manifest = analyze(make_project(tmp_path), client)
    assert len(client.calls) > before and not manifest["cache_hit"]


@needs_ruby
def test_changed_analysis_prompt_automatically_invalidates_without_a_schema_bump(tmp_path, monkeypatch):
    client = Client()
    analyze(make_project(tmp_path), client)
    before, schema = len(client.calls), project.ANALYSIS_SCHEMA
    monkeypatch.setattr(summaries, "_SUMMARY_SYS", summaries._SUMMARY_SYS + " SPECIFIC_NEW_RULE")
    _, manifest = analyze(make_project(tmp_path), client)
    assert not manifest["cache_hit"] and len(client.calls) > before
    assert any("SPECIFIC_NEW_RULE" in system for system, _ in client.calls[before:])
    assert project.ANALYSIS_SCHEMA == schema


@needs_ruby
def test_failed_analysis_keeps_successful_responses_without_publishing_incomplete_cache(tmp_path):
    obj, client = make_project(tmp_path), Client()
    analyze(obj, client)
    cache_path = Path(obj._analysis_path("provenance:test", True))
    previous = cache_path.read_bytes()
    client.calls.clear()
    client.fail_at = 2
    failed = make_project(tmp_path)
    with pytest.raises(ConnectionError):
        analyze(failed, client, use_cache=False)
    root = Path(failed.last_analysis_archive)
    manifest = json.loads((root / "manifest.json").read_text())
    responses = [json.loads(line) for line in (root / "responses.jsonl").read_text().splitlines()]
    assert manifest["status"] == "failed" and manifest["requests"] == 2
    assert responses[0]["response"] == "original summary"
    assert responses[1]["error"]["type"] == "ConnectionError"
    assert not (root / "bundle.json").exists() and cache_path.read_bytes() == previous
    assert len(client.calls) == 2


@needs_ruby
def test_cancelled_analysis_is_archived_as_interrupted(tmp_path):
    obj = make_project(tmp_path)
    async def cancel(system, user):
        raise asyncio.CancelledError("fixture cancellation")
    with pytest.raises(asyncio.CancelledError):
        asyncio.run(obj.analyze_summaries(ask=cancel, use_cache=False))
    root = Path(obj.last_analysis_archive)
    manifest = json.loads((root / "manifest.json").read_text())
    assert manifest["status"] == "interrupted" and manifest["requests"] == 1
    assert not (root / "bundle.json").exists()


@needs_ruby
def test_default_client_is_resolved_before_env_and_provenance_capture(tmp_path, monkeypatch):
    monkeypatch.delenv("MODEL")
    client = Client()
    def default():
        monkeypatch.setenv("MODEL", "provenance:test")
        return client.aask
    monkeypatch.setattr(project, "_default_ask", default)
    obj = make_project(tmp_path)
    asyncio.run(obj.analyze_summaries())
    bundle = json.loads((Path(obj.last_analysis_archive) / "bundle.json").read_text())
    assert bundle["model"] == "provenance:test"
    assert bundle["provenance"]["model"]["configured_name"] == "provenance:test"
    assert bundle["provenance"]["client_parameters"]["temperature"] == client.temperature


def test_empty_analysis_still_has_a_complete_zero_request_archive(tmp_path):
    obj = project.RubyProject(str(tmp_path), "lib")
    client = Client()
    root, manifest = analyze(obj, client, use_cache=False)
    assert manifest["status"] == "complete" and manifest["requests"] == 0
    assert json.loads((root / "bundle.json").read_text())["targets"] == {}
    assert not client.calls


def test_embedding_keys_follow_local_metadata_declared_recipe_and_implementation(tmp_path, monkeypatch):
    model = tmp_path / "local-embedder"
    model.mkdir()
    config = model / "config.json"
    config.write_text('{"hidden_size": 4}')
    first = cache.vectors_key("sources", "llm", str(model))
    config.write_text('{"hidden_size": 8}')
    second = cache.vectors_key("sources", "llm", str(model))
    assert first != second
    monkeypatch.setenv("MARTA_EMBEDDING_RECIPE", "custom-pooling-v2")
    third = cache.vectors_key("sources", "llm", str(model))
    assert second != third
    original_hash = analysis_state.file_hash
    monkeypatch.setattr(analysis_state, "file_hash", lambda path:
        "changed-embedding-code" if Path(path).name == "embedding.py" else original_hash(path))
    assert cache.vectors_key("sources", "llm", str(model)) != third


def test_query_cache_rejects_a_changed_embedding_recipe(tmp_path, monkeypatch):
    from benchmark.xrepotest.reuse import ReferenceEmbeddings
    producer = Mock(return_value=[1.0, 2.0])
    monkeypatch.setitem(sys.modules, "marta.embedding", SimpleNamespace(embedder=SimpleNamespace(embed_query=producer)))
    path = tmp_path / "queries.json"
    bank = ReferenceEmbeddings({}, SimpleNamespace(evento=Mock()), path, "configured-embedder")
    assert bank.query("query") == [1.0, 2.0]
    monkeypatch.setenv("MARTA_EMBEDDING_RECIPE", "another-recipe")
    with pytest.raises(ValueError, match="Query embedding cache changed"):
        ReferenceEmbeddings({}, SimpleNamespace(evento=Mock()), path, "configured-embedder")
    assert producer.call_count == 1


@needs_ruby
@pytest.mark.parametrize("change", ["client", "source"])
def test_changed_inputs_during_analysis_cannot_publish_a_mixed_cache(tmp_path, change):
    obj, client = make_project(tmp_path), Client()
    original = client.aask
    async def mutate(system, user):
        response = await original(system, user)
        if len(client.calls) == 1:
            if change == "client":
                client.temperature = 0.8
            else:
                source = tmp_path / "lib/calc.rb"
                source.write_text(source.read_text() + "\n# edited while analyzing\n")
        return response
    wrapper_ask = mutate
    wrapper_ask.client = client
    with pytest.raises(project.AnalysisResponseError, match="changed"):
        asyncio.run(obj.analyze_summaries(ask=wrapper_ask))
    assert not Path(obj._analysis_path("provenance:test", True)).exists()
    archive = Path(obj.last_analysis_archive)
    assert json.loads((archive / "manifest.json").read_text())["status"] == "failed"
    assert (archive / "responses.jsonl").exists()

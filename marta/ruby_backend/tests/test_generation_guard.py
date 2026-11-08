"""Generation must not certify a recipe that changed while awaiting execution."""
import asyncio
import json
from unittest.mock import Mock
from pathlib import Path
from types import SimpleNamespace

import pytest

from marta.ruby_backend import project, recorder
from marta.ruby_backend.ablation import AblationOptions
from marta.ruby_backend.checkpoints import ResumeValidationError
from marta.ruby_backend.tests.test_generate import _make_project, PLAN_RESPONSE, GOOD_SPEC
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


@needs_ruby
@pytest.mark.parametrize("change", ["source", "client", "dependency", "digest", "loading", "invalid-env"])
def test_a_changed_recipe_cannot_be_certified_after_a_passing_round(tmp_path, monkeypatch, change):
    _make_project(tmp_path)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    client = SimpleNamespace(model_type="fixture", temperature=0.2, max_tokens=512, model_digest="sha256:declared-one")
    calls = []
    async def ask(system, user):
        calls.append(user)
        if len(calls) == 1:
            return PLAN_RESPONSE
        if change == "source":
            with (tmp_path / "src/calculator.rb").open("a") as stream: stream.write("# changed input\n")
        if change == "client": client.temperature = 0.8
        if change == "digest": client.model_digest = "sha256:declared-two"
        if change == "loading": obj.library_targets = ["future-component.rb"]
        if change == "invalid-env": monkeypatch.setenv("MARTA_GRAPH_CONTEXT", "invalid")
        if change == "dependency":
            folder = tmp_path / "component"; folder.mkdir()
            (folder / "Gemfile.lock").write_text("new pins")
        return GOOD_SPEC
    ask.client = client
    with pytest.raises(ResumeValidationError, match="Generation inputs or configuration changed"):
        asyncio.run(obj.generate_rounds(rounds=1, ask=ask))
    assert len(calls) == 2
    assert not (tmp_path / ".marta_generation/rounds.json").exists()
    assert not obj._all_spec_paths()
    assert list((tmp_path / "rejected_specs").rglob("*.rb"))


@needs_ruby
def test_boundary_guard_does_not_repeat_loading_probes_or_bind_service_ports(tmp_path, monkeypatch):
    _make_project(tmp_path)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    loading = Mock(wraps=obj._generation_loading_for)
    monkeypatch.setattr(obj, "_generation_loading_for", loading)
    client = SimpleNamespace(model_type="fixture", temperature=0.2, max_tokens=512,
                             model_digest="sha256:declared", openai_api_base="http://localhost:10001/v1")
    responses = iter([PLAN_RESPONSE, GOOD_SPEC])
    async def ask(system, user):
        client.openai_api_base = "http://localhost:10002/v1"
        return next(responses)
    ask.client = client
    assert asyncio.run(obj.generate_rounds(rounds=1, ask=ask))[0].success
    assert loading.call_count == 2  # Existing initial recipe + the actual generation request.
    state = json.loads((tmp_path / ".marta_generation/rounds.json").read_text())
    assert state["recipe"]["declared_model_digest"] == "sha256:declared"


@needs_ruby
@pytest.mark.parametrize("remove", [False, True])
def test_resume_revalidation_refuses_changes_without_calling_the_model(tmp_path, monkeypatch, remove):
    _make_project(tmp_path)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    obj.recorder = recorder.RubyRecorder(str(tmp_path / "events.jsonl"))
    replies, calls = iter([PLAN_RESPONSE, GOOD_SPEC]), []
    async def ask(system, user):
        calls.append(user)
        return next(replies)
    asyncio.run(obj.generate_rounds(rounds=1, ask=ask))
    ledger = tmp_path / ".marta_generation/rounds.json"
    before = ledger.read_bytes()
    original = obj._measure_retained_suite
    def change(outcomes, **kwargs):
        coverage = original(outcomes, **kwargs)
        source = tmp_path / "src/calculator.rb"
        if remove:
            source.unlink()
        else:
            with source.open("a") as stream: stream.write("# changed during revalidation\n")
        return coverage
    monkeypatch.setattr(obj, "_measure_retained_suite", change)
    with pytest.raises(ResumeValidationError, match="Generation inputs or configuration changed"):
        asyncio.run(obj.generate_rounds(rounds=2, ask=ask))
    assert len(calls) == 2 and ledger.read_bytes() == before and len(obj._all_spec_paths()) == 1
    events = [json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    event = next(e for e in events if e["tipo"] == "generation_inputs_changed")
    assert event["stage"] == "resume_revalidation"
    assert event["changed_fields"] == (["unreadable_or_invalid_inputs"] if remove else ["sources"])


@needs_ruby
def test_later_changed_round_archives_only_new_candidates_and_keeps_previous_checkpoint(tmp_path):
    _make_project(tmp_path)
    obj = project.RubyProject(str(tmp_path), "src", ablation_options=AblationOptions(no_coverage_feedback=True)).discover()
    client = SimpleNamespace(model_type="fixture", temperature=0.2, max_tokens=512)
    calls, replies = [], iter([PLAN_RESPONSE, GOOD_SPEC] * 2)
    ledger = tmp_path / ".marta_generation/rounds.json"
    saved = []
    async def ask(system, user):
        calls.append(user)
        if len(calls) == 4:
            saved.append(ledger.read_bytes())
            client.temperature = 0.7
        return next(replies)
    ask.client = client
    with pytest.raises(ResumeValidationError):
        asyncio.run(obj.generate_rounds(rounds=2, ask=ask))
    assert len(calls) == 4 and ledger.read_bytes() == saved[0]
    assert len(obj._all_spec_paths()) == 1
    assert len(list((tmp_path / "rejected_specs").rglob("*.rb"))) == 1


@needs_ruby
def test_direct_request_local_clients_bind_configuration_for_workers(tmp_path):
    from marta.ruby_backend.tests.test_generation_workers import Client, make
    class ChangingClient(Client):
        temperature = 0.2
        async def aask_result(self, system, user):
            reply = await super().aask_result(system, user)
            self.temperature = 0.8
            return reply
    obj = make(tmp_path)
    client = ChangingClient()
    with pytest.raises(ResumeValidationError):
        asyncio.run(obj.generate_rounds(rounds=1, ask=client))
    assert len(client.calls) == 4
    assert not (tmp_path / ".marta_generation/rounds.json").exists()
    assert not obj._all_spec_paths()

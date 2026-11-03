"""Offline failure/interruption regressions; real Ruby validation, no model server."""
import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import checkpoints, coverage_runner, project, recorder
from marta.ruby_backend.tests.test_generate import PLAN_RESPONSE, GOOD_SPEC, FAILING_SPEC, _make_project
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def make_project(tmp_path):
    if not (tmp_path / "src").exists():
        _make_project(tmp_path)
    return project.RubyProject(str(tmp_path), "src").discover()


def scripted(responses):
    queue = iter(responses)
    calls = []
    async def ask(system, user):
        calls.append((system, user))
        return next(queue)
    return ask, calls


def run_rounds(obj, ask, rounds=1):
    return asyncio.run(obj.generate_rounds(rounds=rounds, ask=ask, max_attempts=1))


def test_atomic_replace_failure_preserves_last_committed_file(tmp_path, monkeypatch):
    path = tmp_path / "spec.rb"
    path.write_text("previous complete bytes")
    def fail(*args):
        raise OSError("interrupted replace")
    monkeypatch.setattr(checkpoints.os, "replace", fail)
    with pytest.raises(OSError, match="interrupted"):
        checkpoints.atomic_write(path, "new bytes")
    assert path.read_text() == "previous complete bytes"
    assert list(tmp_path.iterdir()) == [path]


def test_second_writer_cannot_modify_same_output(tmp_path):
    first = checkpoints.RoundCheckpoints(tmp_path, {}, lambda **kw: None)
    second = checkpoints.RoundCheckpoints(tmp_path, {}, lambda **kw: None)
    with first.locked():
        with pytest.raises(checkpoints.ResumeValidationError, match="Another generation"):
            with second.locked():
                pytest.fail("second writer acquired the lock")
    with second.locked():
        pass


def test_offline_telemetry_does_not_import_or_initialize_a_model(monkeypatch):
    monkeypatch.delitem(sys.modules, "marta.gptapi", raising=False)
    async def ask(system, user):
        return "response"
    assert asyncio.run(recorder.token_tracking_ask(ask, recorder.RubyScore())("s", "u")) == "response"
    assert "marta.gptapi" not in sys.modules


@needs_ruby
@pytest.mark.parametrize("phase", ["sumarios_passagem1", "sumarios_passagem2", "what_todo_raiz",
                                    "what_todo_propagado", "sumario_final", "sumarios_de_classe"])
@pytest.mark.parametrize("bad_response", ["", "  \n", None, 42])
def test_empty_analysis_stops_after_one_bad_call_and_never_caches(tmp_path, phase, bad_response):
    (tmp_path / "src").mkdir()
    (tmp_path / "src/calc.rb").write_text("class Calc\n  def first(x); second(x); end\n  def second(x); x * 2; end\nend\n")
    obj = make_project(tmp_path)
    rec = obj._recorder()
    bad_calls = []
    async def ask(system, user):
        if rec.fase_atual == phase:
            bad_calls.append(user)
            return bad_response
        return "valid summary"
    with pytest.raises(project.AnalysisResponseError, match=phase):
        asyncio.run(obj.analyze_summaries(ask=ask))
    assert len(bad_calls) == 1  # Particularly: no propagation spin or hidden retry.
    assert not list((tmp_path / ".marta_ruby_cache").glob("analysis_*.json"))


@needs_ruby
def test_failed_reanalysis_preserves_prior_atomic_cache(tmp_path):
    obj = make_project(tmp_path)
    async def good(*args):
        return "valid summary"
    asyncio.run(obj.analyze_summaries(ask=good))
    # MODEL may already be set by the caller/test environment.
    import os
    path = Path(obj._analysis_path(os.getenv("MODEL", "default"), True))
    previous = path.read_bytes()
    async def empty(*args):
        return ""
    with pytest.raises(project.AnalysisResponseError):
        asyncio.run(obj.analyze_summaries(ask=empty, use_cache=False))
    assert path.read_bytes() == previous


@needs_ruby
def test_corrupt_empty_bundle_is_recomputed(tmp_path):
    import os
    obj = make_project(tmp_path)
    async def good(*args):
        return "valid summary"
    asyncio.run(obj.analyze_summaries(ask=good))
    path = Path(obj._analysis_path(os.getenv("MODEL", "default"), True))
    payload = json.loads(path.read_text())
    next(iter(payload["targets"].values()))["what_todo"] = " "
    path.write_text(json.dumps(payload))
    ask = Mock(side_effect=good)
    asyncio.run(obj.analyze_summaries(ask=ask))
    assert ask.called and all(t.what_todo == "valid summary" for t in obj.analysis_targets)


@needs_ruby
@pytest.mark.parametrize("old_spec", ["", "RSpec.describe('pending') { xit('later') {} }",
                                        "RSpec.describe('bad') { it('bad') { expect(1).to eq(2) } }"])
def test_an_uncommitted_file_is_archived_before_generation(tmp_path, old_spec):
    obj = make_project(tmp_path)
    path = tmp_path / obj.targets[0].spec_path_for_round(0)
    path.parent.mkdir(parents=True)
    path.write_text(old_spec)
    ask, calls = scripted([PLAN_RESPONSE, GOOD_SPEC])
    assert run_rounds(obj, ask)[0].success
    assert len(calls) == 2
    archived = list((tmp_path / "rejected_specs").rglob(path.name))
    assert len(archived) == 1 and archived[0].read_text() == old_spec
    assert obj.measure_coverage()[0].fully_covered


@needs_ruby
def test_terminal_failure_is_not_resampled_on_resume(tmp_path):
    obj = make_project(tmp_path)
    ask, calls = scripted([PLAN_RESPONSE, FAILING_SPEC])
    assert not run_rounds(obj, ask)[0].success
    assert len(calls) == 2
    fresh = make_project(tmp_path)
    forbidden, resumed_calls = scripted([])
    assert run_rounds(fresh, forbidden) == []
    assert not resumed_calls and fresh._all_spec_paths() == []
    state = json.loads((tmp_path / ".marta_generation/rounds.json").read_text())
    assert state["rounds"][0]["outcomes"][0]["success"] is False


@needs_ruby
def test_resume_revalidates_without_purchasing_another_attempt(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    ask, _ = scripted([PLAN_RESPONSE, GOOD_SPEC])
    run_rounds(obj, ask)
    fresh = make_project(tmp_path)
    validate = Mock(wraps=fresh.measure_coverage)
    monkeypatch.setattr(fresh, "measure_coverage", validate)
    forbidden, calls = scripted([])
    assert run_rounds(fresh, forbidden) == []
    validate.assert_called_once()
    assert not calls


@needs_ruby
def test_resume_failing_in_current_environment_stops_without_regeneration(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    ask, _ = scripted([PLAN_RESPONSE, GOOD_SPEC])
    run_rounds(obj, ask)
    fresh = make_project(tmp_path)
    monkeypatch.setattr(fresh, "measure_coverage", Mock(side_effect=coverage_runner.SuiteValidationError(None)))
    forbidden, calls = scripted([])
    with pytest.raises(coverage_runner.SuiteValidationError):
        run_rounds(fresh, forbidden)
    assert not calls and len(fresh._all_spec_paths()) == 1


@needs_ruby
@pytest.mark.parametrize("change", ["edited", "deleted"])
def test_changed_certified_output_requires_investigation(tmp_path, change):
    obj = make_project(tmp_path)
    ask, _ = scripted([PLAN_RESPONSE, GOOD_SPEC])
    run_rounds(obj, ask)
    path = tmp_path / obj.targets[0].spec_path_for_round(0)
    if change == "edited":
        path.write_text(path.read_text() + "\n# edited\n")
    else:
        path.unlink()
    forbidden, calls = scripted([])
    with pytest.raises(checkpoints.ResumeValidationError, match="changed or disappeared"):
        run_rounds(make_project(tmp_path), forbidden)
    assert not calls


@needs_ruby
@pytest.mark.parametrize("change", ["model", "tokens", "summary", "source", "options", "lockfile"])
def test_incompatible_generation_context_archives_old_output(tmp_path, monkeypatch, change):
    obj = make_project(tmp_path)
    ask, _ = scripted([PLAN_RESPONSE, GOOD_SPEC])
    run_rounds(obj, ask)
    fresh = make_project(tmp_path)
    if change == "model":
        monkeypatch.setenv("MODEL", "different-model")
    elif change == "tokens":
        monkeypatch.setenv("LLM_MAX_TOKENS", "3000")
    elif change == "summary":
        fresh.analysis_targets[0].summary = "different intent"
    elif change == "source":
        path = tmp_path / "src/calculator.rb"
        path.write_text(path.read_text() + "\n# new source\n")
        fresh = make_project(tmp_path)
    elif change == "options":
        from marta.ruby_backend.ablation import AblationOptions
        fresh.ablation_options = AblationOptions(no_type_hints=True)
    else:
        (tmp_path / "Gemfile.lock").write_text("different dependency pins")
    retry, calls = scripted([PLAN_RESPONSE, GOOD_SPEC])
    assert run_rounds(fresh, retry)[0].success
    assert len(calls) == 2 and list((tmp_path / "rejected_specs").rglob("rounds.json"))


@needs_ruby
def test_interrupted_round_keeps_completed_round_and_archives_only_uncommitted_spec(tmp_path):
    from marta.ruby_backend.ablation import AblationOptions
    obj = make_project(tmp_path)
    obj.ablation_options = AblationOptions(no_coverage_feedback=True)
    ask, _ = scripted([PLAN_RESPONSE, GOOD_SPEC])
    run_rounds(obj, ask)
    first = tmp_path / obj.targets[0].spec_path_for_round(0)
    previous = first.read_bytes()
    interrupted = tmp_path / obj.targets[0].spec_path_for_round(1)
    interrupted.write_text("interrupted garbage")
    fresh = make_project(tmp_path)
    fresh.ablation_options = obj.ablation_options
    retry, calls = scripted([PLAN_RESPONSE, GOOD_SPEC])
    outcomes = run_rounds(fresh, retry, rounds=2)
    assert len(outcomes) == 1 and outcomes[0].success and len(calls) == 2
    assert first.read_bytes() == previous
    archived = next((tmp_path / "rejected_specs").rglob(interrupted.name))
    assert archived.read_text() == "interrupted garbage"


@needs_ruby
def test_round_is_not_certified_when_suite_gate_is_interrupted(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    ask, _ = scripted([PLAN_RESPONSE, GOOD_SPEC])
    monkeypatch.setattr(obj, "_measure_retained_suite", Mock(side_effect=RuntimeError("interrupted gate")))
    with pytest.raises(RuntimeError, match="interrupted gate"):
        run_rounds(obj, ask)
    assert not (tmp_path / ".marta_generation/rounds.json").exists()
    assert obj._all_spec_paths()  # Preserved until next run archives uncommitted evidence.


@needs_ruby
def test_colliding_target_paths_are_rejected_before_any_request(tmp_path):
    (tmp_path / "src/a").mkdir(parents=True)
    (tmp_path / "src/b").mkdir()
    code = "class C; def x; 1; end; end"
    (tmp_path / "src/a/same.rb").write_text(code)
    (tmp_path / "src/b/same.rb").write_text(code)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    forbidden, calls = scripted([])
    with pytest.raises(ValueError, match="collide"):
        run_rounds(obj, forbidden)
    assert not calls


@needs_ruby
def test_client_settings_are_bound_but_service_port_is_not(tmp_path):
    client = SimpleNamespace(temperature=0.2, model_type="pinned-model", max_tokens=1000,
                             request_timeout=500, openai_api_base="http://localhost:10001/v1")
    async def ask(system, user):
        return PLAN_RESPONSE if "Test Plan" in system else GOOD_SPEC
    ask.client = client
    obj = make_project(tmp_path)
    run_rounds(obj, ask)
    client.openai_api_base = "http://localhost:10002/v1"
    assert run_rounds(make_project(tmp_path), ask) == []
    client.temperature = 0.7
    assert run_rounds(make_project(tmp_path), ask)[0].success
    assert list((tmp_path / "rejected_specs").rglob("rounds.json"))


def test_dependency_snapshot_prunes_installed_gems_and_archives(tmp_path):
    (tmp_path / "Gemfile").write_text("source")
    for directory in ("vendor", ".gem_home", "rejected_specs", "lib/component"):
        path = tmp_path / directory
        path.mkdir(parents=True)
        (path / "Gemfile.lock").write_text("pins")
    assert [str(Path(p).relative_to(tmp_path)) for p in checkpoints.dependency_files(tmp_path)] == [
        "Gemfile", "lib/component/Gemfile.lock"]


@needs_ruby
def test_empty_fallback_in_a_cycle_cannot_complete_analysis(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src/cycle.rb").write_text(
        "class Cycle\n  def a; b; end\n  def b; a; end\nend\n")
    obj = make_project(tmp_path)
    async def ask(system, user):
        return "" if obj._recorder().fase_atual == "what_todo_fallback" else "valid summary"
    with pytest.raises(project.AnalysisResponseError, match="what_todo_fallback"):
        asyncio.run(obj.analyze_summaries(ask=ask))
    assert not list((tmp_path / ".marta_ruby_cache").glob("analysis_*.json"))

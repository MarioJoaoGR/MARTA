"""Post-generation reports and observed costs; all model calls are forbidden."""
import asyncio
from dataclasses import asdict
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import evaluation, project, start_react
from marta.ruby_backend.coverage_runner import MethodCoverage
from marta.ruby_backend.recorder import RubyRecorder
from marta.ruby_backend.tests.test_generate import _make_project, GOOD_SPEC, PLAN_RESPONSE
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def make_project(tmp_path, spec=True, code=GOOD_SPEC):
    _make_project(tmp_path)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    if spec:
        from marta.ruby_backend.prompts import get_ruby_code
        path = tmp_path / obj.targets[0].spec_path_for_round(0)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(get_ruby_code(code))
    return obj


def test_macro_and_pooled_denominators_remain_explicit():
    rows = [{"mutation": {"valid": True, "mutation_score": 1.0, "counts": {"kills": 1, "mutations": 1}}},
            {"mutation": {"valid": True, "mutation_score": 0.0, "counts": {"kills": 0, "mutations": 9}}},
            {"mutation": {"valid": False, "mutation_score": None}}]
    result = evaluation.summarize_mutation(rows, True)
    assert result["ms_all_targets_zero_imputed"] == pytest.approx(1 / 3)
    assert result["ms_valid_only"] == 0.5 and result["pooled_diagnostic"] == 0.1
    assert rows[-1]["mutation"]["mutation_score"] is None
    assert evaluation.summarize_mutation(rows, False)["ms_all_targets_zero_imputed"] is None


def test_round_deltas_do_not_invent_missing_baselines_or_component_credit():
    t = SimpleNamespace(analysis_id="definition", task_id=None)
    first = MethodCoverage(covered_lines=3, executable_lines=5)
    second = MethodCoverage(covered_lines=2, executable_lines=5)
    start = dict(llm_calls=1, prompt_tokens=20, completion_tokens=10, llm_seconds=2)
    end = dict(llm_calls=3, prompt_tokens=50, completion_tokens=30, llm_seconds=5)
    unknown = evaluation.round_observation([(0, t)], {}, {0: first}, [], start, end, 4)
    assert unknown["targets"][0]["covered_line_delta"] is None
    known = evaluation.round_observation([(0, t)], {0: first}, {0: second}, [], start, end, 4)
    assert known["targets"][0]["covered_line_delta"] == -1
    assert known["new_cost"]["llm_calls"] == 2 and known["new_cost"]["prompt_tokens"] == 30
    changed = evaluation.round_observation([(0, t)], {0: first},
        {0: MethodCoverage(covered_lines=4, executable_lines=6)}, [], start, end, 4)
    assert changed["targets"][0]["covered_line_delta"] is None


def test_cost_snapshot_is_independent_and_only_current_process():
    recorder = RubyRecorder()
    recorder.score.add_llm_call(10, 3, fase="plano", segundos=2)
    first = evaluation.cost_snapshot(recorder)
    recorder.score.add_llm_call(20, 5, fase="plano", segundos=3)
    assert first["llm_calls"] == 1 and first["by_phase"]["plano"]["chamadas"] == 1
    assert first["scope"] == "current_recorder_process_only"


@needs_ruby
def test_core_evaluation_is_independent_preserves_originals_and_does_not_load_llm(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    original = {p: p.read_bytes() for p in tmp_path.rglob("*.rb")}
    monkeypatch.delitem(sys.modules, "marta.gptapi", raising=False)
    forbidden = Mock(side_effect=AssertionError("no LLM"))
    monkeypatch.setattr(obj, "analyze_summaries", forbidden)
    first = evaluation.evaluate_project(obj)
    data = json.loads(first.read_text())
    second = evaluation.evaluate_project(obj)
    assert first != second and first.exists()
    assert data["suite"]["valid"] and data["targets"][0]["coverage"]["invoked"] is True
    assert data["targets"][0]["coverage"]["covered_lines"] > 0
    assert data["generation_cost"] is None and not data["mutation"]["requested"]
    assert all(p.read_bytes() == content for p, content in original.items())
    assert "marta.gptapi" not in sys.modules
    forbidden.assert_not_called()


@needs_ruby
@pytest.mark.parametrize("situation", ["no_tests", "failing"])
def test_no_or_invalid_suites_are_not_valid_zero_mutation_measurements(tmp_path, monkeypatch, situation):
    obj = make_project(tmp_path, spec=situation != "no_tests", code=GOOD_SPEC.replace("eq(5)", "eq(999)"))
    executor = Mock(side_effect=AssertionError("do not mutate invalid suite"))
    monkeypatch.setattr(evaluation, "run_mutation", executor)
    path = evaluation.evaluate_project(obj, mutation=True, mutation_usage="opensource")
    report = json.loads(path.read_text())
    assert not report["suite"]["valid"]
    assert report["targets"][0]["mutation"]["mutation_score"] is None
    assert report["mutation"]["ms_all_targets_zero_imputed"] == 0
    executor.assert_not_called()


@needs_ruby
def test_mutation_gets_disposable_copy_and_frozen_suite(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    seen = []
    def mutate(identity, suite, repo, output, **kwargs):
        assert tmp_path not in repo.parents and repo != tmp_path
        assert identity["subject"] == "Calculator#add"
        assert suite.read_text().strip() == (tmp_path / obj.targets[0].spec_path_for_round(0)).read_text().strip()
        assert (repo / "src/calculator.rb").read_bytes() == (tmp_path / "src/calculator.rb").read_bytes()
        seen.append(repo)
        return {"valid": True, "mutation_score": 0.5, "status": "measured", "counts": {"kills": 1, "mutations": 2}}
    monkeypatch.setattr(evaluation, "run_mutation", mutate)
    path = evaluation.evaluate_project(obj, mutation=True, mutation_usage="opensource")
    assert json.loads(path.read_text())["mutation"]["ms_valid_only"] == 0.5
    assert seen and not seen[0].exists()


@needs_ruby
def test_input_change_prevents_complete_certificate(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    original = obj.backend.run_coverage
    def change(*args, **kwargs):
        result = original(*args, **kwargs)
        (tmp_path / "src/calculator.rb").write_text("class Changed; end\n")
        return result
    monkeypatch.setattr(obj.backend, "run_coverage", change)
    with pytest.raises(RuntimeError, match="inputs changed"):
        evaluation.evaluate_project(obj)
    manifests = list((tmp_path / "run_results/evaluations").glob("*/manifest.json"))
    assert json.loads(manifests[0].read_text())["status"] == "failed"
    assert not (manifests[0].parent / "report.json").exists()


@needs_ruby
def test_evaluate_only_cli_does_not_replace_generation_metrics_or_analyze(tmp_path, monkeypatch):
    obj = make_project(tmp_path)
    out = tmp_path / "run_results"
    out.mkdir()
    metrics, events = out / (tmp_path.name + ".json"), out / (tmp_path.name + ".eventos.jsonl")
    metrics.write_text("FROZEN METRICS")
    events.write_text("FROZEN EVENTS")
    monkeypatch.setattr(project.RubyProject, "analyze_summaries", Mock(side_effect=AssertionError("no analysis")))
    monkeypatch.setattr(project.RubyProject, "generate_rounds", Mock(side_effect=AssertionError("no generation")))
    monkeypatch.setattr(sys, "argv", ["marta", "--project_path", str(tmp_path), "--source_path", "src", "--evaluate_only"])
    start_react.main()
    assert metrics.read_text() == "FROZEN METRICS" and events.read_text() == "FROZEN EVENTS"
    reports = list(out.glob("evaluations/*/report.json"))
    assert len(reports) == 1 and json.loads(reports[0].read_text())["suite"]["valid"]


@needs_ruby
def test_round_utility_is_recorded_after_acceptance_without_extra_llm_requests(tmp_path):
    obj = make_project(tmp_path, spec=False)
    obj.recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    calls = []
    async def ask(system, user):
        calls.append(user)
        return PLAN_RESPONSE if "Test Plan" in system else GOOD_SPEC
    asyncio.run(obj.generate_rounds(ask=ask, rounds=2, max_attempts=1))
    events = [json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    rounds = [e for e in events if e["tipo"] == "round_utility"]
    assert len(calls) == 2 and len(rounds) == 2
    assert rounds[0]["targets"][0]["covered_line_delta"] is None
    assert rounds[1]["targets"][0]["covered_line_delta"] == 0
    assert rounds[0]["new_cost"]["llm_calls"] == 2 and rounds[1]["new_cost"]["llm_calls"] == 0


def test_missing_mutant_is_unavailable_without_baseline_or_installation(tmp_path, monkeypatch):
    from marta.ruby_backend import mutation
    (tmp_path / "box.rb").write_text("class Box; def x; 1; end; end\n")
    suite = tmp_path / "provided_spec.rb"
    suite.write_text("test placeholder")
    execute = Mock(return_value=("", "cannot load such file -- mutant", 1))
    baseline = Mock(side_effect=AssertionError("no baseline when engine missing"))
    monkeypatch.setattr(mutation, "execute", execute)
    monkeypatch.setattr(mutation, "run_rspec", baseline)
    result = mutation.run_mutation({"subject": "Box#x", "file": "box.rb", "start_line": 1, "end_line": 1},
        suite, tmp_path, tmp_path / "output", load_paths=[str(tmp_path)], usage="opensource")
    assert result["status"] == "unavailable" and result["mutation_score"] is None
    assert execute.call_count == 1
    baseline.assert_not_called()
    assert not (tmp_path / "mutant.yml").exists()


@needs_ruby
def test_cli_optional_evaluation_after_scripted_generation(tmp_path, monkeypatch):
    make_project(tmp_path, spec=False)
    monkeypatch.delitem(sys.modules, "marta.gptapi", raising=False)
    async def ask(system, user):
        if "Test Plan" in system:
            return PLAN_RESPONSE
        if "RSpec Expert" in system:
            return GOOD_SPEC
        return "valid analysis summary"
    monkeypatch.setattr(project, "_default_ask", lambda: ask)
    monkeypatch.setattr(sys, "argv", ["marta", "--project_path", str(tmp_path), "--source_path", "src",
                                     "--no_rag", "--num", "1", "--evaluate"])
    start_react.main()
    report = json.loads(next((tmp_path / "run_results/evaluations").glob("*/report.json")).read_text())
    assert report["suite"]["valid"]
    assert report["generation_cost"]["scope"] == "current_recorder_process_only"
    assert report["generation_cost"]["llm_calls"] > 0
    assert "marta.gptapi" not in sys.modules


def test_cli_requires_mutation_usage_before_any_generation(monkeypatch):
    monkeypatch.setattr(project.RubyProject, "discover", Mock(side_effect=AssertionError("no discovery")))
    monkeypatch.setattr(sys, "argv", ["marta", "--project_path", "/unused", "--source_path", "src", "--mutation"])
    with pytest.raises(SystemExit) as error:
        start_react.main()
    assert error.value.code == 2

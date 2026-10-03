"""Component isolation and default-equivalence without live model calls."""
import argparse
import asyncio
import importlib.util
import os
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import project
from marta.ruby_backend.ablation import AblationOptions, add_arguments, from_args
from marta.ruby_backend.tests.test_generate import (PLAN_RESPONSE, BROKEN_SPEC, GOOD_SPEC,
                                                  _make_project)


def test_cli_defaults_are_all_off_and_flags_are_independent():
    parser = argparse.ArgumentParser()
    add_arguments(parser, underscores=True)
    assert from_args(parser.parse_args([])) == AblationOptions()
    for name in AblationOptions.__dataclass_fields__:
        options = from_args(parser.parse_args(["--" + name.replace("_", "-")]))
        assert options.enabled and options.as_dict()[name]
        assert sum(options.as_dict().values()) == 1


def test_type_ablation_omits_hints_without_erasing_the_graph_index(tmp_path):
    target = SimpleNamespace(summary="local summary", planner_summary="local summary TYPE_HINT")
    index = object()
    normal = project.RubyProject(str(tmp_path), "lib", type_index=index)
    ablated = project.RubyProject(str(tmp_path), "lib", type_index=index,
                                 ablation_options=AblationOptions(no_type_hints=True))
    assert normal._planner_summary(target) == "local summary TYPE_HINT"
    assert ablated._planner_summary(target) == "local summary"
    assert ablated.type_index is index


def test_retrieval_ablation_cannot_leak_through_previously_loaded_vectors(tmp_path):
    database = Mock()
    database.related_lines.return_value = ["Helper: retrieved"]
    target = SimpleNamespace(summary="summary", done_what="plain", analysis_id="id")
    normal = project.RubyProject(str(tmp_path), "lib", rag_db=database)
    assert normal._related_for(target) == ["Helper: retrieved"]
    assert normal._error_help_fn(target) is not None
    database.reset_mock()
    normal.ablation_options = AblationOptions(no_method_retrieval=True)
    assert normal._related_for(target) is None
    assert normal._error_help_fn(target) is None
    database.query.assert_not_called()
    database.related_lines.assert_not_called()


@pytest.mark.parametrize("options,functions,classes", [
    (AblationOptions(), True, True),
    (AblationOptions(no_type_hints=True), True, False),
    (AblationOptions(no_method_retrieval=True), False, True),
    (AblationOptions(no_type_hints=True, no_method_retrieval=True), False, False),
])
def test_method_retrieval_and_semantic_type_hints_use_independent_indexes(
        tmp_path, monkeypatch, options, functions, classes):
    method_index = Mock()
    class_index = Mock()
    monkeypatch.setattr(project, "_AnalysisFunctionDatabase", Mock(return_value=method_index))
    monkeypatch.setattr(project.rag, "RubyClassIndex", Mock(return_value=class_index))
    obj = project.RubyProject(str(tmp_path), "lib", ablation_options=options,
                              class_summaries={"Helper": "helper class"})
    augment = Mock()
    monkeypatch.setattr(obj, "_augment_judge_semantic", augment)
    obj.build_rag(embed_documents=lambda docs: [], embed_query=lambda query: [], persist=False)
    assert (obj.rag_db is method_index) is functions
    assert (obj.class_db is class_index) is classes
    assert augment.called is classes


def _run_project(tmp_path, cls=project.RubyProject, options=None, responses=None, fully_covered=True):
    root = _make_project(tmp_path) if not (tmp_path / "src").exists() else tmp_path
    obj = cls(root_dir=str(root), source_dir="src").discover()
    if options is not None:
        obj.ablation_options = options
    obj.targets[0].summary = "Adds values"
    obj.targets[0].judge = "PARAMETER TYPE: Numeric"
    prompts, queue = [], list(responses or [PLAN_RESPONSE, GOOD_SPEC])
    async def ask(system, user):
        prompts.append((system, user))
        return queue.pop(0)
    measured = []
    def coverage():
        measured.append(True)
        return ({0: SimpleNamespace(fully_covered=fully_covered, covered_lines=[2],
                                   format_missing_lines=lambda: "SECRET_MISSING")}
                if list((root / "marta_specs").glob("*.rb")) else {})
    obj.measure_coverage = coverage
    outcome = asyncio.run(obj.generate_rounds(rounds=3, max_attempts=3, ask=ask))
    files = {p.name: p.read_text() for p in (root / "marta_specs").glob("*.rb")}
    return obj, prompts, outcome, measured, files


def test_without_coverage_feedback_all_rounds_run_even_after_full_coverage(tmp_path):
    responses = [PLAN_RESPONSE, GOOD_SPEC] * 3
    obj, prompts, outcomes, measured, files = _run_project(tmp_path,
        options=AblationOptions(no_coverage_feedback=True), responses=responses)
    assert len(outcomes) == 3 and len(measured) == 3 and len(files) == 3
    assert not any("MISSING LINES TO COVER:" in user or "SECRET_MISSING" in user for _, user in prompts)
    assert sum("PARAMETER TYPE: Numeric" in user for _, user in prompts) == 3


@pytest.mark.parametrize("disabled", [False, True])
def test_coverage_feedback_only_controls_specific_missing_lines(tmp_path, disabled):
    _, prompts, outcomes, _, _ = _run_project(tmp_path,
        options=AblationOptions(no_coverage_feedback=disabled),
        responses=[PLAN_RESPONSE, GOOD_SPEC] * 3, fully_covered=False)
    assert len(outcomes) == 3
    feedback = [user for _, user in prompts if "SECRET_MISSING" in user]
    assert len(feedback) == (0 if disabled else 2)


def test_no_repair_still_validates_but_never_asks_for_another_dev_attempt(tmp_path):
    obj, prompts, outcomes, _, files = _run_project(tmp_path,
        options=AblationOptions(no_repair=True), responses=[PLAN_RESPONSE, BROKEN_SPEC] * 3)
    assert len(prompts) == 6 and len(outcomes) == 3
    assert all(o.attempts == 1 and not o.success for o in outcomes)
    assert not files


def test_normal_repair_and_coverage_skip_are_unchanged(tmp_path):
    _, prompts, outcomes, measured, files = _run_project(tmp_path,
        responses=[PLAN_RESPONSE, BROKEN_SPEC, GOOD_SPEC])
    assert len(prompts) == 3 and outcomes[0].attempts == 2 and outcomes[0].success
    assert len(outcomes) == 1 and len(files) == 1 and len(measured) == 3


def test_default_prompts_calls_specs_and_results_match_the_frozen_project(tmp_path):
    baseline = os.getenv("MARTA_BASELINE_PROJECT")
    if not baseline:
        pytest.skip("Set MARTA_BASELINE_PROJECT to the frozen project.py for equivalence verification")
    name = "marta.ruby_backend._frozen_project"
    spec = importlib.util.spec_from_file_location(name, baseline)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    # Same source and output paths keep literal prompts and require strings identical.
    responses = [PLAN_RESPONSE, BROKEN_SPEC, GOOD_SPEC]
    before = _run_project(tmp_path, cls=module.RubyProject, responses=responses)
    import shutil
    shutil.rmtree(tmp_path / "marta_specs")
    after = _run_project(tmp_path, responses=responses)
    assert before[1] == after[1]
    assert [(o.success, o.attempts, o.salvaged, o.results) for o in before[2]] == [
        (o.success, o.attempts, o.salvaged, o.results) for o in after[2]]
    assert before[3:] == after[3:]


@pytest.mark.parametrize('has_spec', [True, False])
def test_shared_first_round_only_generates_later_rounds_even_after_a_failed_seed(tmp_path, has_spec):
    root = _make_project(tmp_path)
    obj = project.RubyProject(str(root), 'src',
        ablation_options=AblationOptions(no_coverage_feedback=True)).discover()
    target = obj.targets[0]
    spec = Path(target.spec_path_for_round(0))
    if not spec.is_absolute(): spec = root/spec
    if has_spec:
        spec.parent.mkdir(parents=True, exist_ok=True)
        spec.write_text(GOOD_SPEC)
    before = spec.read_bytes() if has_spec else None
    calls = []
    queue = [PLAN_RESPONSE, GOOD_SPEC]*2
    async def ask(system, user):
        calls.append(obj._recorder()._contexto['ronda'])
        return queue.pop(0)
    obj.measure_coverage = Mock(return_value={0:SimpleNamespace(fully_covered=True, covered_lines=[2])})
    outcomes = asyncio.run(obj.generate_rounds(3, ask=ask, reuse_first_round=True))
    assert calls == [1,1,2,2] and len(outcomes)==2
    assert obj.measure_coverage.call_count==3
    assert (spec.read_bytes() if has_spec else None)==before
    if not has_spec: assert not spec.exists()


def test_default_tool_refuses_unscoped_round_reuse(tmp_path):
    obj = project.RubyProject(str(_make_project(tmp_path)), 'src').discover()
    with pytest.raises(ValueError, match='coverage-ablation'):
        asyncio.run(obj.generate_rounds(reuse_first_round=True))


def test_normal_and_coverage_ablation_have_identical_first_round_prompts(tmp_path):
    import shutil
    before = _run_project(tmp_path, responses=[PLAN_RESPONSE, GOOD_SPEC]*3, fully_covered=False)
    shutil.rmtree(tmp_path/'marta_specs')
    after = _run_project(tmp_path, options=AblationOptions(no_coverage_feedback=True),
                         responses=[PLAN_RESPONSE, GOOD_SPEC]*3, fully_covered=False)
    assert before[1][:2] == after[1][:2]
    assert before[4][next(name for name in before[4] if '_r0_' in name)] == after[4][
        next(name for name in after[4] if '_r0_' in name)]

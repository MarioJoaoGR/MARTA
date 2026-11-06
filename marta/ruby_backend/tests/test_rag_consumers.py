"""Consumer-level retrieval removal without models or downloaded vectors."""
import asyncio
import itertools
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import project
from marta.ruby_backend.ablation import AblationOptions
from marta.ruby_backend.tests.test_generate import _make_project, PLAN_RESPONSE, BROKEN_SPEC, GOOD_SPEC
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok


FLAGS = ("no_planner_retrieval", "no_error_retrieval", "no_semantic_judge")


@pytest.mark.parametrize("disabled", itertools.product((False, True), repeat=3))
def test_only_required_indexes_are_built_and_consumers_are_independent(tmp_path, monkeypatch, disabled):
    options = AblationOptions(**dict(zip(FLAGS, disabled)))
    db = Mock()
    db.related_lines.return_value = ["PLANNER_RETRIEVED_METHOD"]
    db.query.return_value = []
    function_factory = Mock(return_value=db)
    class_factory = Mock()
    monkeypatch.setattr(project, "_AnalysisFunctionDatabase", function_factory)
    monkeypatch.setattr(project.rag, "RubyClassIndex", class_factory)
    obj = project.RubyProject(str(tmp_path), "src", ablation_options=options,
                              class_summaries={"Helper": "helper class"})
    semantic = Mock()
    monkeypatch.setattr(obj, "_augment_judge_semantic", semantic)
    obj.build_rag(embed_documents=lambda docs: [], embed_query=lambda q: [], persist=False)
    target = SimpleNamespace(summary="summary", done_what="", analysis_id="id")
    planner, error, judge = (not value for value in disabled)
    assert function_factory.call_count == int(planner or error)
    assert class_factory.call_count == int(judge)
    assert semantic.called is judge
    assert obj._related_for(target) == (["PLANNER_RETRIEVED_METHOD"] if planner else None)
    helper = obj._error_help_fn(target)
    assert (helper is not None) is error
    if helper:
        assert helper("an observed failure") == ""
    assert db.related_lines.call_count == int(planner)
    assert db.query.call_count == int(error)


@pytest.mark.parametrize("name", FLAGS)
def test_legacy_flags_dominate_consumer_options(tmp_path, name):
    options = AblationOptions(no_method_retrieval=True, no_type_hints=True, **{name: True})
    obj = project.RubyProject(str(tmp_path), "src", rag_db=Mock(), ablation_options=options)
    assert obj._related_for(SimpleNamespace()) is None
    assert obj._error_help_fn(SimpleNamespace()) is None
    assert not options.method_index_enabled and not options.semantic_judge_enabled
    obj.rag_db.query.assert_not_called()
    obj.rag_db.related_lines.assert_not_called()


def test_disabling_planner_clears_saved_context_but_repair_remains_live(tmp_path):
    db = Mock()
    db.retrieval_revision = "revision"
    db.related_lines.return_value = ["OLD_PLANNER"]
    db.query.return_value = []
    obj = project.RubyProject(str(tmp_path), "src", rag_db=db)
    target = SimpleNamespace(summary="summary", done_what="", analysis_id="id")
    assert obj._related_for(target) == ["OLD_PLANNER"]
    obj.ablation_options = AblationOptions(no_planner_retrieval=True)
    assert obj._related_for(target) is None
    obj._error_help_fn(target)("failure")
    obj.ablation_options = AblationOptions()
    obj._related_for(target)
    assert db.related_lines.call_count == 2 and db.query.call_count == 1


@pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/Prism toolchain")
def test_no_semantic_judge_resets_old_choices_and_retains_structural_hints(tmp_path, monkeypatch):
    obj = project.RubyProject(str(_make_project(tmp_path)), "src").discover()
    t = obj.analysis_targets[0]
    t.method.param_members = {"a": ["add"]}
    structural = obj.type_index.judge_for_method(t.method)
    assert structural
    obj.class_summaries = {"Calculator": "adds values"}
    t.summary = "BASE_SUMMARY"
    t.judge = structural + "\nSTALE_SEMANTIC_CHOICE"
    obj.class_db = Mock()
    obj.judge_decisions = {t.analysis_id: {"old": "choice"}}
    functions = Mock()
    monkeypatch.setattr(project, "_AnalysisFunctionDatabase", Mock(return_value=functions))
    classes = Mock(side_effect=AssertionError("disabled class index must not be built"))
    monkeypatch.setattr(project.rag, "RubyClassIndex", classes)
    obj.ablation_options = AblationOptions(no_semantic_judge=True)
    obj.build_rag(persist=False)
    assert obj.class_db is None and obj.rag_db is functions and obj.judge_decisions == {}
    assert t.judge == structural
    assert "BASE_SUMMARY" in obj._planner_summary(t) and structural in obj._planner_summary(t)
    assert "STALE_SEMANTIC_CHOICE" not in obj._planner_summary(t)
    assert obj.type_index is not None  # Graph/structural typing survives.


@pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")
@pytest.mark.parametrize("options,planner,error", [
    (AblationOptions(), True, True),
    (AblationOptions(no_planner_retrieval=True), False, True),
    (AblationOptions(no_error_retrieval=True), True, False),
    (AblationOptions(no_semantic_judge=True), True, True),
    (AblationOptions(no_method_retrieval=True), False, False),
])
def test_real_generation_prompts_remove_only_the_selected_retrieved_context(
        tmp_path, options, planner, error):
    root = _make_project(tmp_path)
    obj = project.RubyProject(str(root), "src", ablation_options=options).discover()
    obj.targets[0].summary = "BASE_SUMMARY"
    db = Mock()
    db.related_lines.return_value = ["PLANNER_ONLY_MARKER"]
    db.query.return_value = [SimpleNamespace(done_what="REPAIR_ONLY_MARKER", summary="",
                                           method=SimpleNamespace(qualified_name="Helper#run"))]
    obj.rag_db = db
    obj._example_passing_spec = Mock(return_value=None)
    obj.measure_coverage = Mock(return_value={})
    seen, responses = [], iter([PLAN_RESPONSE, BROKEN_SPEC, GOOD_SPEC])
    async def ask(system, user):
        seen.append(user)
        return next(responses)
    outcomes = asyncio.run(obj.generate_rounds(rounds=1, ask=ask))
    assert outcomes[0].success and len(seen) == 3
    assert ("PLANNER_ONLY_MARKER" in seen[0]) is planner
    assert "BASE_SUMMARY" in seen[0]
    assert ("REPAIR_ONLY_MARKER" in seen[2]) is error
    assert "CURRENT FAILURE:" in seen[2] and "ORIGINAL TEST PLAN:" in seen[2]
    assert "syntax error: unclosed" in seen[2]  # Previous broken test survives.
    assert db.related_lines.call_count == int(planner)
    assert db.query.call_count == int(error)


@pytest.mark.parametrize("name", FLAGS)
def test_new_ablations_cannot_reuse_a_normal_first_round(tmp_path, name):
    obj = project.RubyProject(str(tmp_path), "src", targets=[SimpleNamespace()],
        ablation_options=AblationOptions(no_coverage_feedback=True, **{name: True}))
    with pytest.raises(ValueError, match="coverage-ablation"):
        asyncio.run(obj.generate_rounds(reuse_first_round=True))

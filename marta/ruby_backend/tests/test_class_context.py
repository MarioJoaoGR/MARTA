"""Class evidence packing and offline analysis integration; no live LLM."""
import asyncio
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marta.ruby_backend import analysis_state, class_context, project, recorder, summaries
from marta.ruby_backend.prompt_budget import PromptBudget, PromptBudgetExceeded
from marta.ruby_backend.ruby_ast import ClassInfo, MethodInfo, ParamInfo
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/Prism toolchain")


def target(root, name, *, filename="lib/box.rb", line=2, singleton=False, params=()):
    method = MethodInfo(name, "Box", singleton, line, line+2, list(params))
    return SimpleNamespace(method=method, file_path=str(root / filename),
                           analysis_id=f"{filename}:{method.qualified_name}:{line}")


def definition(root, *, filename="lib/box.rb", line=1, parent=None, statements=()):
    return (str(root / filename), ClassInfo("Box", "Box", "class", parent,
                                          line, line+100, body_statements=list(statements)))


def build(root, targets, descriptions=None, definitions=None, limit=6000):
    return class_context.build_class_context("Box", definitions or [definition(root)], targets,
        descriptions or {}, root=str(root), limit=limit)


def test_reuses_behavior_and_parser_facts_without_reading_sources(tmp_path, monkeypatch):
    ctor = target(tmp_path, "initialize", params=[ParamInfo("value", "req")])
    method = target(tmp_path, "fetch", line=10, params=[ParamInfo("fallback", "opt")])
    forbidden = Mock(side_effect=AssertionError("must reuse in-memory evidence"))
    monkeypatch.setattr(Path, "open", forbidden)
    view = build(tmp_path, [method, ctor], {ctor.analysis_id: "Stores the given value.",
        method.analysis_id: "Returns the stored value, falling back when absent."},
        [definition(tmp_path, parent="Base", statements=['attr_reader :value', 'include Helpful'])])
    assert "Box#initialize" in view.text and "value [req]" in view.text
    assert "fallback [opt]" in view.text
    assert "Stores the given value" in view.text and "falling back" in view.text
    assert "class Box < Base" in view.text and "include Helpful" in view.text
    assert view.text.index("Box#initialize") < view.text.index("Box#fetch")
    assert view.metadata["method_descriptions"] == 2
    assert view.metadata["prepared_chars"] == len(view.text) <= 6000
    forbidden.assert_not_called()


def test_all_methods_considered_without_a_first_forty_cap(tmp_path):
    targets = [target(tmp_path, f"method_{n}", line=3*n+1) for n in range(65)]
    view = build(tmp_path, targets, limit=30000)
    assert view.metadata["prepared"]["methods"] == 65
    assert "Box#method_64" in view.text
    assert view.metadata["omitted"]["methods"] == 0


def test_reopened_declarations_remain_distinct_and_input_order_does_not_matter(tmp_path):
    a = target(tmp_path, "work", line=3)
    b = target(tmp_path, "work", filename="lib/extension.rb", line=7)
    definitions = [definition(tmp_path, parent="Parent"),
                   definition(tmp_path, filename="lib/extension.rb", statements=['FLAG = true'])]
    descriptions = {a.analysis_id: "Original behavior.", b.analysis_id: "Reopened behavior."}
    before = build(tmp_path, [a, b], descriptions, definitions)
    after = build(tmp_path, [b, a], descriptions, list(reversed(definitions)))
    assert before == after
    assert before.metadata["available"]["declarations"] == 2
    assert before.text.count("Method Box#work") == 2
    assert "runtime winner" in before.core
    assert "Original behavior" in before.text and "Reopened behavior" in before.text


def test_methods_from_other_files_get_considered_before_second_same_file_method(tmp_path):
    a = target(tmp_path, "a", filename="lib/a.rb", line=2)
    b = target(tmp_path, "b", filename="lib/a.rb", line=10)
    c = target(tmp_path, "c", filename="lib/z.rb", line=2)
    view = build(tmp_path, [b, c, a])
    assert view.text.index("Box#a") < view.text.index("Box#c") < view.text.index("Box#b")


def test_large_statement_does_not_block_later_small_statements(tmp_path):
    view = build(tmp_path, [], definitions=[definition(tmp_path, statements=[
        'CONFIG = "' + "x"*20000 + '"', 'attr_reader :value'])], limit=1000)
    assert 'CONFIG = "' not in view.text and 'attr_reader :value' in view.text
    assert view.metadata["omitted"]["statements"] == 1
    assert len(view.text) <= 1000


def test_verbose_summaries_are_labelled_excerpts_not_more_llm_requests(tmp_path):
    method = target(tmp_path, "long")
    view = build(tmp_path, [method], {method.analysis_id: "description " * 2000})
    assert "incomplete excerpt" in view.text
    assert view.metadata["method_descriptions"] == 1
    assert len(view.text) < 1500


def test_long_description_can_fall_back_to_intact_facts(tmp_path):
    method = target(tmp_path, "short")
    view = build(tmp_path, [method], {method.analysis_id: "description " * 2000}, limit=650)
    assert "Method Box#short" in view.text
    assert "Generated source-only" not in view.text
    assert view.metadata["prepared"]["methods"] == 1
    assert view.metadata["method_descriptions"] == 0
    assert len(view.text) <= 650


def test_missing_description_does_not_invent_behavior_defaults_or_visibility(tmp_path):
    method = target(tmp_path, "make", singleton=True, params=[ParamInfo(None, "rest")])
    view = build(tmp_path, [method])
    assert "Box.make" in view.text and "<unnamed> [rest]" in view.text
    assert "Generated source-only" not in view.text
    assert "Defaults/visibility not inferred" in view.text


@pytest.mark.parametrize("limit", [0, -1, True, 1.5])
def test_invalid_local_limits_fail(limit, tmp_path):
    with pytest.raises(ValueError, match="positive integer"):
        build(tmp_path, [], limit=limit)


def test_tiny_local_budget_retains_identity_and_reports_oversized_core(tmp_path):
    view = build(tmp_path, [target(tmp_path, "m")], limit=1)
    assert "CLASS: Box" in view.core and not view.records
    assert view.metadata["prepared_chars"] > 1
    assert view.metadata["omitted"]["methods"] == 1


def char_counter(system, user):
    return len(system) + len(user)


def test_whole_prompt_budget_reduces_complete_records_not_class_identity():
    seen = []
    async def ask(system, user):
        seen.append((system, user))
        return "summary"
    evidence = ["RECORD_A " + "x"*100, "RECORD_B " + "y"*600, "RECORD_C " + "z"*600]
    budget = PromptBudget(1800, 100, 0, counter=char_counter)
    result = asyncio.run(summaries.analyze_class(ask, "CLASS: Box", class_evidence=evidence, budget=budget))
    assert result == "summary" and len(seen) == 1
    system, user = seen[0]
    assert "CLASS: Box" in user and len(system) + len(user) <= 1700
    assert "RECORD_A " + "x"*100 in user
    assert "RECORD_C" not in user
    for record in evidence:
        if record.split()[0] in user:
            assert record in user  # A retained record is complete, not a sliced string.
    assert "Do not invent" in system


def test_mandatory_identity_overflow_stops_before_any_model_request():
    ask = Mock(side_effect=AssertionError("must not request"))
    with pytest.raises(PromptBudgetExceeded):
        asyncio.run(summaries.analyze_class(ask, "CLASS: " + "x"*3000,
            class_evidence=["optional"], budget=PromptBudget(1500, 100, 0, counter=char_counter)))
    ask.assert_not_called()


def test_provenance_identifies_class_policy_and_builder():
    data = analysis_state.analysis_provenance()
    assert data["class_context_policy"] == class_context.POLICY
    assert len(data["implementation"]["class_context.py"]) == 64


@needs_ruby
def test_pipeline_uses_existing_source_only_summaries_and_same_class_call_count(tmp_path, monkeypatch):
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib/parcel.rb").write_text('''class Parcel
  attr_reader :value
  def initialize(value)
    @value = value
  end
  def get
    @value
  end
  def twice
    get * 2
  end
end
class Unused
  FLAG = true
end
''')
    monkeypatch.setenv("MODEL", "class-context-offline-fixture")
    obj = project.RubyProject(str(tmp_path), "lib").discover()
    assert set(obj._class_definitions) == {"Parcel"}
    obj.recorder = recorder.RubyRecorder(str(tmp_path / "events.jsonl"))
    seen = []
    async def ask(system, user):
        phase = obj.recorder.fase_atual
        seen.append((phase, system, user))
        if phase == "sumarios_passagem1":
            return "SOURCE_ONLY_DESCRIPTION::" + obj.recorder._contexto["metodo"]
        if phase == "sumarios_de_classe":
            return "Parcel stores a value and exposes it."
        return "GRAPH_OR_REQUIREMENT_CONTEXT_MUST_NOT_LEAK"
    read_lines = project._slice_lines
    def guarded_read(*args):
        assert obj.recorder.fase_atual != "sumarios_de_classe", "class stage must not re-read source"
        return read_lines(*args)
    monkeypatch.setattr(project, "_slice_lines", guarded_read)
    asyncio.run(obj.analyze_summaries(ask=ask, enrich=True))
    first = [v for v in seen if v[0] == "sumarios_passagem1"]
    classes = [v for v in seen if v[0] == "sumarios_de_classe"]
    assert len(first) == 3 and len(classes) == 1
    assert "SOURCE_ONLY_DESCRIPTION::Parcel#initialize" in classes[0][2]
    assert "SOURCE_ONLY_DESCRIPTION::Parcel#twice" in classes[0][2]
    assert "GRAPH_OR_REQUIREMENT" not in classes[0][2]
    assert obj.class_summaries == {"Parcel": "Parcel stores a value and exposes it."}
    assert len(obj.analysis_targets) == 3 and len(obj.targets) == 2
    # The class stage no longer reads a file for every signature.
    forbidden = Mock(side_effect=AssertionError("old class signature reader must not run"))
    monkeypatch.setattr(project, "_slice_lines", forbidden)
    count = len(seen)
    asyncio.run(obj.analyze_summaries(ask=ask, enrich=True))
    assert len(seen) == count  # Compatible cache hit: no new calls.
    forbidden.assert_not_called()
    events = [json.loads(v) for v in (tmp_path / "events.jsonl").read_text().splitlines()]
    prepared = [v for v in events if v["tipo"] == "class_context"]
    assert len(prepared) == 1 and prepared[0]["method_descriptions"] == 3
    assert prepared[0]["prepared_chars"] <= project.MAX_CONTEXT_CHARS
    monkeypatch.setattr(project, "_slice_lines", guarded_read)
    asyncio.run(obj.analyze_summaries(ask=ask, enrich=False, use_cache=False))
    no_graph = [v for v in seen[count:] if v[0] == "sumarios_de_classe"]
    assert len(no_graph) == 1 and no_graph[0][2] == classes[0][2]


def test_same_line_reopenings_are_not_collapsed_by_equal_ranges(tmp_path):
    first = definition(tmp_path, statements=["FLAG = :first"])
    second = definition(tmp_path, statements=["FLAG = :second"])
    view = build(tmp_path, [], definitions=[first, first, second])
    assert view.metadata["available"]["declarations"] == 2
    assert "FLAG = :first" in view.text and "FLAG = :second" in view.text
    assert view.text.count("Declaration lib/box.rb:") == 2

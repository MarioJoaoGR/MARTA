"""Categorical graph evidence and abstaining type selection; no model calls."""
import asyncio
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from marta.ruby_backend import call_graph, param_types, project, rag
from marta.ruby_backend.analysis_state import analysis_provenance
from marta.ruby_backend.evidence import evidence_policy, semantic_decision
from marta.ruby_backend.ruby_ast import parse_source
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok


@pytest.fixture(autouse=True)
def default_policy(monkeypatch):
    for name in ("MARTA_GRAPH_CONTEXT", "MARTA_JUDGE_MIN_SIMILARITY", "MARTA_JUDGE_MIN_MARGIN"):
        monkeypatch.delenv(name, raising=False)


def scored(name, value):
    return rag.ClassMatch(SimpleNamespace(method=SimpleNamespace(qualified_name=name)), value)


def gates(monkeypatch, similarity="0.8", margin="0.1"):
    # Fixture values, not calibrated/default production thresholds.
    monkeypatch.setenv("MARTA_JUDGE_MIN_SIMILARITY", similarity)
    monkeypatch.setenv("MARTA_JUDGE_MIN_MARGIN", margin)
    return evidence_policy()


def test_no_default_thresholds_or_automatic_semantic_top_one():
    policy = evidence_policy()
    assert policy["judge_min_similarity"] is None
    decision = semantic_decision(["A", "B"], [scored("A", 0.99), scored("B", 0.1)], policy)
    assert decision["selected"] is None and decision["reason"] == "no_threshold_policy_declared"


@pytest.mark.parametrize("similarity,margin", [("nan", "0.1"), ("2", "0"), ("0", "-1"), ("oops", "0"), ("0.5", "inf")])
def test_invalid_gates_fail_before_inference(monkeypatch, similarity, margin):
    with pytest.raises(ValueError):
        gates(monkeypatch, similarity, margin)


def test_partial_policy_is_invalid(monkeypatch):
    monkeypatch.setenv("MARTA_JUDGE_MIN_SIMILARITY", "0.5")
    with pytest.raises(ValueError, match="both"):
        evidence_policy()


@pytest.mark.parametrize("scores,reason", [
    ([scored("A", 0.79), scored("B", 0.1)], "below_similarity_threshold"),
    ([scored("A", 0.9), scored("B", 0.89)], "below_margin_threshold"),
    ([scored("A", 0.9), scored("B", 0.9)], "tie"),
    ([scored("A", 0.9)], "incomplete_scored_evidence"),
    ([scored("A", float("nan")), scored("B", 0.1)], "nonfinite_score"),
])
def test_abstention_reasons_are_explicit_and_json_safe(monkeypatch, scores, reason):
    result = semantic_decision(["A", "B"], scores, gates(monkeypatch))
    assert result["selected"] is None and result["reason"] == reason
    json.dumps(result, allow_nan=False)


def test_declared_gates_can_accept_a_strict_compatible_winner(monkeypatch):
    result = semantic_decision(["A", "B"], [scored("A", 0.9), scored("B", 0.2)], gates(monkeypatch))
    assert result["selected"] == "A" and result["reason"] == "declared_thresholds_met"
    assert result["margin"] == pytest.approx(0.7)


def test_missing_and_unique_structural_candidates_do_not_force_semantic_selection():
    assert semantic_decision([], [], evidence_policy())["reason"] == "no_structural_candidates"
    assert semantic_decision(["A"], [], evidence_policy())["selected"] is None


def class_index(vectors):
    # Keep real NumPy scoring, with deterministic injected vectors.
    index = rag.RubyClassIndex(lambda docs: vectors, lambda text: [1.0, 0.0])
    index.init([SimpleNamespace(method=SimpleNamespace(qualified_name=name), summary=name)
                for name in ("A", "B", "Incompatible")])
    return index


def test_scores_are_filtered_to_compatible_classes_before_ranking():
    index = class_index([[0.8, 0.6], [0.6, 0.8], [1, 0]])
    hits = index.query_scored("query", allowed={"A", "B"}, k=3)
    assert [hit.target.method.qualified_name for hit in hits] == ["A", "B"]
    assert [hit.score for hit in hits] == pytest.approx([0.8, 0.6])
    assert index.query("query", k=1)[0].method.qualified_name == "Incompatible"


@pytest.mark.parametrize("query", [[0, 0], [float("nan"), 0], [float("inf"), 0]])
def test_invalid_query_vectors_provide_no_evidence(query):
    index = class_index([[1, 0], [0, 1], [0.5, 0.5]])
    index._embed_query = lambda _: query
    assert index.query_scored("query") == []


def test_invalid_class_vectors_cannot_win_and_ties_are_stable():
    index = class_index([[0, 0], [float("nan"), 1], [1, 0]])
    assert [hit.target.method.qualified_name for hit in index.query_scored("query")] == ["Incompatible"]
    tied = class_index([[1, 0], [1, 0], [1, 0]])
    assert [hit.target.method.qualified_name for hit in tied.query_scored("query")] == ["A", "B", "Incompatible"]


def test_legacy_graph_records_remain_unknown_and_roundtrip_new_evidence():
    legacy = call_graph.CallGraph.from_json({"edges": [["A#a", "B#b", 3, "const"]]})
    assert not legacy.edges[0].supported
    assert legacy.callees("A#a", supported_only=True) == []
    new = call_graph.CallGraph(edges=[call_graph.CallEdge("A#a", "B#b", 3, "const", "static_lookup", ("B",))])
    new._index()
    restored = call_graph.CallGraph.from_json(json.loads(json.dumps(new.to_json())))
    assert restored.edges == new.edges and restored.callees("A#a", supported_only=True) == ["B#b"]


def test_policy_changes_separate_analysis_graph_from_post_analysis_judge(monkeypatch):
    before = analysis_provenance()
    gates(monkeypatch)
    assert analysis_provenance() == before  # Gate calibration need not rerun LLM summaries.
    monkeypatch.setenv("MARTA_GRAPH_CONTEXT", "supported_only")
    assert analysis_provenance() != before


needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def graph(source):
    parsed = parse_source(source)
    index = param_types.ProjectTypeIndex().add_file(parsed)
    return call_graph.StaticCallGraph.build(parsed.methods, index), index


@needs_ruby
def test_ambiguous_constants_never_choose_first_and_qualified_misses_stay_missing():
    source = '''module A
 class Service
  def self.run; 1; end
 end
end
module B
 class Service
  def self.run; 2; end
 end
end
class Caller
 def go; Service.run; end
 def exact; A::Service.run; end
 def missing; Missing::Service.run; end
end
'''
    result, index = graph(source)
    assert index.resolve_candidates("Service") == ["A::Service", "B::Service"]
    assert index._resolve("Service") is None
    assert set(result.callees("Caller#go")) == {"A::Service.run", "B::Service.run"}
    assert result.callees("Caller#go", supported_only=True) == []
    assert result.callees("Caller#exact", supported_only=True) == ["A::Service.run"]
    assert result.callees("Caller#missing") == []


@needs_ruby
def test_singleton_self_does_not_resolve_to_same_named_instance_method():
    result, _ = graph('''class Box
 def run; 1; end
 def self.run; 2; end
 def self.go; run; end
 def self.wrong; self.class.run; end
end
''')
    assert result.callees("Box.go") == ["Box.run"]
    assert result.callees("Box.wrong") == []


@needs_ruby
def test_custom_new_takes_precedence_over_constructor_mapping():
    result, _ = graph('''class Box
 def initialize; 1; end
 def self.new; 2; end
end
class Factory
 def go; Box.new; end
end
''')
    assert result.callees("Factory#go") == ["Box.new"]


@needs_ruby
def test_duck_uniqueness_is_still_inference_not_a_guarantee():
    result, _ = graph('''class Item
 def value; 1; end
end
class Caller
 def go(item); item.value; end
end
''')
    assert result.callees("Caller#go") == ["Item#value"]
    assert result.edges[0].evidence == "duck_unique" and not result.edges[0].supported


@needs_ruby
def test_distinct_callsite_evidence_is_preserved():
    result, _ = graph('''class Service
 def run; 1; end
 def go(other)
  run
  other.run
 end
end
''')
    pair = [edge for edge in result.edges if edge.caller == "Service#go" and edge.callee == "Service#run"]
    assert len(pair) == 2 and {edge.evidence for edge in pair} == {"static_lookup", "duck_unique"}
    assert result.callees("Service#go") == ["Service#run"]
    assert result.callees("Service#go", supported_only=True) == ["Service#run"]


@needs_ruby
def test_uncertain_context_is_labelled_and_filter_applies_both_directions(tmp_path, monkeypatch):
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib/item.rb").write_text('''class Item
 def value; 1; end
end
class Caller
 def go(item); item.value; end
end
''')
    seen = []
    async def ask(system, user):
        seen.append((obj._recorder().fase_atual, user))
        return "valid summary"
    obj = project.RubyProject(str(tmp_path), "lib").discover()
    asyncio.run(obj.analyze_summaries(ask=ask, use_cache=False))
    assert any("duck_unique" in user for phase, user in seen if phase == "sumarios_passagem2")
    assert any("duck_unique" in user for phase, user in seen if phase == "what_todo_propagado")
    seen.clear()
    monkeypatch.setenv("MARTA_GRAPH_CONTEXT", "supported_only")
    obj = project.RubyProject(str(tmp_path), "lib").discover()
    asyncio.run(obj.analyze_summaries(ask=ask, use_cache=False))
    assert not any(phase in ("sumarios_passagem2", "what_todo_propagado") for phase, _ in seen)


@needs_ruby
def test_judge_scores_compatible_candidates_archives_and_can_accept_declared_gates(tmp_path, monkeypatch):
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib/item.rb").write_text('''class A
 def value; 1; end
end
class B
 def value; 2; end
end
class Wrong
 def other; 3; end
end
class Consumer
 def go(item); item.value; end
end
''')
    obj = project.RubyProject(str(tmp_path), "lib", method_names=["Consumer#go"]).discover()
    obj.class_summaries = {name: name for name in ("A", "B", "Wrong", "Consumer")}
    vectors = {"A": [0.9, 0.1], "B": [0.1, 0.9], "Wrong": [1, 0], "Consumer": [0, 1]}
    queries = []
    def query(text):
        queries.append(text)
        return [1, 0]
    def build():
        obj.build_rag(lambda texts: [vectors[text] for text in texts], query, persist=False)
    build()
    selected = obj.targets[0]
    decision = obj.judge_decisions[selected.analysis_id]["item"]
    assert len(queries) == 1
    assert {score["class"] for score in decision["scores"]} == {"A", "B"}
    assert decision["selected"] is None and "semantic type unknown" in selected.judge
    gates(monkeypatch)
    build()
    assert len(queries) == 2 and "semantic candidate: A" in selected.judge
    assert "semantic candidate: Wrong" not in selected.judge
    archives = list((tmp_path / "run_results/judge_runs").glob("*/report.json"))
    assert len(archives) == 2
    assert {json.loads(path.read_text())["policy"]["judge_min_similarity"] for path in archives} == {None, 0.8}
    assert obj.targets[0].judge == next(t.judge for t in obj.analysis_targets if t.analysis_id == selected.analysis_id)
    obj.class_summaries = {}
    build()
    assert len(queries) == 2 and "semantic candidate:" not in selected.judge
    assert obj.judge_decisions == {}


@needs_ruby
@pytest.mark.parametrize("member", ["only_a", "absent"])
def test_unique_or_missing_structural_evidence_skips_query_embedding(tmp_path, member):
    (tmp_path / "lib").mkdir()
    (tmp_path / "lib/item.rb").write_text(f'''class A
 def only_a; 1; end
end
class Consumer
 def go(item); item.{member}; end
end
''')
    obj = project.RubyProject(str(tmp_path), "lib").discover()
    obj.class_summaries = {"A": "A", "Consumer": "Consumer"}
    def forbidden(_):
        raise AssertionError("no query embedding for zero or one structural candidates")
    obj.build_rag(lambda texts: [[1.0, 0.0] for text in texts], forbidden, persist=False)
    target = next(t for t in obj.analysis_targets if t.method.name == "go")
    assert "semantic type unknown" in target.judge
    assert obj.judge_decisions[target.analysis_id]["item"]["scores"] == []


@needs_ruby
def test_ambiguous_ancestor_name_does_not_create_a_false_interface():
    _, index = graph('''module A
 module Shared
  def foo; 1; end
 end
end
module B
 module Shared
  def bar; 2; end
 end
end
class Consumer
 include Shared
end
''')
    assert index._resolve("Shared") is None
    assert not {"foo", "bar"} & index.responds_to("Consumer")


def test_supported_lookup_does_not_rescan_the_edge_list():
    result = call_graph.CallGraph(edges=[call_graph.CallEdge("A#a", "B#b", 1, "self", "static_lookup")])
    result._index()
    class NoRescan(list):
        def __iter__(self):
            raise AssertionError("indexed lookups should not rescan all edges")
    result.edges = NoRescan(result.edges)
    assert result.callees("A#a", supported_only=True) == ["B#b"]
    assert result.callers("B#b", supported_only=True) == ["A#a"]
    assert result.has_supported("A#a", "B#b")
    assert "static_lookup" in result.evidence_label("A#a", "B#b")


def test_identical_judge_questions_share_one_embedding_with_independent_decisions(tmp_path):
    from unittest.mock import Mock
    obj = project.RubyProject(str(tmp_path), "lib")
    obj.type_index = SimpleNamespace(judge_for_method=lambda _: "project candidates: A, B",
                                     candidates=lambda _: ["A", "B"])
    obj.class_db = SimpleNamespace(query_scored=Mock(return_value=[scored("A", 0.9), scored("B", 0.1)]))
    obj.analysis_targets = [SimpleNamespace(analysis_id=str(i), judge="",
        method=SimpleNamespace(param_members={"item": ["value"]})) for i in range(3)]
    obj._augment_judge_semantic()
    assert obj.class_db.query_scored.call_count == 1
    assert all("semantic type unknown" in target.judge for target in obj.analysis_targets)
    obj.judge_decisions["0"]["item"]["scores"][0]["cosine"] = -1
    assert obj.judge_decisions["1"]["item"]["scores"][0]["cosine"] == 0.9
    obj._augment_judge_semantic()  # A new pass/index scope must query anew.
    assert obj.class_db.query_scored.call_count == 2


def test_no_indexed_compatible_classes_skip_query_embedding():
    index = class_index([[1, 0], [0, 1], [1, 1]])
    def forbidden(_):
        raise AssertionError("no embedding when no eligible vectors exist")
    index._embed_query = forbidden
    assert index.query_scored("query", allowed={"Missing"}) == []

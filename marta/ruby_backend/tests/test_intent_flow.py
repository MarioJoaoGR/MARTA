"""Intent-parent scheduling, independent of supplied method/edge order."""
import asyncio
import random
from unittest.mock import Mock

import pytest

from marta.ruby_backend import project
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

SOURCE = """class Flow
  def root; alpha; beta; end
  def alpha; join; end
  def beta; join; end
  def join; :ok; end
end
"""


def analyze(tmp_path, names):
    source = tmp_path / "lib"
    source.mkdir()
    (source / "flow.rb").write_text(SOURCE)
    obj = project.RubyProject(str(tmp_path), "lib").discover()
    by_name = {t.method.name: t for t in obj.analysis_targets}
    obj.analysis_targets = [by_name[name] for name in names]
    selected = []
    events = []
    obj._recorder().evento = lambda **data: events.append(data)
    obj._intent_test_events = events
    async def ask(system, user):
        recorder = obj._recorder()
        if recorder.fase_atual == "what_todo_propagado":
            selected.append((recorder._contexto["metodo"], recorder._contexto["chamador"]))
        return "A stable nonempty synthetic summary"
    asyncio.run(obj.analyze_summaries(ask=ask, use_cache=False))
    return obj, selected


@pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/Prism toolchain")
def test_analysis_selects_same_parent_when_definition_order_changes(tmp_path):
    one = tmp_path / "one"; one.mkdir()
    two = tmp_path / "two"; two.mkdir()
    a, before = analyze(one, ("root", "beta", "join", "alpha"))
    b, after = analyze(two, ("root", "alpha", "join", "beta"))
    assert dict(before)["Flow#join"] == dict(after)["Flow#join"] == "Flow#alpha"
    assert before == after
    for obj in (a, b):
        phases = obj._recorder().score.por_fase
        assert phases["what_todo_raiz"]["chamadas"] == 1
        assert phases["what_todo_propagado"]["chamadas"] == 3
        assert phases["sumarios_passagem2"]["chamadas"] == 3  # Still LLM synthesis.
        choices = [e for e in obj._intent_test_events if e.get("tipo") == "intent_parent_selection"]
        assert [(e["metodo"], e["chamador"], e["depth"]) for e in choices] == [
            ("Flow#alpha", "Flow#root", 1), ("Flow#beta", "Flow#root", 1),
            ("Flow#join", "Flow#alpha", 2)]


def graph(edges):
    from marta.ruby_backend.call_graph import CallGraph, CallEdge
    obj = CallGraph(edges=[CallEdge(a, b, 1, "self", evidence) for a, b, evidence in edges])
    obj._index()
    return obj


def plan(names, edges=(), **kwargs):
    from marta.ruby_backend.intent_flow import plan_intent_flow
    return plan_intent_flow(names, graph(edges), **kwargs)


def chosen(result):
    return {s.callee: (s.caller, s.depth) for layer in result.layers for s in layer}


def test_empty_and_no_graph_plans_have_no_propagation():
    from marta.ruby_backend.intent_flow import plan_intent_flow
    assert plan_intent_flow([]).roots == ()
    result = plan_intent_flow(["B", "A"])
    assert result.roots == ("A", "B") and result.layers == result.fallback == ()


def test_node_and_adjacency_permutations_have_identical_schedules():
    names = ["root", "alpha", "beta", "join", "tail"]
    edges = [("root", "alpha", "static_lookup"), ("root", "beta", "static_lookup"),
             ("alpha", "join", "duck_unique"), ("beta", "join", "static_lookup"),
             ("join", "tail", "static_lookup")]
    expected = plan(names, edges)
    rng = random.Random(611)
    for _ in range(30):
        rng.shuffle(names); rng.shuffle(edges)
        assert plan(names, edges) == expected
    assert chosen(expected)["join"] == ("beta", 2)  # Supported edge breaks a same-depth tie.


def test_lexical_tie_break_does_not_depend_on_edge_insertion_order():
    result = plan(["r", "a", "b", "child"], [("r", "b", "static_lookup"),
        ("r", "a", "static_lookup"), ("b", "child", "static_lookup"),
        ("a", "child", "static_lookup")])
    assert chosen(result)["child"] == ("a", 2)


def test_root_distance_precedes_edge_support_and_does_not_claim_semantic_optimality():
    result = plan(["root", "a", "child"], [("root", "a", "static_lookup"),
        ("root", "child", "duck_unique"), ("a", "child", "static_lookup")])
    assert chosen(result)["child"] == ("root", 1)


def test_omitted_or_ambiguous_callers_are_not_used_as_roots_for_other_methods():
    # Production discovery removes ambiguous qns before invoking this planner.
    result = plan(["b", "c"], [("excluded", "b", "static_lookup"), ("b", "c", "static_lookup")])
    assert result.roots == ("b",) and chosen(result) == {"c": ("b", 1)}


def test_unreachable_cycle_and_its_descendants_keep_the_readme_fallback():
    edges = [("a", "b", "static_lookup"), ("b", "a", "static_lookup"),
             ("b", "tail", "static_lookup")]
    result = plan(["isolated", "a", "b", "tail"], edges)
    assert result.roots == ("isolated",) and result.layers == ()
    assert result.fallback == ("a", "b", "tail")
    reached = plan(["root", "a", "b", "tail"], edges + [("root", "a", "static_lookup")])
    assert chosen(reached) == {"a": ("root", 1), "b": ("a", 2), "tail": ("b", 3)}
    assert not reached.fallback


def test_supported_only_filters_before_roots_and_parent_selection():
    edges = [("a", "b", "duck_unique"), ("b", "c", "static_lookup")]
    result = plan(["a", "b", "c"], edges, supported_only=True)
    assert result.roots == ("a", "b") and chosen(result) == {"c": ("b", 1)}


def test_long_chain_has_one_adjacency_lookup_and_one_step_per_method():
    from marta.ruby_backend.intent_flow import plan_intent_flow
    names = [f"m{i:04}" for i in range(2500)]
    obj = graph([(a, b, "static_lookup") for a, b in zip(names, names[1:])])
    obj.callers = Mock(wraps=obj.callers)
    result = plan_intent_flow(reversed(names), obj)
    assert obj.callers.call_count == len(names)
    assert len(result.layers) == len(names) - 1 and not result.fallback
    assert sum(len(layer) for layer in result.layers) == len(names) - 1
    assert result.layers[-1][0].depth == len(names) - 1


def test_policy_and_implementation_are_part_of_analysis_provenance():
    from marta.ruby_backend.analysis_state import analysis_provenance
    from marta.ruby_backend.intent_flow import POLICY
    provenance = analysis_provenance()
    assert provenance["intent_flow_policy"] == POLICY
    assert len(provenance["implementation"]["intent_flow.py"]) == 64

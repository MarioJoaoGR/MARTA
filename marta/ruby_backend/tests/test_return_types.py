"""Direct constructor-return facts and one-hop inference, without executing Ruby."""
import json
from unittest.mock import Mock

import pytest

from marta.ruby_backend import call_graph, param_types, ruby_ast
from marta.ruby_backend.analysis_state import analysis_provenance
from marta.ruby_backend.return_types import POLICY, ReturnTypeIndex
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/Prism toolchain")


WIDGET = "class Widget; def run; :ok; end; end\n"


def inventory(source):
    parsed = ruby_ast.parse_source(source)
    index = param_types.ProjectTypeIndex().add_file(parsed)
    return parsed, index, ReturnTypeIndex(parsed.methods, index)


def graph(source):
    parsed, index, returns = inventory(source)
    return call_graph.StaticCallGraph.build(parsed.methods, index), parsed, returns


def factory(body):
    return WIDGET + f"class Factory\n  def self.build(value = nil)\n    {body}\n  end\nend\n"


def inferred(graph):
    return [edge for edge in graph.edges if edge.evidence == "return_type_inferred"]


@needs_ruby
@pytest.mark.parametrize("body", ["Widget.new", "return Widget.new", "Widget.new(value)",
                                   "::Widget.new(value: value)", "return ::Widget.new(value)"])
def test_direct_constructor_normal_return_candidates(body):
    parsed, _, index = inventory(factory(body))
    method = next(m for m in parsed.methods if m.qualified_name == "Factory.build")
    assert method.return_fact["policy"] == POLICY
    assert method.return_fact["kind"] == "constant_new"
    hint = index.for_method("Factory.build")
    assert hint.candidates == ("Widget",) and hint.reason == "direct_constructor_candidate"


@needs_ruby
def test_endless_factory_is_supported_without_an_extra_parse():
    _, _, index = inventory(WIDGET + "class Factory; def self.build = Widget.new; end")
    assert index.for_method("Factory.build").candidates == ("Widget",)


@needs_ruby
@pytest.mark.parametrize("body", [
    "nil", "return", "return Widget.new, Widget.new", "[Widget.new]",
    "if value; Widget.new; else; nil; end", "return Widget.new if value",
    "log; Widget.new", "Widget.new; nil", "Widget.new rescue nil",
    "Widget&.new", "Widget.new { return nil }", "build_again", "@stored",
    "(Widget.new)", "Widget.new(begin; return nil; end)",
])
def test_unsupported_bodies_stay_unknown(body):
    _, _, index = inventory(factory(body))
    assert not index.for_method("Factory.build").candidates


@needs_ruby
@pytest.mark.parametrize("expression,reason", [
    ("External.new", "unknown_project_constant"),
    ("Missing::Widget.new", "unknown_project_constant"),
    ("Container.new", "not_project_class"),
])
def test_external_missing_and_module_constants_are_not_instance_types(expression, reason):
    _, _, index = inventory(factory(expression) + "module Container; end")
    hint = index.for_method("Factory.build")
    assert hint.candidates == () and hint.reason == reason


@needs_ruby
def test_ambiguous_constants_are_not_arbitrarily_selected_but_absolute_root_can_match():
    source = factory("Widget.new") + "module Extra; class Widget; end; end"
    _, _, index = inventory(source)
    assert index.for_method("Factory.build").reason == "ambiguous_project_constant"
    _, _, exact = inventory(source.replace("    Widget.new", "    ::Widget.new"))
    assert exact.for_method("Factory.build").candidates == ("Widget",)


@needs_ruby
def test_short_constant_fallback_is_not_used_as_return_evidence():
    source = "module Extra; class Widget; end; end\nclass Factory; def self.build; Widget.new; end; end"
    _, _, index = inventory(source)
    assert index.for_method("Factory.build").reason == "non_exact_constant_lookup"


@needs_ruby
@pytest.mark.parametrize("source,reason", [
    ("class Widget; def self.new; nil; end; end", "custom_new"),
    ("class Parent; def self.new; nil; end; end\nclass Widget < Parent; end", "custom_new"),
    ("module Build; def new; nil; end; end\nclass Widget; extend Build; end", "custom_new_extension"),
])
def test_known_custom_constructor_paths_abstain(source, reason):
    _, _, index = inventory(source + "\nclass Factory; def self.build; Widget.new; end; end")
    assert index.for_method("Factory.build").reason == reason


@needs_ruby
def test_custom_new_method_itself_is_not_treated_as_an_ordinary_factory():
    _, _, index = inventory(WIDGET + "class Factory; def self.new; Widget.new; end; end")
    assert index.for_method("Factory.new").reason == "custom_constructor_method"


@needs_ruby
def test_redefined_factory_is_unknown_even_if_bodies_appear_equivalent():
    source = factory("Widget.new") + "class Factory; def self.build; Widget.new; end; end"
    _, _, index = inventory(source)
    assert index.for_method("Factory.build").reason == "ambiguous_definition"


@needs_ruby
def test_fact_queries_are_memoized_per_index_and_do_not_leak_to_a_new_index(monkeypatch):
    _, _, index = inventory(factory("Widget.new"))
    infer = Mock(wraps=index._infer)
    monkeypatch.setattr(index, "_infer", infer)
    first = index.for_method("Factory.build")
    assert index.for_method("Factory.build") is first and infer.call_count == 1
    _, _, changed = inventory(factory("nil"))
    assert not changed.for_method("Factory.build").candidates
    assert index.for_method("missing").reason == "missing_definition"


@needs_ruby
def test_factory_chain_adds_possible_instance_edge_with_source_and_preserves_old_lookup():
    source = factory("Widget.new(value)") + "def use; Factory.build(1).run; end"
    result, parsed, _ = graph(source)
    edges = inferred(result)
    assert len(edges) == 1
    edge = edges[0]
    assert (edge.caller, edge.callee) == ("use", "Widget#run")
    assert edge.receiver_candidates == ("Widget",) and edge.via == ("Factory.build",)
    assert not edge.supported
    assert "Widget#run" not in result.callees("use", supported_only=True)
    assert "Factory.build" in result.callees("use", supported_only=True)
    assert "return source: Factory.build" in result.evidence_label("use", "Widget#run")
    restored = call_graph.CallGraph.from_json(json.loads(json.dumps(result.to_json())))
    assert restored.edges == result.edges
    call = next(c for m in parsed.methods if m.name == "use" for c in m.calls if c["name"] == "run")
    assert call["receiver_call"]["name"] == "build"


@needs_ruby
@pytest.mark.parametrize("expression", ["build.run", "self.build.run"])
def test_one_hop_instance_factory_receiver(expression):
    source = WIDGET + f"class Factory; def build; Widget.new; end; def use; {expression}; end; end"
    result, _, _ = graph(source)
    assert any(e.caller == "Factory#use" and e.callee == "Widget#run" for e in inferred(result))


@needs_ruby
@pytest.mark.parametrize("expression", ["Factory&.build.run", "Factory.build&.run", "Factory.build {}.run"])
def test_safe_navigation_and_blocks_do_not_gain_new_return_edges(expression):
    result, _, _ = graph(factory("Widget.new") + f"def use; {expression}; end")
    assert not inferred(result)


@needs_ruby
def test_argument_control_transfer_and_large_argument_tree_do_not_create_facts():
    _, _, index = inventory(factory("Widget.new([" + ",".join("1" for _ in range(1000)) + "])") )
    assert not index.for_method("Factory.build").candidates
    _, _, control = inventory(factory("Widget.new(begin; return nil; end)"))
    assert not control.for_method("Factory.build").candidates


@needs_ruby
def test_chains_of_factories_and_assigned_locals_are_not_globally_propagated():
    source = factory("Widget.new") + "class Other; def self.build; Factory.build; end; end\ndef use; Other.build.run; end"
    result, _, _ = graph(source)
    assert not inferred(result)
    result, _, _ = graph(factory("Widget.new") + "def use; item = Factory.build; item.run; end")
    assert not inferred(result)


@needs_ruby
def test_explicit_nonself_method_receiver_is_not_bound_to_the_lexical_owner():
    source = WIDGET + "class Wrong; def Other.build; Widget.new; end; end"
    parsed, _, _ = inventory(source)
    assert next(m for m in parsed.methods if m.name == "build").return_fact is None


def test_old_metadata_is_unknown_and_parse_errors_remove_new_evidence():
    raw = {"name": "build", "owner": "Factory", "singleton": True,
           "start_line": 1, "end_line": 2}
    old = ruby_ast._from_json({"methods": [raw]})
    assert old.methods[0].return_fact is None
    broken = ruby_ast._from_json({"methods": [{**raw,
        "return_fact": {"policy": POLICY, "kind": "constant_new", "constant": "Widget"},
        "calls": [{"name": "run", "recv": "other", "receiver_call": {"name": "build"}}]}],
        "errors": [{"message": "broken"}]})
    assert broken.methods[0].return_fact is None
    assert "receiver_call" not in broken.methods[0].calls[0]


def test_provenance_identifies_extractor_and_inference_policy():
    metadata = analysis_provenance()
    assert metadata["return_type_policy"] == POLICY
    for name in ("return_types.py", "ruby_ast.py", "rb/marta_parse.rb", "rb/marta_return_facts.rb"):
        assert len(metadata["implementation"][name]) == 64
    assert call_graph.RESOLVER_VERSION == 4


@needs_ruby
def test_ambiguous_factory_lookup_does_not_gain_return_evidence():
    source = factory("Widget.new") + "module Extra; class Factory; def self.build; Widget.new; end; end; end\ndef use; Factory.build.run; end"
    result, _, _ = graph(source)
    assert not inferred(result)


@needs_ruby
def test_top_level_factory_can_resolve_but_owner_global_fallback_is_not_upgraded():
    source = WIDGET + "def build; Widget.new; end\ndef use; build.run; end"
    result, _, _ = graph(source)
    assert any(e.caller == "use" and e.callee == "Widget#run" for e in inferred(result))
    result, _, _ = graph(source + "class Caller; def use; build.run; end; end")
    assert not any(e.caller == "Caller#use" for e in inferred(result))


def test_extra_edge_provenance_is_omitted_when_empty_and_roundtrips_when_present():
    edge = call_graph.CallEdge("A#x", "B#y", 2, "const", "static_lookup")
    data = call_graph.CallGraph(edges=[edge]).to_json()
    assert "via" not in data["edges"][0]
    assert call_graph.CallGraph.from_json(data).edges == [edge]


@needs_ruby
def test_invalid_recovered_parse_does_not_publish_return_hypotheses():
    parsed, _, _ = inventory(factory("Widget.new") + "def broken(")
    assert parsed.errors and all(m.return_fact is None for m in parsed.methods)
    assert all("receiver_call" not in c for m in parsed.methods for c in m.calls)


@needs_ruby
@pytest.mark.parametrize("extension", [
    "module Actual; def new; nil; end; end; module Build; include Actual; end",
    "module Build; attr_reader :new; end",
])
def test_extended_module_inheritance_and_generated_new_accessor_abstain(extension):
    _, _, index = inventory(extension + "\nclass Widget; extend Build; end\nclass Factory; def self.build; Widget.new; end; end")
    assert index.for_method("Factory.build").reason == "custom_new_extension"


@needs_ruby
def test_initialize_return_value_is_not_the_new_objects_type():
    source = factory("Widget.new") + "class Other; def run; end; end\nclass Widget; def initialize; Other.new; end; end\ndef use; Factory.build.run; end"
    result, _, index = graph(source)
    assert index.for_method("Factory.build").candidates == ("Widget",)
    assert [(e.caller, e.callee) for e in inferred(result)] == [("use", "Widget#run")]

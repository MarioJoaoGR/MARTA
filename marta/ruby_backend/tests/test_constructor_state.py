"""Constructor/getter candidates, guarded by supplied write and scope evidence."""
import json

import pytest

from marta.ruby_backend import call_graph, param_types, ruby_ast
from marta.ruby_backend.return_types import ReturnTypeIndex, STATE_POLICY
from marta.ruby_backend.analysis_state import analysis_provenance
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/Prism toolchain")

WIDGET = "class Widget; def run; :ok; end; end\nclass Other; def run; :different; end; end\n"


def code(*, constructor="@widget = Widget.new", getter="def widget; @widget; end", extra="", header="class Box"):
    return WIDGET + f"{header}\n def initialize(value = nil)\n  {constructor}\n end\n {getter}\n def use; widget.run; end\n def direct; @widget.run; end\n {extra}\nend\n"


def inventory(source):
    parsed = ruby_ast.parse_source(source)
    types = param_types.ProjectTypeIndex().add_file(parsed)
    returns = ReturnTypeIndex(parsed.methods, types)
    graph = call_graph.StaticCallGraph.build(parsed.methods, types)
    return parsed, types, returns, graph


def state_edges(graph):
    return [e for e in graph.edges if e.evidence in ("state_return_inferred", "constructor_ivar_inferred")]


@needs_ruby
@pytest.mark.parametrize("getter", ["def widget; @widget; end", "def widget; return @widget; end",
                                   "def widget = @widget", "attr_reader :widget"])
def test_simple_constructor_supports_getter_and_direct_ivar_without_runtime_guarantee(getter):
    parsed, types, returns, graph = inventory(code(getter=getter))
    assert parsed.state_policy == STATE_POLICY and types.state_complete and not types.state_opaque
    hint = returns.for_method("Box#widget")
    assert hint.candidates == ("Widget",) and hint.via == ("Box#initialize",)
    assert hint.reason == "constructor_ivar_candidate"
    edges = state_edges(graph)
    assert {(e.caller, e.callee) for e in edges} == {("Box#use", "Widget#run"), ("Box#direct", "Widget#run")}
    assert all(not e.supported for e in edges)
    assert "Widget#run" not in graph.callees("Box#use", supported_only=True)
    assert "Other#run" not in graph.callees("Box#use")  # Typed hypothesis narrows duck alternatives.
    getter_edge = next(e for e in edges if e.caller == "Box#use")
    assert getter_edge.via == ("Box#initialize", "Box#widget")
    assert graph.from_json(json.loads(json.dumps(graph.to_json()))).edges == graph.edges


@needs_ruby
def test_multiple_simple_fields_are_independent_and_other_field_writes_do_not_taint_type():
    parsed, _, returns, _ = inventory(code(constructor="@widget = Widget.new(value)\n @counter = 0",
                                          extra="def tick; @counter += 1; end"))
    assert returns.for_ivar("Box", "@widget").candidates == ("Widget",)
    assert not returns.for_ivar("Box", "@counter").candidates
    init = next(m for m in parsed.methods if m.qualified_name == "Box#initialize")
    assert init.state_effects["writes"] == {"@widget": 1, "@counter": 1}


@needs_ruby
@pytest.mark.parametrize("extra", [
    "def reset; @widget = Other.new; end",
    "def reset; @widget = Widget.new; end",
    "def reset; @widget ||= Other.new; end",
    "def reset; @widget &&= nil; end",
    "def reset; @widget += Other.new; end",
    "def reset; @widget, @other = [Other.new, nil]; end",
    "def widget=(value); @widget = value; end",
    "def later; 2.times { @widget = Other.new }; end",
])
def test_observed_later_writes_block_state_candidate(extra):
    _, _, returns, graph = inventory(code(extra=extra))
    assert not returns.for_ivar("Box", "@widget").candidates
    assert returns.for_ivar("Box", "@widget").reason == "other_or_repeated_ivar_writes"
    assert not state_edges(graph)


@needs_ruby
@pytest.mark.parametrize("getter", ["attr_accessor :widget", "attr_reader :widget\nattr_writer :widget"])
def test_exposed_generated_writer_blocks_initial_type_even_without_an_observed_call(getter):
    _, _, returns, graph = inventory(code(getter=getter))
    assert returns.for_ivar("Box", "@widget").reason == "exposed_attribute_writer"
    assert not state_edges(graph)


@needs_ruby
@pytest.mark.parametrize("constructor", [
    "@widget = value", "@widget = nil", "@widget ||= Widget.new",
    "if value; @widget = Widget.new; end", "setup; @widget = Widget.new",
    "@widget = Widget.new(self)", "@widget = Widget.new(value.fetch(:x))",
    "@widget = Widget.new { value }", "@widget = Widget.new\n return",
    "@widget = Widget.new\n @widget = Other.new",
])
def test_nonclosed_or_nonunique_construction_stays_unknown(constructor):
    _, _, returns, graph = inventory(code(constructor=constructor))
    assert not returns.for_ivar("Box", "@widget").candidates
    assert not state_edges(graph)


@needs_ruby
@pytest.mark.parametrize("mutation", [
    "def touch; instance_variable_set(:@widget, Other.new); end",
    "def touch; remove_instance_variable(:@widget); end",
    "def touch; send(target, Other.new); end",
    "def touch; send(:instance_variable_set, :@widget, Other.new); end",
    "def touch; send(:send, :instance_variable_set, :@widget, Other.new); end",
    "def touch; self.class.attr_writer :widget; end",
    "def touch; self.class.include Extra; end",
    "alias another widget", "undef widget",
])
def test_reflection_or_dynamic_method_changes_block_state_inference(mutation):
    parsed, _, returns, graph = inventory(code(extra=mutation))
    assert parsed.state_opaque
    assert returns.for_ivar("Box", "@widget").reason == "opaque_project_state_effects"
    assert not state_edges(graph)


@needs_ruby
def test_reflection_in_another_class_is_a_project_blocker_when_receiver_is_not_tracked():
    _, _, returns, graph = inventory(code() + "class External; def mutate(box); box.instance_variable_set(:@widget, Other.new); end; end")
    assert returns.for_ivar("Box", "@widget").reason == "opaque_project_state_effects"
    assert not state_edges(graph)


@needs_ruby
def test_literal_send_to_an_ordinary_method_is_not_assumed_to_write_state():
    parsed, _, returns, _ = inventory(code(extra="def inspect_field; send(:widget); end"))
    assert not parsed.state_opaque
    assert returns.for_ivar("Box", "@widget").candidates == ("Widget",)


@needs_ruby
@pytest.mark.parametrize("source", [
    code(header="class Box < Object"),
    code(extra="include Extra"), code(extra="prepend Extra"), code(extra="extend Extra"),
    code() + "class Child < Box; end",
    code() + "class Box; include Extra; end",
])
def test_inheritance_mixins_and_known_subclasses_do_not_borrow_owner_state(source):
    _, _, returns, graph = inventory(source)
    assert not returns.for_ivar("Box", "@widget").candidates
    assert not state_edges(graph)


@needs_ruby
def test_reopened_methods_preserve_writes_and_duplicate_initializers_abstain():
    _, _, returns, _ = inventory(code() + "class Box; def reset; @widget = nil; end; end")
    assert returns.for_ivar("Box", "@widget").reason == "other_or_repeated_ivar_writes"
    _, _, duplicate, _ = inventory(code() + "class Box; def initialize; @widget = Widget.new; end; end")
    assert duplicate.for_ivar("Box", "@widget").reason == "ambiguous_or_missing_initializer"


@needs_ruby
def test_redefined_getters_and_generated_reader_conflicts_are_not_resolved_by_order():
    _, _, returns, _ = inventory(code(extra="def widget; @widget; end"))
    assert returns.for_method("Box#widget").reason == "ambiguous_definition"
    _, _, conflict, _ = inventory(code(extra="attr_reader :widget"))
    assert conflict.for_method("Box#widget").reason == "generated_method_conflict"
    # This also closes the known attr-reader shadowing hole for direct factories.
    _, _, constant, _ = inventory(code(getter="def widget; Other.new; end", extra="attr_reader :widget"))
    assert constant.for_method("Box#widget").reason == "generated_method_conflict"


@needs_ruby
def test_class_object_state_is_separate_from_instance_state():
    _, _, returns, graph = inventory(code(extra="def self.change; @widget = Other.new; end\ndef self.use; @widget.run; end"))
    assert returns.for_ivar("Box", "@widget").candidates == ("Widget",)
    assert not any(e.caller == "Box.use" for e in state_edges(graph))


@needs_ruby
def test_custom_owner_new_and_target_new_abstain():
    _, _, owner, _ = inventory(code(extra="def self.new; allocate; end"))
    assert not owner.for_ivar("Box", "@widget").candidates
    _, _, target, _ = inventory(code() + "class Widget; def self.new; Other.new; end; end")
    assert not target.for_ivar("Box", "@widget").candidates


@needs_ruby
def test_lexical_and_global_constant_aliases_cannot_silently_select_a_class():
    _, _, returns, _ = inventory(code(extra="Widget = Other"))
    assert returns.for_ivar("Box", "@widget").reason == "lexical_constant_assignment"
    _, _, absolute, _ = inventory(code(constructor="@widget = ::Widget.new", extra="Widget = Other"))
    assert absolute.for_ivar("Box", "@widget").candidates == ("Widget",)
    _, _, global_alias, _ = inventory(code() + "Widget = Other")
    assert global_alias.for_ivar("Box", "@widget").reason == "opaque_project_state_effects"


@needs_ruby
def test_state_queries_are_memoized_without_reusing_an_old_source_index():
    _, _, returns, _ = inventory(code())
    first = returns.for_ivar("Box", "@widget")
    assert returns.for_ivar("Box", "@widget") is first
    _, _, changed, _ = inventory(code(extra="def reset; @widget = nil; end"))
    assert not changed.for_ivar("Box", "@widget").candidates


def test_legacy_or_invalid_metadata_does_not_assert_absence_of_writes():
    raw = {"path": "x.rb", "classes": [{"name": "Box", "qualified_name": "Box", "kind": "class",
            "start_line": 1, "end_line": 3}], "methods": []}
    parsed = ruby_ast._from_json(raw)
    types = param_types.ProjectTypeIndex().add_file(parsed)
    returns = ReturnTypeIndex(parsed.methods, types)
    assert not types.state_complete
    assert returns.for_ivar("Box", "@widget").reason == "incomplete_state_metadata"
    invalid = ruby_ast._from_json({**raw, "state_policy": STATE_POLICY, "errors": [{"message": "bad"}]})
    assert invalid.state_policy is None and invalid.state_opaque


def test_provenance_identifies_state_extractor_and_policy():
    metadata = analysis_provenance()
    assert metadata["constructor_state_policy"] == STATE_POLICY
    assert len(metadata["implementation"]["rb/marta_state_facts.rb"]) == 64
    assert call_graph.RESOLVER_VERSION == 5


@needs_ruby
def test_multiple_files_are_combined_before_deciding_that_no_later_write_exists():
    first = ruby_ast.parse_source(WIDGET + "class Box; def initialize; @widget = Widget.new; end; end", "first.rb")
    second = ruby_ast.parse_source("class Box; attr_reader :widget; def use; widget.run; end; end", "second.rb")
    types = param_types.ProjectTypeIndex().add_file(first).add_file(second)
    methods = first.methods + second.methods
    assert ReturnTypeIndex(methods, types).for_method("Box#widget").candidates == ("Widget",)
    third = ruby_ast.parse_source("class Box; def reset; @widget = nil; end; end", "third.rb")
    types.add_file(third)
    assert not ReturnTypeIndex(methods + third.methods, types).for_method("Box#widget").candidates


@needs_ruby
def test_one_unscanned_or_invalid_file_prevents_a_project_wide_no_writes_claim():
    parsed, types, _, _ = inventory(code())
    types.add_file(ruby_ast.FileParse("legacy.rb"))
    assert ReturnTypeIndex(parsed.methods, types).for_ivar("Box", "@widget").reason == "incomplete_state_metadata"
    parsed, types, _, _ = inventory(code())
    broken = ruby_ast.parse_source("def broken(", "broken.rb")
    types.add_file(broken)
    assert not ReturnTypeIndex(parsed.methods + broken.methods, types).for_ivar("Box", "@widget").candidates


@needs_ruby
def test_oversized_constructor_is_unknown_instead_of_silently_ignoring_tail_statements():
    assignments = "@widget = Widget.new\n" + "\n".join(f"@v{i} = {i}" for i in range(64))
    _, _, returns, graph = inventory(code(constructor=assignments))
    assert returns.for_ivar("Box", "@widget").reason == "unsupported_constructor"
    assert not state_edges(graph)


@needs_ruby
def test_incomplete_constructor_record_is_not_treated_as_complete():
    parsed, types, _, _ = inventory(code())
    initializer = next(m for m in parsed.methods if m.qualified_name == "Box#initialize")
    initializer.state_effects["constructor"].pop("assignments")
    assert ReturnTypeIndex(parsed.methods, types).for_ivar("Box", "@widget").reason == "incomplete_constructor_metadata"


@needs_ruby
def test_default_parameter_calls_cannot_read_state_before_initialization():
    source = code(extra="def before; @widget.run; end").replace(
        "initialize(value = nil)", "initialize(value = before)")
    _, _, returns, graph = inventory(source)
    assert returns.for_ivar("Box", "@widget").reason == "unsupported_constructor"
    assert not state_edges(graph)


@needs_ruby
def test_literal_keyword_defaults_remain_supported_and_source_label_is_not_a_return_claim():
    source = code().replace("initialize(value = nil)", "initialize(value: nil, count: 1)")
    _, _, returns, graph = inventory(source)
    assert returns.for_ivar("Box", "@widget").candidates == ("Widget",)
    assert "inference source: Box#initialize" in graph.evidence_label("Box#direct", "Widget#run")

"""Tests for the dynamic (TracePoint) call graph and static/dynamic comparison."""
import textwrap

import pytest

from marta.ruby_backend import call_graph, dyn_call_graph, param_types, runner
from marta.ruby_backend.ruby_ast import RubyParseError, parse_source


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


SRC = """\
class Transaction
  def initialize(kind, amount); @kind = kind; @amount = amount; end
  attr_reader :amount, :kind
end
class Wallet
  def deposit(amount); apply(Transaction.new(:deposit, amount)); end
  def apply(entry); validate(entry); @balance = entry.amount; end
  def validate(entry); raise "bad" if entry.amount <= 0; end
end
"""


def _project(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "wallet.rb").write_text(SRC)
    (tmp_path / "driver.rb").write_text('require "wallet"\nWallet.new.deposit(100)\n')
    return tmp_path


def test_dynamic_captures_exercised_edges(tmp_path):
    p = _project(tmp_path)
    g = dyn_call_graph.run_dynamic("src", str(p / "driver.rb"), cwd=str(p))
    assert "Wallet#apply" in g.callees("Wallet#deposit")
    assert "Transaction#initialize" in g.callees("Wallet#deposit")
    assert "Wallet#validate" in g.callees("Wallet#apply")


def test_dynamic_misses_c_level_attr_readers(tmp_path):
    p = _project(tmp_path)
    g = dyn_call_graph.run_dynamic("src", str(p / "driver.rb"), cwd=str(p))
    # attr_reader #amount is C-defined -> not traced by :call
    assert "Transaction#amount" not in g.callees("Wallet#apply")


def test_static_vs_dynamic_comparison(tmp_path):
    p = _project(tmp_path)
    fp = parse_source(SRC, "wallet.rb")
    idx = param_types.ProjectTypeIndex().add_file(fp)
    static_g = call_graph.StaticCallGraph.build(fp.methods, idx)
    dyn_g = dyn_call_graph.run_dynamic("src", str(p / "driver.rb"), cwd=str(p))

    cmp = dyn_call_graph.compare(static_g, dyn_g)
    # Method-to-method edges agree; the difference is the attr-accessor edges the
    # static graph adds and the dynamic one can't see.
    assert ("Wallet#deposit", "Wallet#apply") in cmp.both
    assert ("Wallet#apply", "Wallet#validate") in cmp.both
    assert ("Wallet#apply", "Transaction#amount") in cmp.static_only
    assert cmp.dynamic_only == set()  # dynamic saw nothing static missed here
    assert 0.0 <= cmp.agreement <= 1.0


def test_optional_c_mode_adds_accessors_without_hiding_ruby_calls_or_core_noise(tmp_path):
    p = _project(tmp_path)
    before = dyn_call_graph.run_dynamic("src", str(p / "driver.rb"), cwd=str(p))
    trace = dyn_call_graph.trace_dynamic("src", str(p / "driver.rb"), cwd=str(p), include_c=True)
    assert before.edge_set() <= trace.graph.edge_set()
    assert ("Wallet#apply", "Transaction#amount") in trace.graph.edge_set()
    assert ("Wallet#validate", "Transaction#amount") in trace.graph.edge_set()
    native = [e for e in trace.graph.edges if e.kind == "dynamic_c"]
    assert native and all(e.callee == "Transaction#amount" for e in native)
    assert all(e.evidence == "runtime_observed" and e.supported for e in native)
    assert trace.metadata["completed"] and trace.metadata["driver_status"] == "returned"
    assert set(trace.metadata["events"]) == {"call", "return", "c_call", "c_return"}
    assert trace.metadata["stack_resets"] == trace.metadata["remaining_frames"] == 0
    assert len(trace.metadata["helper_sha256"]) == 64 and trace.metadata["helper_unchanged"]
    assert trace.metadata["driver_sha256_before"] == trace.metadata["driver_sha256_after"]
    assert call_graph.CallGraph.from_json(trace.graph.to_json()).edges == trace.graph.edges
    fp = parse_source(SRC, "wallet.rb")
    static = call_graph.StaticCallGraph.build(fp.methods, param_types.ProjectTypeIndex().add_file(fp))
    assert ("Wallet#apply", "Transaction#amount") in dyn_call_graph.compare(static, trace.graph).both


def traced(tmp_path, source, driver, *, include_c=True):
    (tmp_path / "src").mkdir()
    (tmp_path / "src/code.rb").write_text(textwrap.dedent(source))
    (tmp_path / "driver.rb").write_text(textwrap.dedent('require "code"\n' + driver))
    return dyn_call_graph.trace_dynamic("src", str(tmp_path / "driver.rb"), str(tmp_path), include_c=include_c)


def test_accessors_inherited_mixed_in_and_singleton_are_named_by_definition_owner(tmp_path):
    trace = traced(tmp_path, """
        module Fields
          attr_accessor :value
        end
        class Base
          include Fields
          def read; self.value = 3; value; end
        end
        class Child < Base; end
        class Registry
          class << self
            attr_accessor :item
            def fetch; self.item = 1; item; end
          end
        end
    """, "Child.new.read\nRegistry.fetch\n")
    assert trace.graph.edge_set() == {("Base#read", "Fields#value="), ("Base#read", "Fields#value"),
                                     ("Registry.fetch", "Registry.item="), ("Registry.fetch", "Registry.item")}
    assert all(e.kind == "dynamic_c" for e in trace.graph.edges)


def test_native_origin_is_not_the_project_call_site_and_source_prefix_has_boundary(tmp_path):
    other = tmp_path / "src_extra"
    other.mkdir()
    (other / "outside.rb").write_text("class Outside; attr_reader :value; def relay; Inside.leaf; end; end")
    trace = traced(tmp_path, """
        class Inside
          def self.leaf; 1; end
          def self.run(o); o.value; 1.to_s; o.relay; end
        end
    """, 'require_relative "src_extra/outside"\nInside.run(Outside.new)\n')
    assert trace.graph.edge_set() == set()  # No Outside/Integer edge or bridge through Outside#relay.
    assert trace.metadata["completed"] and trace.metadata["stack_resets"] == 0


def test_native_iterators_exceptions_and_recursion_preserve_the_enclosing_ruby_frame(tmp_path):
    trace = traced(tmp_path, """
        class Flow
          attr_reader :value
          def entry
            [1, 2].each { recursive(2) }
            begin; fail_here; rescue RuntimeError; after; end
          end
          def recursive(n); n > 0 ? recursive(n - 1) : value; end
          def fail_here; raise "expected"; end
          def after; tail; end
          def tail; value; end
        end
    """, "Flow.new.entry\n")
    assert trace.graph.edge_set() == {("Flow#entry", "Flow#recursive"), ("Flow#recursive", "Flow#value"),
        ("Flow#entry", "Flow#fail_here"), ("Flow#entry", "Flow#after"), ("Flow#after", "Flow#tail"),
        ("Flow#tail", "Flow#value")}
    assert trace.metadata["stack_resets"] == trace.metadata["remaining_frames"] == 0


def test_fiber_suspension_does_not_make_one_fibers_method_call_another(tmp_path):
    trace = traced(tmp_path, """
        class Flow
          attr_reader :value
          def first; Fiber.yield; value; end
          def second; Fiber.yield; value; end
        end
    """, "o = Flow.new\na = Fiber.new { o.first }\nb = Fiber.new { o.second }\na.resume; b.resume; a.resume; b.resume\n")
    assert trace.graph.edge_set() == {("Flow#first", "Flow#value"), ("Flow#second", "Flow#value")}
    assert trace.metadata["stack_resets"] == trace.metadata["remaining_frames"] == 0


def test_threads_do_not_share_call_stacks(tmp_path):
    trace = traced(tmp_path, """
        class Flow
          attr_reader :value
          def first(ready, go); ready << true; go.pop; value; end
          def second; value; end
        end
    """, "o = Flow.new\nready = Queue.new; go = Queue.new\nt = Thread.new { o.first(ready, go) }\nready.pop; o.second; go << true; t.join\n")
    assert trace.graph.edge_set() == {("Flow#first", "Flow#value"), ("Flow#second", "Flow#value")}
    assert trace.metadata["stack_resets"] == trace.metadata["remaining_frames"] == 0


def test_lookup_is_not_stale_after_a_generated_reader_is_redefined(tmp_path):
    trace = traced(tmp_path, """
        class Box
          attr_reader :value
          def run; value; end
        end
    """, "Box.new.run\nBox.class_eval { def value; 2; end }\nBox.new.run\n")
    # The replacement was defined in driver.rb, outside source scope.
    assert len(trace.graph.edges) == 1 and trace.graph.edges[0].kind == "dynamic_c"
    assert trace.graph.edge_set() == {("Box#run", "Box#value")}


@pytest.mark.parametrize("ending,status", [('raise "driver failed"', "raised"), ('exit 0', "system_exit")])
def test_partial_driver_output_is_available_but_not_claimed_complete(tmp_path, ending, status):
    trace = traced(tmp_path, "class Box; attr_reader :value; def run; value; end; end",
                   "Box.new.run\n" + ending + "\n")
    assert trace.graph.edge_set() == {("Box#run", "Box#value")}
    assert not trace.metadata["completed"] and trace.metadata["driver_status"] == status
    assert trace.metadata["driver_error"] and "driver raised:" in trace.stderr


def test_legacy_mode_policy_is_explicit_and_invalid_scope_is_refused(tmp_path):
    trace = traced(tmp_path, "class Box; def run; leaf; end; def leaf; 1; end; end", "Box.new.run\n", include_c=False)
    assert trace.metadata["include_c"] is False and trace.metadata["events"] == ["call", "return"]
    assert trace.graph.edge_set() == {("Box#run", "Box#leaf")}
    with pytest.raises(RubyParseError):
        dyn_call_graph.trace_dynamic("absent", str(tmp_path / "driver.rb"), str(tmp_path))


def test_c_alias_uses_definition_name_and_never_the_alias_call_site_as_origin(tmp_path):
    trace = traced(tmp_path, "class Box; attr_reader :value; alias old_value value; def run; old_value; end; end", "Box.new.run\n")
    assert trace.graph.edge_set() == {("Box#run", "Box#value")}
    assert trace.graph.edges[0].kind == "dynamic_c"


def test_driver_edit_is_visible_without_claiming_a_complete_source_manifest(tmp_path):
    trace = traced(tmp_path, "class Box; def run; leaf; end; def leaf; 1; end; end",
                   'Box.new.run\nFile.open(__FILE__, "a") { |f| f.write("# edited\\n") }\n')
    assert trace.metadata["completed"]
    assert trace.metadata["driver_sha256_before"] != trace.metadata["driver_sha256_after"]

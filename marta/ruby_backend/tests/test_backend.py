"""Tests for the LanguageBackend interface + RubyBackend (item 9)."""
import asyncio

import pytest

from marta.ruby_backend import runner
from marta.ruby_backend.backend import LanguageBackend, RubyBackend
from marta.ruby_backend.ruby_ast import RubyParseError


# --- interface conformance (no toolchain) ---------------------------------- #
def test_ruby_backend_is_a_language_backend():
    assert isinstance(RubyBackend(), LanguageBackend)


def test_abstract_base_cannot_be_instantiated():
    with pytest.raises(TypeError):
        LanguageBackend()  # abstract methods unimplemented


def test_ruby_backend_implements_every_abstract_method():
    abstract = LanguageBackend.__abstractmethods__
    assert abstract  # sanity: the ABC actually declares some
    # RubyBackend overrides all of them (else it too would be abstract).
    assert not getattr(RubyBackend, "__abstractmethods__", frozenset())


def test_build_call_graph_returns_graph(tmp_path):
    f = tmp_path / "w.rb"
    f.write_text("class W\n  def a; b; end\n  def b; end\nend\n")
    try:
        g = RubyBackend().build_call_graph([str(f)])
    except RubyParseError:
        pytest.skip("no Ruby toolchain")
    assert g is not None
    assert "W#b" in g.callees("W#a")


def test_module_ref_strips_extension():
    assert RubyBackend().module_ref("foo/bar.rb") == "foo/bar"


def test_prompts_exposes_builders():
    p = RubyBackend().prompts
    for name in ("PLAN_SYS", "plan_user", "DEV_SYS", "dev_user", "get_ruby_code",
                 "build_context_block", "first_dev_instruction", "repair_dev_instruction"):
        assert hasattr(p, name)


def test_discover_files_excludes_tests(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "a.rb").write_text("class A; end")
    (tmp_path / "src" / "spec").mkdir()
    (tmp_path / "src" / "spec" / "a_spec.rb").write_text("x")
    files = RubyBackend().discover_files(str(tmp_path / "src"))
    assert [f.endswith("a.rb") for f in files] == [True]
    assert len(files) == 1  # spec/ excluded


# --- the loop actually routes through the backend -------------------------- #
def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


class SpyBackend(RubyBackend):
    """Wraps RubyBackend, recording which surface methods the flow calls."""

    def __init__(self):
        self.calls = []

    def syntax_check(self, source):
        self.calls.append("syntax_check")
        return super().syntax_check(source)

    def run_tests(self, test_path, load_paths, cwd):
        self.calls.append("run_tests")
        return super().run_tests(test_path, load_paths, cwd)


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_generation_uses_injected_backend(tmp_path):
    from marta.ruby_backend import generate

    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text("class Calc\n  def add(a, b) = a + b\nend\n")
    good = '''```ruby
require "calc"
RSpec.describe Calc do
  it "adds" do
    expect(Calc.new.add(2, 3)).to eq(5)
  end
end
```'''

    async def ask(system, user):
        return '[{"name":"a","desc":"x","setup":"None"}]' if "Test Plan" in system else good

    spy = SpyBackend()
    out = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc#add", describe_subject="Calc",
        method_source="def add(a, b) = a + b", require_target="calc",
        load_paths=["src"], spec_path="spec/add_spec.rb", cwd=str(tmp_path),
        ask=ask, backend=spy,
    ))
    assert out.success
    # The ReAct loop drove syntax_check and run_tests THROUGH the backend.
    assert "syntax_check" in spy.calls
    assert "run_tests" in spy.calls

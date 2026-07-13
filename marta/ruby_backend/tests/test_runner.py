"""Tests for the Ruby syntax check and RSpec runner.

Requires Ruby >= 3.3 and RSpec on the same toolchain (via $MARTA_RUBY_BIN /
$MARTA_RSPEC_BIN or PATH). Skips when unavailable.
"""
import os
import textwrap

import pytest

from marta.ruby_backend import runner
from marta.ruby_backend.ruby_ast import RubyParseError


def _toolchain_ok() -> bool:
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")


# --- syntax_check ---------------------------------------------------------- #
def test_syntax_ok():
    assert runner.syntax_check("class Foo\n  def bar = 1\nend\n") is None


def test_syntax_error_message():
    msg = runner.syntax_check("def broken(")
    assert msg is not None
    assert "SyntaxError" in msg or "syntax error" in msg.lower()


# --- run_rspec ------------------------------------------------------------- #
def _project(tmp_path):
    # Deliberately NOT under lib/ or spec/, which RSpec auto-adds to $LOAD_PATH.
    # Placing the code under src/ forces an explicit -I, exercising the
    # PYTHONPATH-analogue and the import-root concern from the benchmark.
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calculator.rb").write_text(
        "class Calculator\n  def add(a, b) = a + b\nend\n"
    )
    return tmp_path


def test_rspec_all_pass(tmp_path):
    p = _project(tmp_path)
    (p / "spec" / "calculator_spec.rb").write_text(textwrap.dedent("""
        require "calculator"
        RSpec.describe Calculator do
          it "adds" do
            expect(described_class.new.add(2, 3)).to eq(5)
          end
        end
    """))
    res = runner.run_rspec("spec/calculator_spec.rb", load_paths=["src"], cwd=str(p))
    assert res.all_passed
    assert len(res.examples) == 1
    assert list(res.results.values()) == ["passed"]
    assert not res.load_error


def test_rspec_mixed_results(tmp_path):
    p = _project(tmp_path)
    (p / "spec" / "calculator_spec.rb").write_text(textwrap.dedent("""
        require "calculator"
        RSpec.describe Calculator do
          it "adds" do
            expect(described_class.new.add(2, 3)).to eq(5)
          end
          it "wrong" do
            expect(described_class.new.add(2, 3)).to eq(99)
          end
        end
    """))
    res = runner.run_rspec("spec/calculator_spec.rb", load_paths=["src"], cwd=str(p))
    assert not res.all_passed
    statuses = {e.full_description: e.status for e in res.examples}
    assert statuses == {"Calculator adds": "passed", "Calculator wrong": "failed"}
    failed = res.failed
    assert len(failed) == 1
    assert "expected: 99" in (failed[0].message or "")


def test_rspec_load_error_without_load_path(tmp_path):
    # Same spec but no -I lib: the `require "calculator"` cannot resolve.
    p = _project(tmp_path)
    (p / "spec" / "calculator_spec.rb").write_text(textwrap.dedent("""
        require "calculator"
        RSpec.describe Calculator do
          it "adds" do
            expect(described_class.new.add(2, 3)).to eq(5)
          end
        end
    """))
    res = runner.run_rspec("spec/calculator_spec.rb", cwd=str(p))
    assert not res.all_passed
    assert res.load_error

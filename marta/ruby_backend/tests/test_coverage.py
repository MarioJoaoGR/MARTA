"""Tests for per-method coverage synthesis (Fase 2).

Pure synthesis logic is toolchain-free; the live coverage run needs Ruby/RSpec.
"""
import textwrap

import pytest

from marta.ruby_backend import coverage_runner as cov
from marta.ruby_backend import runner
from marta.ruby_backend.ruby_ast import MethodInfo, RubyParseError, parse_file


# --- format_missing_lines / synthesize (pure) ------------------------------ #
def test_format_missing_lines_ranges():
    mc = cov.MethodCoverage(missing_lines=[5, 6, 8, 9, 10, 12])
    assert mc.format_missing_lines() == "5-6, 8-10, 12"


def test_synthesize_intersects_range():
    # method spans lines 2..9; hit array (1-indexed via idx): lines 5,6,8 == 0
    lines = [1, 1, 1, 1, 0, 0, None, 0, None, None, None]
    m = MethodInfo(name="sign", owner="Calc", singleton=False, start_line=2, end_line=9)
    mc = cov.synthesize(m, lines)
    assert mc.missing_lines == [5, 6, 8]
    assert mc.covered_lines == 3           # lines 2,3,4
    assert mc.executable_lines == 6        # 2,3,4,5,6,8 (7,9 are nil/non-exec)
    assert not mc.fully_covered


def test_synthesize_fully_covered():
    lines = [1, 1, 1, None]
    m = MethodInfo(name="x", owner=None, singleton=False, start_line=1, end_line=4)
    mc = cov.synthesize(m, lines)
    assert mc.fully_covered
    assert mc.format_missing_lines() == ""


# --- live coverage run ----------------------------------------------------- #
def _toolchain_ok() -> bool:
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


@pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby/RSpec toolchain")
def test_run_line_coverage_and_synthesize(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "src" / "calc.rb").write_text(textwrap.dedent("""
        class Calc
          def sign(n)
            if n > 0
              "pos"
            elsif n < 0
              "neg"
            else
              "zero"
            end
          end
        end
    """).lstrip())
    # Spec exercises only the positive branch.
    (tmp_path / "spec" / "calc_spec.rb").write_text(textwrap.dedent("""
        require "calc"
        RSpec.describe Calc do
          it "pos" do
            expect(described_class.new.sign(5)).to eq("pos")
          end
        end
    """))

    result = cov.run_line_coverage("src", ["spec/calc_spec.rb"], cwd=str(tmp_path))
    assert "calc.rb" in result.files
    lines = result.files["calc.rb"]

    fp = parse_file(str(tmp_path / "src" / "calc.rb"))
    sign = next(m for m in fp.methods if m.name == "sign")
    mc = cov.synthesize(sign, lines)
    # neg and zero branches uncovered -> missing lines non-empty, not fully covered
    assert not mc.fully_covered
    assert mc.missing_lines  # the elsif/else bodies
    assert mc.covered_lines >= 2

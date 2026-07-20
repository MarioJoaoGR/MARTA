"""Tests for the Minitest backend: JSON runner, prompts, salvage, detection."""
import asyncio

import pytest

from marta.ruby_backend import generate, runner, salvage
from marta.ruby_backend.backend import MinitestBackend, RubyBackend, detect_backend
from marta.ruby_backend.ruby_ast import RubyParseError, parse_source


def _toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


needs_ruby = pytest.mark.skipif(not _toolchain_ok(), reason="no Ruby toolchain")

CALC = "class Calc\n  def add(a, b) = a + b\nend\n"


def _project(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "test").mkdir()
    (tmp_path / "src" / "calc.rb").write_text(CALC)
    return tmp_path


# --- runner ---------------------------------------------------------------- #
@needs_ruby
def test_minitest_runner_reports_pass_and_fail(tmp_path):
    p = _project(tmp_path)
    (p / "test" / "calc_test.rb").write_text(
        'require "minitest/autorun"\nrequire "calc"\n\n'
        "class CalcTest < Minitest::Test\n"
        "  def test_adds\n    assert_equal 5, Calc.new.add(2, 3)\n  end\n\n"
        "  def test_wrong\n    assert_equal 99, Calc.new.add(2, 3)\n  end\nend\n"
    )
    res = runner.run_minitest("test/calc_test.rb", load_paths=["src"], cwd=str(p))
    assert not res.all_passed
    statuses = {e.full_description: e.status for e in res.examples}
    assert statuses == {"CalcTest test_adds": "passed", "CalcTest test_wrong": "failed"}
    failed = res.failed[0]
    assert failed.line_number == 9          # points at `def test_wrong`
    assert "99" in (failed.message or "")


@needs_ruby
def test_minitest_runner_all_green(tmp_path):
    p = _project(tmp_path)
    (p / "test" / "calc_test.rb").write_text(
        'require "minitest/autorun"\nrequire "calc"\n\n'
        "class CalcTest < Minitest::Test\n"
        "  def test_adds\n    assert_equal 5, Calc.new.add(2, 3)\n  end\nend\n"
    )
    res = runner.run_minitest("test/calc_test.rb", load_paths=["src"], cwd=str(p))
    assert res.all_passed and not res.load_error


@needs_ruby
def test_minitest_runner_flags_load_error(tmp_path):
    p = _project(tmp_path)
    (p / "test" / "calc_test.rb").write_text(
        'require "minitest/autorun"\nrequire "nope_missing"\n'
    )
    res = runner.run_minitest("test/calc_test.rb", load_paths=["src"], cwd=str(p))
    assert not res.all_passed and res.load_error


# --- prompts --------------------------------------------------------------- #
def test_minitest_prompts_use_minitest_syntax():
    b = MinitestBackend()
    p = b.prompts.dev_user("instr", "def add; end", "calc", "Money::Bank::Base")
    assert "Minitest::Test" in p
    assert "MoneyBankBaseTest" in p          # class name derived from subject
    assert "assert_equal" in p
    assert "minitest/autorun" in p
    assert "expect(" not in p                # no RSpec syntax leaking in


def test_minitest_backend_shares_agnostic_planner():
    assert MinitestBackend().prompts.PLAN_SYS == RubyBackend().prompts.PLAN_SYS


# --- salvage --------------------------------------------------------------- #
@needs_ruby
def test_salvage_removes_failing_test_method():
    src = (
        'require "minitest/autorun"\n\n'
        "class CalcTest < Minitest::Test\n"
        "  def test_ok\n    assert true\n  end\n\n"
        "  def test_bad\n    assert false\n  end\nend\n"
    )
    methods = parse_source(src, "t.rb").methods
    out = salvage.salvage_minitest(src, methods, failed_lines=[8])
    assert out is not None
    trimmed, removed = out
    assert removed == 1
    assert "test_ok" in trimmed and "test_bad" not in trimmed


@needs_ruby
def test_salvage_none_when_all_tests_fail():
    src = (
        "class T < Minitest::Test\n"
        "  def test_a\n    assert false\n  end\n\n"
        "  def test_b\n    assert false\n  end\nend\n"
    )
    methods = parse_source(src, "t.rb").methods
    assert salvage.salvage_minitest(src, methods, failed_lines=[2, 6]) is None


# --- framework detection --------------------------------------------------- #
def test_detect_rspec_from_spec_dir(tmp_path):
    (tmp_path / "lib").mkdir()
    (tmp_path / "spec").mkdir()
    assert isinstance(detect_backend(str(tmp_path / "lib")), RubyBackend)


def test_detect_minitest_from_test_dir(tmp_path):
    (tmp_path / "lib").mkdir()
    (tmp_path / "test").mkdir()
    assert isinstance(detect_backend(str(tmp_path / "lib")), MinitestBackend)


def test_gemfile_breaks_the_tie(tmp_path):
    (tmp_path / "lib").mkdir()
    (tmp_path / "spec").mkdir()
    (tmp_path / "test").mkdir()          # ambiguous layout
    (tmp_path / "Gemfile").write_text('gem "rspec"\n')
    assert isinstance(detect_backend(str(tmp_path / "lib")), RubyBackend)


# --- end-to-end through the generation flow -------------------------------- #
@needs_ruby
def test_generation_end_to_end_with_minitest(tmp_path):
    p = _project(tmp_path)
    good = '''```ruby
require "minitest/autorun"
require "calc"

class CalcTest < Minitest::Test
  def test_adds
    assert_equal 5, Calc.new.add(2, 3)
  end
end
```'''

    async def ask(system, user):
        return '[{"name":"a","desc":"x","setup":"None"}]' if "Test Plan" in system else good

    out = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc#add", describe_subject="Calc",
        method_source="def add(a, b) = a + b", require_target="calc",
        load_paths=["src"], spec_path="marta_specs/calc_test.rb", cwd=str(p),
        ask=ask, backend=MinitestBackend(), max_attempts=1,
    ))
    assert out.success
    assert (p / "marta_specs" / "calc_test.rb").exists()

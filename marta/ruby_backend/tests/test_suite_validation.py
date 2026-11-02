"""Real RSpec regressions for suite acceptance, coverage and round interaction."""
import asyncio

import pytest

from marta.ruby_backend import coverage_runner, project, runner
from marta.ruby_backend.ruby_ast import RubyParseError


def toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


pytestmark = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


@pytest.mark.parametrize("source,accepted", [
    ('RSpec.describe("empty") {}', False),
    ('RSpec.describe("pending") { xit("later") {} }', False),
    ('RSpec.describe("mixed") { it("works") { expect(1).to eq(1) }; xit("later") {} }', True),
    ('RSpec.configure { |c| c.failure_exit_code = 0 }; '
     'RSpec.describe("masked") { it("works") { expect(1).to eq(1) }; '
     'it("fails") { expect(1).to eq(2) } }', False),
    ('RSpec.describe("interrupted") { it("works") { expect(1).to eq(1) }; '
     'it("stops") { exit(0) }; it("never runs") { expect(1).to eq(1) } }', False),
    ('RSpec.configure { |c| c.failure_exit_code = 0 }; '
     'RSpec.describe("load") { it("works") { expect(1).to eq(1) } }; '
     'raise "outside examples"', False),
])
def test_acceptance_uses_complete_report_not_only_process_status(tmp_path, source, accepted):
    spec = tmp_path / "candidate_spec.rb"
    spec.write_text(source)
    result = runner.run_rspec(str(spec), cwd=str(tmp_path))
    assert result.all_passed is accepted
    if not accepted:
        assert result.validation_error


def test_coverage_keeps_failing_observations_separate_from_suite_validity(tmp_path):
    (tmp_path / "calc.rb").write_text("class Calc\n  def self.double(n)\n    n * 2\n  end\nend\n")
    spec = tmp_path / "calc_spec.rb"
    spec.write_text('require "calc"; RSpec.configure { |c| c.failure_exit_code = 0 }; '
                    'RSpec.describe(Calc) { it("fails") { expect(Calc.double(2)).to eq(9) } }')
    measured = coverage_runner.run_line_coverage(".", [str(spec)], cwd=str(tmp_path), isolated=True)
    assert measured.files["calc.rb"]
    assert measured.suite_result is not None
    assert not measured.suite_result.all_passed
    assert measured.suite_result.failed
    assert measured.suite_result.exit_code == 0


SOURCE = """class Calc
  def self.sign(n)
    if n > 0
      :positive
    else
      :negative
    end
  end
end
"""
FIRST = """require "calc"
$marta_fixture_mode = :first
RSpec.describe Calc do
  it("positive") do
    expect(Calc.sign(1)).to eq(:positive)
    expect($marta_fixture_mode).to eq(:first)
  end
end
"""
SECOND = """require "calc"
$marta_fixture_mode = :second
RSpec.describe Calc do
  it("negative") do
    expect(Calc.sign(-1)).to eq(:negative)
    expect($marta_fixture_mode).to eq(:second)
  end
end
"""


def test_interacting_round_is_archived_without_losing_previous_valid_suite(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src/calc.rb").write_text(SOURCE)
    responses = iter(['[{"name":"sign", "desc":"exercise branch", "setup":"none"}]', FIRST,
                      '[{"name":"sign", "desc":"other branch", "setup":"none"}]', SECOND])
    calls = []
    async def ask(system, user):
        calls.append(user)
        return next(responses)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    outcomes = asyncio.run(obj.generate_rounds(rounds=2, max_attempts=1, ask=ask))
    assert len(calls) == 4  # Validation does not purchase another LLM attempt.
    assert outcomes[0].success
    assert not outcomes[1].success
    assert "accumulated" in outcomes[1].last_error.lower()
    retained = [tmp_path / p for p in obj._all_spec_paths()]
    assert len(retained) == 1 and retained[0].read_text().strip() == FIRST.strip()
    assert list((tmp_path / "rejected_specs").rglob("*.rb"))
    measured = obj.backend.run_coverage("src", [str(p) for p in retained], cwd=str(tmp_path))
    assert measured.suite_result.all_passed
    assert not obj.measure_coverage()[0].fully_covered


def valid_report():
    return {"examples": [{"id": "./spec.rb[1:1]", "status": "passed"}],
            "summary": {"example_count": 1, "failure_count": 0, "pending_count": 0,
                        "errors_outside_of_examples_count": 0}}


@pytest.mark.parametrize("data", [None, [], {}, {"examples": [], "summary": None}])
def test_missing_report_is_rejected_without_crashing(data):
    result = runner.rspec_result(data, 0)
    assert not result.all_passed and not result.report_valid
    assert result.validation_error


@pytest.mark.parametrize("change", ["count", "failures", "pending", "boolean_count", "missing_count",
                                    "duplicate", "missing_id", "bad_status", "bad_exception"])
def test_incomplete_or_contradictory_report_never_certifies_a_suite(change):
    data = valid_report()
    if change == "count":
        data["summary"]["example_count"] = 2
    elif change == "failures":
        data["summary"]["failure_count"] = 1
    elif change == "pending":
        data["summary"]["pending_count"] = 1
    elif change == "boolean_count":
        data["summary"]["example_count"] = True
    elif change == "missing_count":
        del data["summary"]["errors_outside_of_examples_count"]
    elif change == "duplicate":
        data["examples"] *= 2
        data["summary"]["example_count"] = 2
    elif change == "missing_id":
        del data["examples"][0]["id"]
    elif change == "bad_status":
        data["examples"][0]["status"] = []
    elif change == "bad_exception":
        data["examples"][0]["exception"] = "invalid"
    result = runner.rspec_result(data, 0)
    assert not result.all_passed and not result.report_valid


def test_valid_report_with_interruption_is_not_successful():
    result = runner.rspec_result(valid_report(), 0, interrupted=True)
    assert result.report_valid and not result.all_passed
    assert "interrupted" in result.validation_error


def test_preexisting_invalid_suite_is_preserved_and_requires_attention(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src/calc.rb").write_text(SOURCE)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    directory = tmp_path / "marta_specs"
    directory.mkdir()
    spec = directory / "preexisting_spec.rb"
    code = 'RSpec.describe("bad") { it("fails") { expect(1).to eq(2) } }'
    spec.write_text(code)
    with pytest.raises(coverage_runner.SuiteValidationError, match="accumulated"):
        obj._measure_retained_suite([])
    assert spec.read_text() == code
    assert not (tmp_path / "rejected_specs").exists()


def test_coverage_report_preserves_active_support_encoder_compatibility(tmp_path):
    package = tmp_path / "active_support"
    package.mkdir()
    (package / "json.rb").write_text("module ActiveSupport; module JSON; end; end")
    spec = tmp_path / "encoder_spec.rb"
    spec.write_text("""module ActiveSupport
  module ToJsonWithActiveSupportEncoder
    def to_json(*)
      raise NameError, 'missing encoder' unless defined?(ActiveSupport::JSON)
      ::JSON.generate(self)
    end
  end
end
Hash.prepend(ActiveSupport::ToJsonWithActiveSupportEncoder)
RSpec.describe 'encoding' do
  it('works') { expect(1).to eq(1) }
end
""")
    measured = coverage_runner.run_line_coverage(".", [str(spec)], cwd=str(tmp_path), isolated=True)
    assert measured.suite_result.all_passed
    assert measured.suite_result.report_valid

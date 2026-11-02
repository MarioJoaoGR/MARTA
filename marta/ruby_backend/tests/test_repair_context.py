"""Repair must see the actual previous test, effective plan and observed results."""
import asyncio
import json

import pytest

from marta.ruby_backend import generate, runner
from marta.ruby_backend.recorder import RubyRecorder
from marta.ruby_backend.ruby_ast import RubyParseError


def toolchain_ok():
    try:
        return runner.syntax_check("def x; end") is None
    except RubyParseError:
        return False


needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")
PLAN = '[{"name":"already works","desc":"positive value","setup":"real object"},' \
       '{"name":"other value","desc":"second value","setup":"real object"}]'
SOURCE = "class Calc\n  def self.double(n)\n    n * 2\n  end\nend\n"
BAD = '''require "calc"
RSpec.describe Calc do
  it("already works") { expect(Calc.double(2)).to eq(4) }
  it("other value") { expect(Calc.double(5)).to eq(99) }
end
'''
GOOD = BAD.replace("eq(99)", "eq(10)")


def run_flow(tmp_path, responses, attempts, recorder=None):
    (tmp_path / "src").mkdir()
    (tmp_path / "src/calc.rb").write_text(SOURCE)
    seen, queue = [], iter(responses)
    async def ask(system, user):
        seen.append((system, user))
        return PLAN if "Test Plan" in system else next(queue)
    outcome = asyncio.run(generate.generate_spec_for_method(
        method_qualified_name="Calc.double", describe_subject="Calc", method_source=SOURCE,
        require_target="calc", load_paths=["src"], spec_path="spec/double_spec.rb",
        cwd=str(tmp_path), ask=ask, max_attempts=attempts, recorder=recorder,
        error_help_fn=lambda error: "ERROR-RETRIEVAL-HELP"))
    return outcome, [user for system, user in seen if "Test Plan" not in system]


def section(text, label):
    return json.JSONDecoder().raw_decode(text.split(label + "\n", 1)[1])[0]


@needs_ruby
def test_execution_repair_carries_plan_complete_test_and_example_results(tmp_path):
    recorder = RubyRecorder(str(tmp_path / "events.jsonl"))
    outcome, seen = run_flow(tmp_path, [BAD, GOOD], 2, recorder)
    assert outcome.success and outcome.attempts == 2 and len(seen) == 2
    request = seen[1]
    assert BAD.strip() in request
    assert section(request, "ORIGINAL TEST PLAN:") == json.loads(PLAN)
    diagnosis = section(request, "CURRENT FAILURE:")
    assert diagnosis["stage"] == "rspec" and diagnosis["category"] == "assertion"
    assert diagnosis["attempt"] == 1 and diagnosis["report_valid"]
    assert diagnosis["counts"] == {"passed": 1, "failed": 1, "pending": 0}
    assert {e["status"] for e in diagnosis["examples"]} == {"passed", "failed"}
    assert "ERROR-RETRIEVAL-HELP" in request
    assert "Preserve passing examples and their meaningful assertions" in request
    events = [json.loads(line) for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    repair = next(e for e in events if e["tipo"] == "repair_context")
    assert repair["source_attempt"] == 1 and len(repair["plan_id"]) == 64


@needs_ruby
def test_syntax_repair_carries_the_broken_code_and_no_invented_execution_results(tmp_path):
    broken = 'require "calc"\nRSpec.describe Calc do\n it("broken") { expect( }\nend'
    outcome, seen = run_flow(tmp_path, [broken, GOOD], 2)
    assert outcome.success
    assert broken in seen[1]
    diagnosis = section(seen[1], "CURRENT FAILURE:")
    assert diagnosis["stage"] == "syntax" and diagnosis["category"] == "syntax"
    assert diagnosis["counts"] is None and diagnosis["examples"] == []


@needs_ruby
def test_empty_response_keeps_previous_nonempty_code_and_its_own_validation(tmp_path):
    outcome, seen = run_flow(tmp_path, [BAD, "", GOOD], 3)
    assert outcome.success and outcome.attempts == 3 and len(seen) == 3
    request = seen[2]
    assert BAD.strip() in request and "PREVIOUS TEST ATTEMPT: 1" in request
    failure = section(request, "CURRENT FAILURE:")
    validation = section(request, "PREVIOUS TEST VALIDATION:")
    assert failure["stage"] == "empty_response" and failure["attempt"] == 2
    assert validation["stage"] == "rspec" and validation["attempt"] == 1
    assert validation["counts"] == {"passed": 1, "failed": 1, "pending": 0}


@needs_ruby
def test_each_repair_uses_latest_nonempty_test_not_first_candidate(tmp_path):
    second = BAD.replace('it("other value")', 'it("changed candidate")').replace("eq(99)", "eq(98)")
    outcome, seen = run_flow(tmp_path, [BAD, second, GOOD], 3)
    assert outcome.success and len(seen) == 3
    assert second.strip() in seen[2] and BAD.strip() not in seen[2]
    assert "PREVIOUS TEST ATTEMPT: 2" in seen[2]


@needs_ruby
def test_initial_empty_candidate_still_has_plan_without_fake_previous_test(tmp_path):
    outcome, seen = run_flow(tmp_path, ["", GOOD], 2)
    assert outcome.success and len(seen) == 2
    assert "No non-empty test has been generated yet." in seen[1]
    assert section(seen[1], "ORIGINAL TEST PLAN:") == json.loads(PLAN)
    assert section(seen[1], "CURRENT FAILURE:")["stage"] == "empty_response"


@pytest.mark.parametrize("exception,category", [
    ("LoadError", "loading"), ("NameError", "missing_constant"),
    ("NoMethodError", "missing_method"), ("ArgumentError", "arguments"),
    ("TypeError", "type_error"),
    ("RSpec::Expectations::ExpectationNotMetError", "assertion"),
    ("RuntimeError", "execution"),
])
def test_diagnosis_uses_exception_class_not_words_in_the_error(exception, category):
    from marta.ruby_backend.repair import diagnose_result
    example = runner.ExampleResult("spec[1:1]", "case", "failed", 4,
                                   "NoMethodError LoadError expected", exception_class=exception)
    result = runner.RSpecResult(False, [example], report_valid=True, exit_code=1)
    diagnosis = diagnose_result(result, 2)
    assert diagnosis.category == category and diagnosis.stage == "rspec"
    assert diagnosis.counts == {"passed": 0, "failed": 1, "pending": 0}
    assert diagnosis.examples[0]["exception_class"] == exception


def test_timeout_and_invalid_report_do_not_invent_execution_counts():
    from marta.ruby_backend.repair import diagnose_result
    timeout = diagnose_result(runner.RSpecResult(False, output="time exceeded", timed_out=True), 1)
    assert timeout.category == "timeout" and timeout.counts is None
    invalid = diagnose_result(runner.RSpecResult(False, load_error=True,
                                               validation_error="missing JSON"), 2)
    assert invalid.category == "invalid_report" and invalid.counts is None
    assert invalid.examples == []


def test_different_failures_are_reported_as_mixed():
    from marta.ruby_backend.repair import diagnose_result
    examples = [runner.ExampleResult(str(i), "case", "failed", 2, "error", exception_class=kind)
                for i, kind in enumerate(("NoMethodError", "RSpec::Expectations::ExpectationNotMetError"))]
    diagnosis = diagnose_result(runner.RSpecResult(False, examples, report_valid=True, exit_code=1), 1)
    assert diagnosis.category == "mixed" and diagnosis.counts["failed"] == 2


def test_plan_identity_is_stable_and_changes_when_testing_objective_changes():
    from marta.ruby_backend.repair import FailureDiagnostic, RepairContext
    failure = FailureDiagnostic("syntax", "syntax", 1)
    first = RepairContext([{"name": "a", "desc": "positive"}], failure, "first code", 1)
    reordered = RepairContext([{"desc": "positive", "name": "a"}], failure, "second code", 2)
    changed = RepairContext([{"name": "a", "desc": "negative"}], failure, "first code", 1)
    assert first.plan_id == reordered.plan_id and first.code_id != reordered.code_id
    assert first.plan_id != changed.plan_id


@needs_ruby
def test_real_process_timeout_is_recorded_explicitly(tmp_path):
    spec = tmp_path / "slow_spec.rb"
    spec.write_text('RSpec.describe("slow") { it("waits") { sleep 30 } }')
    result = runner.run_rspec(str(spec), cwd=str(tmp_path), timeout=0.2)
    assert result.timed_out and not result.all_passed and not result.report_valid

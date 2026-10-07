import pytest
from deucalion.xrepotest_ir_audit import audit_task, summarize


def event(code, phase="dev_primeira", *, rnd=0, valid=False, stage="rspec"):
    return dict(tipo="generation_validation", ronda=rnd, fase=phase,
                etapa=stage, code=code, valid=valid)


def task(events, final="", *, passed=True):
    response = [final] if final else []
    row = {"test": response, "checks": [dict(invocation="CALL" in final, tests=passed, compilation=True)] if final else []}
    return audit_task({"task_id": 1, "function_name": "f", "file_path": "p/lib/f.rb"},
                      response, row, events, lambda code, name: "CALL" in code)


def test_discarded_failed_invocation_is_distinct_from_empty_model_output():
    discarded = task([event("CALL", valid=False)])
    empty = task([event("", stage="empty")])
    assert discarded["category"] == "no_tests_earlier_ir_positive"
    assert empty["category"] == "no_tests_no_earlier_ir"
    assert empty["empty_candidate_events"] == 1
    assert discarded["first_round_first_candidate_ir"] is True


def test_repair_and_salvage_losses_are_evidenced_and_not_double_counted():
    repaired = task([event("CALL"), event("other", "dev_reparacao", valid=True)], "other")
    salvaged = task([event("CALL"), event("CALL", "dev_reparacao"),
                     event("other", "salvage", valid=True)], "other")
    result = summarize([repaired, salvaged])
    assert result["accepted_round_ir_losses"] == {"repair": 1, "salvage": 1}
    assert result["first_to_final_transitions"] == {"positive_to_negative": 2}
    assert result["nonempty_ir_negative"] == 2
    assert result["final_pass_without_ir"] == 2


def test_recovery_in_later_round_preserves_final_ir_despite_round_loss():
    case = task([event("CALL"), event("other", "salvage", valid=True),
                 event("CALL", rnd=1, valid=True)], "other CALL")
    result = summarize([case])
    assert result["accepted_round_ir_losses"] == {"salvage": 1}
    assert result["final_negative_with_accepted_round_loss"] == 0
    assert result["final_ir_pct"] == 100


def test_first_candidate_includes_syntax_failure_not_only_rspec_and_no_other_round():
    case = task([event("CALL", stage="syntax"), event("other", "dev_reparacao", valid=True),
                 event("CALL", rnd=1, valid=True)], "CALL")
    assert case["first_candidate"]["stage"] == "syntax"
    assert case["first_round_first_candidate_ir"] is True
    assert task([event("CALL", rnd=1)], "CALL")["first_round_first_candidate_ir"] is None


def test_missing_telemetry_is_unknown_and_denominator_retains_no_tests():
    case = task([])
    assert case["any_candidate_ir"] is None
    assert case["category"] == "no_tests_missing_validation_telemetry"
    result = summarize([case, task([event("CALL", valid=True)], "CALL")])
    assert result["tasks"] == 2 and result["final_ir_pct"] == 50
    assert result["first_candidate_available"] == 1
    assert result["ir_among_nonempty_pct"] == 100


def test_failing_final_suite_with_ir_stays_in_metric():
    result = summarize([task([event("CALL", valid=True)], "CALL", passed=False)])
    assert result["final_ir_pct"] == 100
    assert result["final_pass_and_ir"] == 0


def test_refuses_export_mismatch_and_changed_official_ir():
    base = {"task_id": 1, "function_name": "f", "file_path": "p/lib/f.rb"}
    with pytest.raises(ValueError, match="suites differ"):
        audit_task(base, ["CALL"], {"test": ["other"]}, [], lambda code, name: True)
    with pytest.raises(ValueError, match="IR differs"):
        audit_task(base, ["CALL"], {"test": ["CALL"], "checks": [{"invocation": False}]}, [], lambda code, name: True)

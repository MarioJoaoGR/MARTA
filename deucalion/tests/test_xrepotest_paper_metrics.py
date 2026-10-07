import json
from pathlib import Path
import pytest
from deucalion.xrepotest_paper_metrics import summarize, report


def sample(tid, killed, total, *, passed=True, valid=True, covered=1, lines=2):
    return {"task_id": tid, "file_path": "project/lib/example.rb", "test": ["suite"],
            "checks": [{"compilation": True, "tests": passed, "invocation": True, "mutation": valid}],
            "coverage_stats": [{"covered_lines": covered, "total_lines": lines}],
            "mutation_scores": [{"killed_count": killed, "total_count": total}]}


def test_paper_macro_differs_from_pooled_and_missing_counts_zero():
    rows = [sample(1, 1, 1), sample(2, 0, 9), {"task_id": 3, "test": []}]
    result = summarize(rows)
    assert result["mutation"]["MS_pct"] == pytest.approx(100 / 3)
    assert result["mutation"]["MS_at_Pass_pct"] == 50
    assert result["mutation"]["pooled_killed_pct_diagnostic"] == 10
    assert result["mutation"]["valid_measurements"] == 2
    assert result["test_pass_pct"] == pytest.approx(200 / 3)
    assert result["focal_line_coverage_macro_pct"] == pytest.approx(100 / 3)
    assert result["no_tests"] == 1


def test_failed_or_unavailable_mutation_is_zero_ms_and_excluded_at_pass():
    rows = [sample(1, 1, 2), sample(2, 9, 10, passed=False),
            sample(3, 3, 4, valid=False), sample(4, 0, 0)]
    result = summarize(rows)["mutation"]
    assert result["MS_pct"] == 12.5
    assert result["MS_at_Pass_pct"] == 50
    assert result["passing_tasks"] == 3
    assert result["valid_measurements"] == 1
    assert result["passing_without_valid_measurement"] == 2
    assert result["killed"] == 1 and result["mutants"] == 2


def test_failing_suite_may_have_coverage_per_official_protocol():
    assert summarize([sample(1, 0, 0, passed=False, covered=2)]) ["focal_line_coverage_macro_pct"] == 100


@pytest.mark.parametrize("rows", [[], [{"task_id": 1, "test": []}]])
def test_empty_or_no_suite_has_finite_zero_metrics(rows):
    result = summarize(rows)
    assert result["mutation"]["MS_pct"] == 0
    assert result["mutation"]["MS_at_Pass_pct"] == 0
    assert result["compilation_pct"] == 0


@pytest.mark.parametrize("rows", [
    [sample(1, 0, 1), sample(1, 0, 1)],
    [dict(sample(1, 0, 1), test=["one", "two"])],
    [sample(1, 2, 1)], [sample(1, 0, 1, covered=3)],
    [{"task_id": 1, "test": [], "checks": [{"tests": True}]}],
])
def test_rejects_ambiguous_or_invalid_denominators(rows):
    with pytest.raises(ValueError):
        summarize(rows)


def test_report_pairs_exact_ids_and_keeps_provenance(tmp_path):
    tasks = tmp_path / "tasks"
    tasks.mkdir()
    for tid in (1, 2, 3):
        (tasks / (str(tid) + ".json")).write_text(json.dumps(sample(tid, 1, 2)))
    (tmp_path / "experiment.json").write_text(json.dumps({"mutation": True}))
    before = {p.name: p.read_bytes() for p in tasks.iterdir()}
    result = report(tmp_path, [3, 1])
    assert result["task_ids"] == [1, 3]
    assert result["summary"]["total_tasks"] == 2
    assert result["by_project"]["project"]["total_tasks"] == 2
    assert set(result["input_sha256"]) == {"1.json", "3.json"}
    assert result["evaluation_manifest"] == {"mutation": True}
    assert result["mutation_validity"].startswith("UNVERIFIED")
    assert before == {p.name: p.read_bytes() for p in tasks.iterdir()}
    for ids in ([1, 1], [4]):
        with pytest.raises(ValueError):
            report(tmp_path, ids)

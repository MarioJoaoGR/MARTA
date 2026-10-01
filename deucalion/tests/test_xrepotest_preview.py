import copy
import importlib.util
import json
from pathlib import Path

import pytest

from deucalion import xrepotest_preview as preview
from benchmark.xrepotest.tests.test_adapter import task, state
from benchmark.xrepotest.tests.test_cluster import fake_cluster


def metrics():
    path = Path('/Users/mario/.cache/marta-xrepotest/image-app/base/metrics.py')
    if not path.exists():
        pytest.skip("Official metric module not present in this local environment")
    spec = importlib.util.spec_from_file_location("official_metrics", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.calculate_summary


def test_snapshot_keeps_whole_project_and_empty_outputs_without_writing_generation(tmp_path):
    tasks = [task(0, path="capybara/lib/a.rb"), task(1, path="capybara/lib/a.rb"),
             task(2, path="grape/lib/b.rb")]
    generation = tmp_path / "generation"
    state(generation, 0, "complete", "RSpec.describe {}\n")
    state(generation, 1, "no_tests")
    state(generation, 2, "running")
    before = {str(p): p.read_bytes() for p in generation.rglob("*") if p.is_file()}
    selected, responses = preview.snapshot_projects(tasks, generation, {"capybara"})
    assert selected == tasks[:2]
    assert responses == [{"task_id": 0, "response": ["RSpec.describe {}\n"]},
                         {"task_id": 1, "response": []}]
    assert before == {str(p): p.read_bytes() for p in generation.rglob("*") if p.is_file()}


@pytest.mark.parametrize("status", ["running", "infrastructure_failure", "unknown"])
def test_project_with_unfinished_task_is_refused(tmp_path, status):
    state(tmp_path, 0, status)
    with pytest.raises(ValueError, match="unfinished"):
        preview.snapshot_projects([task(0)], tmp_path, {"repo"})


@pytest.mark.parametrize("projects", [set(), {"missing"}])
def test_unknown_or_empty_project_selection_is_refused(tmp_path, projects):
    with pytest.raises(ValueError, match="known"):
        preview.snapshot_projects([task(0)], tmp_path, projects)


def test_smaller_complete_project_is_measured_first_without_changing_task_set():
    tasks = [task(0, path="capybara/lib/a.rb"), task(1, path="capybara/lib/a.rb"),
             task(2, path="dotenv/lib/b.rb")]
    ordered = preview.evaluation_order(tasks)
    assert [t["task_id"] for t in ordered] == [2, 0, 1]
    assert set(t["task_id"] for t in ordered) == {0, 1, 2}


def test_summary_uses_official_denominator_including_no_tests_and_macro_coverage(tmp_path):
    tasks = [task(0, path="capybara/lib/a.rb"), task(1, path="capybara/lib/b.rb"),
             task(2, path="dotenv/lib/a.rb")]
    responses = [{"task_id": 0, "response": ["suite"]}, {"task_id": 1, "response": []},
                 {"task_id": 2, "response": ["failing suite"]}]
    for task_row, response in zip(tasks, responses):
        result = copy.deepcopy(task_row)
        passed = task_row["task_id"] == 0
        result.update(test=response["response"], checks=[{"compilation": True, "tests": passed,
                       "invocation": True}] if response["response"] else [],
                      coverage_stats=[{"covered_lines": 2, "total_lines": 4}]
                      if response["response"] else [])
        file = tmp_path / "tasks" / (str(task_row["task_id"]) + ".json")
        file.parent.mkdir(exist_ok=True)
        file.write_text(json.dumps(result))
    report = preview.write_summary(tmp_path, tasks, responses, metrics(), mutation=False)
    assert report["preliminary"] and report["no_tests"] == 1
    assert report["summary"]["total_samples"] == 3
    assert report["summary"]["compiled_rate"] == pytest.approx(200/3)
    assert report["summary"]["test_pass_rate"] == pytest.approx(100/3)
    assert report["summary"]["line_coverage"] == pytest.approx(100/3)
    assert report["by_project"]["capybara"]["line_coverage"] == 25
    assert "não medida" in (tmp_path / "presentation.md").read_text()
    assert "675 tarefas" in (tmp_path / "presentation.md").read_text()
    preview.project_checkpoint(tmp_path, tasks, "capybara", metrics())
    saved = json.loads((tmp_path / "project_summaries/capybara.json").read_text())
    assert saved["summary"]["total_samples"] == 2 and saved["no_tests"] == 1
    (tmp_path / "tasks/1.json").unlink()
    (tmp_path / "project_summaries/capybara.json").unlink()
    preview.project_checkpoint(tmp_path, tasks, "capybara", metrics())
    assert not (tmp_path / "project_summaries/capybara.json").exists()


def test_preview_wrapper_only_starts_cpu_evaluation_with_separate_paths(fake_cluster):
    import subprocess
    root, tmp, env = fake_cluster
    child = subprocess.run(["bash", str(root / "deucalion/run_xrepotest_preview_cpu.sh")],
                           env=env, capture_output=True, text=True, timeout=20)
    assert child.returncode == 0, child.stderr
    calls = [json.loads(line) for line in (tmp / "calls.jsonl").read_text().splitlines()]
    assert len(calls) == 2
    invocation = calls[-1]
    assert "/opt/marta/deucalion/xrepotest_preview.py" in invocation
    assert "--enable-mutation" not in invocation
    assert invocation[invocation.index("--projects") + 1] == "capybara,dotenv"
    assert "/data/xrepo/runs/new-experiment/previews/capybara_dotenv_20261001" in invocation
    assert not any("serve" in row or "benchmark.xrepotest.run" in row for row in calls)

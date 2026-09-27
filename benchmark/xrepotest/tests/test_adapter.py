"""Offline contract tests for the independent-task XRepoTest adapter.

All datasets and outputs are temporary. Ruby parsing/execution and model calls
are replaced at their external boundaries; no model or embedding is loaded.
"""
import asyncio
import copy
import hashlib
import json
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from benchmark.xrepotest import backend, protocol, run
from marta.ruby_backend.ruby_ast import ClassInfo, FileParse, MethodInfo
from marta.ruby_backend.runner import ExampleResult, RSpecResult


SOURCE = (
    "class Widget\n"
    "  def initialize\n"
    "    @value = 1\n"
    "  end\n"
    "  private def value\n"
    "    @value\n"
    "  end\n"
    "  def other\n"
    "    :other\n"
    "  end\n"
    "end\n"
)
SUITES = [
    'RSpec.describe "round zero" do\n  it("first") { expect(1).to eq(1) }\nend\n',
    'RSpec.describe "round one" do\n  it("second") { expect(2).to eq(2) }\nend\n',
]


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def task(tid=42, path="repo/lib/widget.rb", name="value", start=5, end=7,
         source=SOURCE):
    return {"task_id": tid, "file_path": path, "file_content": source,
            "function_name": name,
            "function_component": {"start_line": start, "end_line": end}}


def dataset(path, rows):
    return write(path, "\n".join(json.dumps(row) for row in rows) + "\n\n")


def state(root, tid, status, code=None):
    folder = root / "tasks" / str(tid)
    write(folder / "state.json", json.dumps({"task_id": tid, "status": status}))
    if code is not None:
        write(folder / "final_spec.rb", code)
    return folder


def snapshot(root):
    return {p.relative_to(root).as_posix(): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


def test_load_tasks_fixture_preserves_exact_ids_and_sorts(tmp_path):
    rows = [task(674), task(0), task(42)]
    loaded = protocol.load_tasks(dataset(tmp_path / "tasks.jsonl", rows), pinned=False)
    assert loaded == [rows[1], rows[2], rows[0]]


def test_load_tasks_retains_all_675_independent_tasks(tmp_path):
    # Identical focal methods still represent distinct official task IDs.
    rows = [task(i) for i in reversed(range(675))]
    loaded = protocol.load_tasks(dataset(tmp_path / "tasks.jsonl", rows), pinned=False)
    assert [row["task_id"] for row in loaded] == list(range(675))


@pytest.mark.parametrize("ids", [[1, 1], [True], [False], [1.0], ["1"]])
def test_load_tasks_rejects_duplicate_or_coerced_ids(tmp_path, ids):
    with pytest.raises(ValueError):
        protocol.load_tasks(dataset(tmp_path / "tasks.jsonl", [task(i) for i in ids]),
                            pinned=False)


def test_load_tasks_defaults_to_verifying_pinned_bytes(tmp_path):
    path = dataset(tmp_path / "tasks.jsonl", [task()])
    with pytest.raises(ValueError, match="pinned"):
        protocol.load_tasks(path)


@pytest.mark.parametrize("ids", [range(674), range(1, 676)])
def test_pinned_tasks_require_exact_official_id_set(tmp_path, monkeypatch, ids):
    path = dataset(tmp_path / "tasks.jsonl", [task(i) for i in ids])
    # Bypass only the release-byte gate to exercise the independent ID gate.
    monkeypatch.setattr(protocol, "DATA_SHA256", hashlib.sha256(path.read_bytes()).hexdigest())
    with pytest.raises(ValueError, match="0..674"):
        protocol.load_tasks(path)


@pytest.mark.parametrize("path", ["/repo/lib/a.rb", "repo/../a.rb", "a.rb"])
def test_load_tasks_rejects_unsafe_source_paths(tmp_path, path):
    with pytest.raises(ValueError):
        protocol.load_tasks(dataset(tmp_path / "tasks.jsonl", [task(path=path)]),
                            pinned=False)


@pytest.mark.parametrize("start,end", [(0, 1), (-1, 2), (7, 5)])
def test_load_tasks_rejects_invalid_inclusive_ranges(tmp_path, start, end):
    with pytest.raises(ValueError):
        protocol.load_tasks(dataset(tmp_path / "tasks.jsonl", [task(start=start, end=end)]),
                            pinned=False)


def test_selectors_preserve_identity_and_inclusive_coordinates():
    rows = [task(674, path="repo/subgem/lib/widget.rb"), task(0, start=8, end=10)]
    original = copy.deepcopy(rows)
    assert protocol.selectors(rows) == [
        {"task_id": 674, "file": "subgem/lib/widget.rb", "name": "value",
         "start_line": 5, "end_line": 7},
        {"task_id": 0, "file": "lib/widget.rb", "name": "value",
         "start_line": 8, "end_line": 10},
    ]
    assert rows == original


def test_inventory_includes_unselected_production_and_subgems_only(tmp_path):
    files = {"lib/widget.rb": SOURCE, "lib/nested/context.rb": "# context\n",
             "subgem/lib/helper.rb": "# subgem\n", "README.md": "Project intent",
             "subgem/README": "Subgem intent"}
    for rel, text in files.items():
        write(tmp_path / rel, text)
    excluded = ["spec/lib/a.rb", "vendor/gems/lib/a.rb", "test/lib/a.rb",
                "tests/lib/a.rb", "lib/fixtures/a.rb", "lib/examples/a.rb",
                "lib/templates/a.rb", ".git/lib/a.rb", "marta_specs/lib/a.rb",
                ".marta_ruby_cache/lib/a.rb", "script.rb", "spec/README.md",
                "vendor/README", ".marta_ruby_cache/README"]
    for rel in excluded:
        write(tmp_path / rel, "not production context")
    inv = protocol.source_inventory(tmp_path, [task()])
    assert inv["code_files"] == ["lib/nested/context.rb", "lib/widget.rb", "subgem/lib/helper.rb"]
    assert inv["load_paths"] == ["lib", "subgem/lib"]
    assert set(inv["input_hashes"]) == set(files)
    for rel, content in files.items():
        assert inv["input_hashes"][rel] == hashlib.sha256(content.encode()).hexdigest()
    for rel in excluded:
        write(tmp_path / rel, "changed old result")
    after = protocol.source_inventory(tmp_path, [task()])
    assert after["code_files"] == inv["code_files"]
    assert after["input_hashes"] == inv["input_hashes"]
    assert after["source_digest"] == inv["source_digest"]


@pytest.mark.parametrize("rel", ["lib/context.rb", "README.md", "subgem/README"])
def test_inventory_digest_changes_for_nonfocal_context(tmp_path, rel):
    write(tmp_path / "lib/widget.rb", SOURCE)
    write(tmp_path / rel, "before")
    before = protocol.source_inventory(tmp_path, [task()])
    write(tmp_path / rel, "after")
    after = protocol.source_inventory(tmp_path, [task()])
    assert before["source_digest"] != after["source_digest"]


@pytest.mark.parametrize("case", ["missing", "changed", "spec", "vendor"])
def test_inventory_refuses_missing_changed_or_excluded_focal_file(tmp_path, case):
    rel = f"{case}/lib/widget.rb" if case in {"spec", "vendor"} else "lib/widget.rb"
    if case != "missing":
        write(tmp_path / rel, "# changed" if case == "changed" else SOURCE)
    with pytest.raises(ValueError, match="42"):
        protocol.source_inventory(tmp_path, [task(path="repo/" + rel)])


@pytest.fixture
def config():
    return {"model": "local:test", "model_digest": "immutable-model-v1",
            "input_hashes": {"repo": "production-source-v1"},
            "generation": "independent-task", "context": "production-project"}


def test_guard_run_creates_manifest_and_preserves_compatible_resume(tmp_path, config):
    root = tmp_path / "new-run"
    protocol.guard_run(root, config)
    assert json.loads((root / "experiment.json").read_text()) == {"schema": protocol.SCHEMA, **config}
    state(root, 42, "complete", SUITES[0])
    before = snapshot(root)
    protocol.guard_run(root, copy.deepcopy(config))
    assert snapshot(root) == before


@pytest.mark.parametrize("change", [
    {"model": "different:model"}, {"model_digest": "replacement-weights"},
    {"input_hashes": {"repo": "edited-production-source"}},
])
def test_guard_run_refuses_changed_model_or_source_without_overwriting(tmp_path, config, change):
    protocol.guard_run(tmp_path, config)
    state(tmp_path, 42, "complete", SUITES[0])
    before = snapshot(tmp_path)
    with pytest.raises(ValueError):
        protocol.guard_run(tmp_path, {**config, **change})
    assert snapshot(tmp_path) == before


@pytest.mark.parametrize("old_path", ["processed.jsonl", ".marta_ruby_cache/analysis.json",
                                      "tasks/42/final_spec.rb"])
def test_guard_run_refuses_unmanifested_old_outputs_and_caches(tmp_path, config, old_path):
    write(tmp_path / old_path, "old experiment")
    before = snapshot(tmp_path)
    with pytest.raises(ValueError):
        protocol.guard_run(tmp_path, config)
    assert snapshot(tmp_path) == before


@pytest.mark.parametrize("status,code", [
    (None, None), ("running", SUITES[0]), ("failed", SUITES[0]),
    ("complete", None), ("complete", " \n\t"),
])
def test_export_refuses_unfinished_or_missing_suites_atomically(tmp_path, status, code):
    root = tmp_path / "run"
    state(root, 0, "complete", SUITES[0])
    if status is not None:
        state(root, 674, status, code)
    output = write(tmp_path / "processed.jsonl", "previous valid export\n")
    with pytest.raises(ValueError, match="674"):
        protocol.export_responses([task(0), task(674)], root, output)
    assert output.read_text() == "previous valid export\n"


def test_export_keeps_no_tests_in_denominator_and_ignores_stale_suite(tmp_path):
    root = tmp_path / "run"
    state(root, 42, "no_tests", "stale suite from an earlier attempt")
    output = tmp_path / "export/processed.jsonl"
    protocol.export_responses([task()], root, output)
    assert [json.loads(line) for line in output.read_text().splitlines()] == [
        {"task_id": 42, "response": []}]


def test_joined_rounds_export_as_one_final_suite(tmp_path):
    paths = [write(tmp_path / f"r{i}_spec.rb", text) for i, text in enumerate(SUITES)]
    code = backend.joined_specs(paths)
    assert code.count(SUITES[0]) == code.count(SUITES[1]) == 1
    assert code.index(SUITES[0]) < code.index(SUITES[1])
    root = tmp_path / "run"
    state(root, 674, "complete", code)
    state(root, 0, "no_tests")
    output = tmp_path / "processed.jsonl"
    protocol.export_responses([task(674), task(0)], root, output)
    assert [json.loads(line) for line in output.read_text().splitlines()] == [
        {"task_id": 674, "response": [code]}, {"task_id": 0, "response": []}]


def test_summary_checkpoint_reuses_exact_phase_and_prompts_after_restart(tmp_path):
    client = SimpleNamespace(aask=AsyncMock(return_value="summary"), last_call={})
    recorder = SimpleNamespace(fase_atual="implementation", evento=Mock())
    calls = tmp_path / "calls"
    first = run.SummaryCheckpoints(calls, client, recorder)
    assert asyncio.run(first("system", "source")) == "summary"
    client.aask.assert_awaited_once_with("system", "source")
    fresh_client = SimpleNamespace(aask=AsyncMock(side_effect=AssertionError("cache miss")),
                                   last_call=None)
    resumed = run.SummaryCheckpoints(calls, fresh_client, recorder)
    assert asyncio.run(resumed("system", "source")) == "summary"
    fresh_client.aask.assert_not_awaited()
    assert fresh_client.last_call.get("cache_hit") is True
    recorder.evento.assert_not_called()


@pytest.mark.parametrize("phase,system,user", [
    ("requirements", "system", "source"),
    ("implementation", "changed system", "source"),
    ("implementation", "system", "changed source"),
])
def test_summary_checkpoint_does_not_cross_phase_or_prompt_boundaries(tmp_path, phase, system, user):
    client = SimpleNamespace(aask=AsyncMock(side_effect=["first", "second"]), last_call={})
    recorder = SimpleNamespace(fase_atual="implementation", evento=Mock())
    cached = run.SummaryCheckpoints(tmp_path, client, recorder)
    assert asyncio.run(cached("system", "source")) == "first"
    recorder.fase_atual = phase
    assert asyncio.run(cached(system, user)) == "second"
    assert client.aask.await_count == 2


@pytest.mark.parametrize("response,detail", [
    (None, {}), ("", {}), (" \n\t", {}),
    ("partial", {"erro": "transport failed"}),
    ("partial", {"finish_reason": "length"}),
])
def test_failed_or_truncated_summaries_are_not_checkpointed(tmp_path, response, detail):
    client = SimpleNamespace(aask=AsyncMock(return_value=response), last_call=detail)
    recorder = SimpleNamespace(fase_atual="implementation", evento=Mock())
    cached = run.SummaryCheckpoints(tmp_path, client, recorder)
    with pytest.raises(RuntimeError):
        asyncio.run(cached("system", "source"))
    assert not list(tmp_path.rglob("*.json"))
    assert recorder.evento.called
    client.aask.return_value, client.last_call = "recovered summary", {}
    assert asyncio.run(cached("system", "source")) == "recovered summary"
    assert client.aask.await_count == 2


def test_exception_from_summary_client_is_not_cached(tmp_path):
    client = SimpleNamespace(aask=AsyncMock(side_effect=TimeoutError("offline timeout")),
                             last_call={})
    recorder = SimpleNamespace(fase_atual="implementation", evento=Mock())
    with pytest.raises(TimeoutError):
        asyncio.run(run.SummaryCheckpoints(tmp_path, client, recorder)("system", "source"))
    assert not list(tmp_path.rglob("*.json"))


@pytest.mark.parametrize("phase,reused", [("sumarios_passagem1", True),
                                         ("sumarios_passagem2", False)])
def test_shared_summary_cache_reuses_only_source_only_phase(tmp_path, phase, reused):
    shared, local = tmp_path / "normal/calls", tmp_path / "ablation/calls"
    recorder = SimpleNamespace(fase_atual=phase, evento=Mock())
    producer = SimpleNamespace(aask=AsyncMock(return_value="normal summary"), last_call={})
    assert asyncio.run(run.SummaryCheckpoints(shared, producer, recorder)(
        "system", "same source")) == "normal summary"
    before = snapshot(shared)
    consumer = SimpleNamespace(aask=AsyncMock(return_value="ablation summary"), last_call={})
    cached = run.SummaryCheckpoints(local, consumer, recorder, shared_root=shared)
    assert asyncio.run(cached("system", "same source")) == (
        "normal summary" if reused else "ablation summary")
    assert consumer.aask.await_count == (0 if reused else 1)
    assert snapshot(shared) == before


@pytest.mark.parametrize("statuses,runner_passed,expected", [
    ([], True, False), (["pending"], True, False),
    (["passed"], True, True), (["passed", "failed"], False, False),
    (["passed"], False, False),
])
def test_backend_stages_official_spec_and_requires_a_passing_example(
        tmp_path, monkeypatch, statuses, runner_passed, expected):
    source = write(tmp_path / "generated/r0_spec.rb", SUITES[0])
    result = RSpecResult(runner_passed, [
        ExampleResult(str(i), "example", status, i + 1, None)
        for i, status in enumerate(statuses)])
    execute = Mock(return_value=result)
    monkeypatch.setattr(backend.runner, "run_rspec", execute)
    actual = backend.XRepoBackend().run_tests("generated/r0_spec.rb", ["lib"], str(tmp_path))
    assert actual is result
    assert actual.all_passed is expected
    staged = tmp_path / "spec/temp_spec.rb"
    assert staged.read_text() == source.read_text()
    execute.assert_called_once_with(str(staged), cwd=str(tmp_path), use_bundle=True,
                                    isolated=False, use_guard=False)


@pytest.mark.parametrize("hidden", ["extra", "backend"])
def test_backend_rejects_hidden_requires_before_staging(tmp_path, monkeypatch, hidden):
    adapter = backend.XRepoBackend()
    if hidden == "backend":
        adapter.requires = ["secret_helper"]
    execute = Mock(side_effect=AssertionError("must not run"))
    monkeypatch.setattr(backend.runner, "run_rspec", execute)
    with pytest.raises(ValueError, match="requires"):
        adapter.run_tests("missing.rb", ["lib"], str(tmp_path),
                          requires_extra=["secret_helper"] if hidden == "extra" else None)
    execute.assert_not_called()
    assert not (tmp_path / "spec/temp_spec.rb").exists()


def test_backend_coverage_runs_accumulated_suite_at_same_evaluator_path(tmp_path, monkeypatch):
    paths = [write(tmp_path / f"generated/r{i}_spec.rb", text) for i, text in enumerate(SUITES)]
    result = object()
    measure = Mock(return_value=result)
    monkeypatch.setattr(backend.coverage_runner, "run_line_coverage", measure)
    assert backend.XRepoBackend().run_coverage(
        ".", [str(paths[0].relative_to(tmp_path)), str(paths[1])], str(tmp_path)) is result
    staged = tmp_path / "spec/temp_spec.rb"
    assert staged.read_text() == backend.joined_specs(paths)
    measure.assert_called_once_with(".", [str(staged)], cwd=str(tmp_path),
                                    isolated=False, use_bundle=True)


def test_workspace_replaces_prior_task_edits_and_preserves_source(tmp_path):
    source, first, second = (tmp_path / name for name in ("source", "task42", "task674"))
    write(source / "lib/widget.rb", SOURCE)
    write(source / "vendor/bundle/installed.gemspec", "installed dependency")
    before = snapshot(source)
    run.workspace(source, first)
    write(first / "lib/widget.rb", "task-specific edit")
    write(first / "leftover.rb", "old workspace output")
    run.workspace(source, second)
    assert (second / "lib/widget.rb").read_text() == SOURCE
    assert not (second / "leftover.rb").exists()
    assert (second / "vendor").resolve() == (source / "vendor").resolve()
    run.workspace(source, first)
    assert (first / "lib/widget.rb").read_text() == SOURCE
    assert not (first / "leftover.rb").exists()
    assert snapshot(source) == before


@pytest.mark.parametrize("old_path", ["marta_specs/answer.rb", "coverage/result.json",
                                      ".marta_ruby_cache/analysis_old.json"])
def test_workspace_excludes_old_outputs_and_analysis_cache(tmp_path, old_path):
    source, destination = tmp_path / "source", tmp_path / "work"
    write(source / "lib/widget.rb", SOURCE)
    write(source / old_path, "old experiment")
    run.workspace(source, destination)
    assert not (destination / old_path).exists()
    assert (source / old_path).read_text() == "old experiment"


def test_workspace_refuses_unmarked_existing_directory_without_deleting_it(tmp_path):
    source, destination = tmp_path / "source", tmp_path / "unrelated"
    write(source / "lib/widget.rb", SOURCE)
    write(destination / "important.txt", "unrelated work")
    before = snapshot(tmp_path)
    with pytest.raises(ValueError):
        run.workspace(source, destination)
    assert snapshot(tmp_path) == before


@pytest.mark.parametrize("relationship", ["same", "child", "parent"])
def test_workspace_refuses_overlapping_source_and_destination(tmp_path, relationship):
    source = tmp_path / "source"
    write(source / "lib/widget.rb", SOURCE)
    destination = {"same": source, "child": source / "work", "parent": tmp_path}[relationship]
    before = snapshot(tmp_path)
    with pytest.raises(ValueError):
        run.workspace(source, destination)
    assert snapshot(tmp_path) == before


def test_project_never_retrieves_another_tasks_passing_spec(tmp_path):
    old = write(tmp_path / "old/answer_spec.rb", SUITES[0])
    target = SimpleNamespace(spec_path=str(old), spec_path_for_round=lambda _: str(old))
    project = backend.XRepoProject(root_dir=str(tmp_path), source_dir=".")
    assert project._example_passing_spec(target) is None


@pytest.fixture
def parsed_repo(tmp_path, monkeypatch):
    """Fixed Prism output, including duplicate names and a private definition.

    Coordinates are literal source positions, not calculated by the selector
    implementation. The unselected helper must remain in production context.
    """
    root = tmp_path / "repos/repo"
    write(root / "lib/widget.rb", SOURCE)
    other = "class Helper\n  def value\n    :helper\n  end\nend\n"
    write(root / "lib/helper.rb", other)
    parsed = {
        "widget.rb": FileParse(str(root / "lib/widget.rb"), classes=[
            ClassInfo("Widget", "Widget", "class", None, 1, 11)], methods=[
                MethodInfo("initialize", "Widget", False, 2, 4),
                MethodInfo("value", "Widget", False, 5, 7),
                MethodInfo("other", "Widget", False, 8, 10)]),
        "helper.rb": FileParse(str(root / "lib/helper.rb"), classes=[
            ClassInfo("Helper", "Helper", "class", None, 1, 5)], methods=[
                MethodInfo("value", "Helper", False, 2, 4)]),
    }
    monkeypatch.setattr(backend.XRepoBackend, "parse_file",
                        lambda self, path: copy.deepcopy(parsed[Path(path).name]))
    monkeypatch.setattr(backend.XRepoBackend, "build_call_graph", lambda *a, **k: None)
    return root


def discover(root, output, rows):
    inventory = protocol.source_inventory(root, rows)
    return backend.XRepoProject(
        root_dir=str(root), source_dir=".", output_root=str(output),
        code_files=inventory["code_files"], load_paths=inventory["load_paths"],
        full_context=True, target_selectors=protocol.selectors(rows),
        backend=backend.XRepoBackend()).discover()


def test_discovery_selects_private_method_by_exact_coordinates_and_keeps_context(parsed_repo, tmp_path):
    project = discover(parsed_repo, tmp_path / "analysis", [task(674)])
    assert len(project.targets) == 1
    target = project.targets[0]
    assert target.task_id == 674
    assert target.source_rel == "lib/widget.rb"
    assert target.method.qualified_name == "Widget#value"
    assert (target.method.start_line, target.method.end_line) == (5, 7)
    assert "  private def value\n    @value\n  end" in target.context_source
    assert {t.method.qualified_name for t in project.analysis_targets} >= {
        "Widget#initialize", "Widget#value", "Widget#other", "Helper#value"}


@pytest.mark.parametrize("change", [{"start": 4}, {"end": 8}, {"name": "absent"}])
def test_discovery_refuses_nonexact_selector_instead_of_dropping_task(parsed_repo, tmp_path, change):
    with pytest.raises(ValueError):
        discover(parsed_repo, tmp_path / "analysis", [task(**change)])


def test_all_675_ids_remain_independent_even_for_the_same_focal_method(parsed_repo, tmp_path):
    project = discover(parsed_repo, tmp_path / "analysis", [task(i) for i in range(675)])
    assert [target.task_id for target in project.targets] == list(range(675))
    assert len({id(target) for target in project.targets}) == 675
    assert len({target.spec_path_for_round(0) for target in project.targets}) == 675
    assert len(project.analysis_targets) == 4


def test_pipeline_isolates_task_rounds_and_resumes_without_generation(parsed_repo, tmp_path, monkeypatch):
    # Exercise real discovery, workspaces, final-state writes and export. Only
    # model/embedding work and generation's Ruby subprocesses are substituted.
    rows = [task(42), task(674, name="other", start=8, end=10)]
    inventories = {"repo": protocol.source_inventory(parsed_repo, rows)}
    model = SimpleNamespace(temperature=None,
                            aask=AsyncMock(side_effect=AssertionError("no live model calls")),
                            last_call={})
    fake_gpt = ModuleType("marta.gptapi")
    fake_gpt.model = model
    monkeypatch.setitem(sys.modules, "marta.gptapi", fake_gpt)
    analyzed, generated = [], []

    async def analyze(self, **kwargs):
        analyzed.append({t.method.qualified_name for t in self.analysis_targets})

    async def generate(self, **kwargs):
        assert len(self.targets) == 1
        target = self.targets[0]
        work, output = Path(self.root_dir), Path(self.output_root)
        assert output == args.output / "tasks" / str(target.task_id)
        assert work == args.work / "tasks" / str(target.task_id) / "repo"
        assert Path(target.spec_dir).is_relative_to(output)
        assert (work / "lib/widget.rb").read_text() == SOURCE
        assert not self._all_spec_paths(), "another task's specs leaked into this task"
        assert self._example_passing_spec(target) is None
        # Workspace edits must not contaminate the next task or image sources.
        write(work / "lib/widget.rb", "# edited in this task only")
        for i, code in enumerate(SUITES):
            write(Path(target.spec_path_for_round(i)), f"# task {target.task_id}\n{code}")
        generated.append(target.task_id)

    monkeypatch.setattr(backend.XRepoProject, "analyze_summaries", analyze)
    monkeypatch.setattr(backend.XRepoProject, "build_rag", lambda self: None)
    monkeypatch.setattr(backend.XRepoProject, "generate_rounds", generate)
    args = SimpleNamespace(repos=parsed_repo.parent, output=tmp_path / "output",
                           work=tmp_path / "work", temperature=0.0, no_graph=True,
                           rounds=2, attempts=1, reuse_analysis_from=None)
    asyncio.run(run.pipeline(args, rows, inventories))
    assert generated == [42, 674]
    assert analyzed == [{"Widget#initialize", "Widget#value", "Widget#other", "Helper#value"}]
    assert (parsed_repo / "lib/widget.rb").read_text() == SOURCE
    records = [json.loads(line) for line in (args.output / "processed.jsonl").read_text().splitlines()]
    assert [record["task_id"] for record in records] == [42, 674]
    for record in records:
        assert len(record["response"]) == 1
        code = record["response"][0]
        assert all(suite in code for suite in SUITES)
        sibling = 674 if record["task_id"] == 42 else 42
        assert f"# task {sibling}\n" not in code
        folder = args.output / "tasks" / str(record["task_id"])
        assert json.loads((folder / "state.json").read_text())["status"] == "complete"
    before = snapshot(args.output / "tasks")
    asyncio.run(run.pipeline(args, rows, inventories))
    assert generated == [42, 674]
    assert snapshot(args.output / "tasks") == before
    model.aask.assert_not_awaited()

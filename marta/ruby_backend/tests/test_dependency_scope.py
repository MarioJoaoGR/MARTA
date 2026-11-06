"""Dependency declarations must not come from MARTA's generated output trees."""
import asyncio
import json
from types import SimpleNamespace
from pathlib import Path

import pytest

from marta.ruby_backend import checkpoints, evaluation, execution, project
from marta.ruby_backend.tests.test_generate import _make_project, PLAN_RESPONSE, GOOD_SPEC
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def write(root, name, text="pins"):
    p = root / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    return p


def test_result_archives_do_not_become_dependency_declarations(tmp_path):
    write(tmp_path, "Gemfile")
    write(tmp_path, "component/Gemfile.lock")
    write(tmp_path, "run_results/old-repo/Gemfile.lock")
    actual = {Path(p).relative_to(tmp_path).as_posix() for p in checkpoints.dependency_files(tmp_path)}
    assert actual == {"Gemfile", "component/Gemfile.lock"}


@needs_ruby
def test_nested_custom_output_is_not_an_input_missing_from_the_workspace(tmp_path):
    _make_project(tmp_path)
    output = tmp_path / "artifacts"
    archived = write(output, "old-copy/Gemfile.lock")
    obj = project.RubyProject(str(tmp_path), "src", output_root=str(output), isolate_execution=True).discover()
    with execution.GenerationWorkspace(obj) as workspace:
        workspace.ensure()
        workspace.verify_inputs()
        assert archived.resolve() not in workspace.inputs


def test_output_exclusion_is_exact_and_preserves_real_subproject_declarations(tmp_path):
    write(tmp_path, "Gemfile")
    write(tmp_path, "artifacts/current/old/Gemfile.lock")
    write(tmp_path, "artifacts/current_extra/real.gemspec")
    write(tmp_path, "packages/component/run_results/Gemfile.lock")
    actual = {Path(p).relative_to(tmp_path).as_posix() for p in checkpoints.dependency_files(
        tmp_path, output_root=tmp_path / "artifacts/current")}
    assert actual == {"Gemfile", "artifacts/current_extra/real.gemspec",
                      "packages/component/run_results/Gemfile.lock"}


@pytest.mark.parametrize("where", [None, "root", "ancestor", "external"])
def test_output_at_root_or_outside_never_excludes_the_real_project(tmp_path, where):
    wanted = write(tmp_path, "Gemfile.lock")
    roots = {None: None, "root": tmp_path, "ancestor": tmp_path.parent,
             "external": tmp_path.parent / "external-output"}
    assert checkpoints.dependency_files(tmp_path, output_root=roots[where]) == [str(wanted)]


def test_owned_trees_are_pruned_before_descent_not_filtered_after_a_full_walk(tmp_path, monkeypatch):
    write(tmp_path, "run_results/large/archive/Gemfile")
    write(tmp_path, "outputs/current/large/Gemfile")
    write(tmp_path, "component/Gemfile")
    visited = []
    real_walk = checkpoints.os.walk
    def walk(root):
        for item in real_walk(root):
            visited.append(Path(item[0]).relative_to(tmp_path).as_posix())
            yield item
    monkeypatch.setattr(checkpoints.os, "walk", walk)
    checkpoints.dependency_files(tmp_path, output_root=tmp_path / "outputs/current")
    assert set(visited) == {".", "outputs", "component"}


@pytest.mark.parametrize("alias", [False, True])
def test_relative_or_symlinked_project_roots_still_exclude_the_same_output(tmp_path, monkeypatch, alias):
    root = tmp_path / "repo"; root.mkdir()
    write(root, "Gemfile")
    write(root, "output/archive/Gemfile.lock")
    if alias:
        (tmp_path / "alias").symlink_to(root, target_is_directory=True)
    monkeypatch.chdir(tmp_path)
    name = "alias" if alias else "repo"
    result = checkpoints.dependency_files(name, output_root=root / "output")
    assert result == [str(Path(name) / "Gemfile")]


@needs_ruby
def test_archived_dependencies_do_not_buy_another_attempt_on_resume(tmp_path):
    _make_project(tmp_path)
    obj = project.RubyProject(str(tmp_path), "src").discover()
    calls, queue = [], iter([PLAN_RESPONSE, GOOD_SPEC])
    async def ask(system, user):
        calls.append(user)
        assert len(calls) <= 2, "output-only changes must not buy another model attempt"
        return next(queue)
    first = asyncio.run(obj.generate_rounds(rounds=1, ask=ask))
    assert first[0].success and len(calls) == 2
    archive = write(tmp_path, "run_results/old-copy/Gemfile.lock")
    assert asyncio.run(obj.generate_rounds(rounds=1, ask=ask)) == []
    assert len(calls) == 2 and archive.is_file()
    assert not list((tmp_path / "rejected_specs").glob("resume_*/rounds.json"))


@needs_ruby
def test_real_dependency_changes_still_change_the_generation_recipe(tmp_path):
    _make_project(tmp_path)
    output = tmp_path / "out"
    obj = project.RubyProject(str(tmp_path), "src", output_root=str(output)).discover()
    targets = list(enumerate(obj.targets))
    before = obj._generation_recipe(targets, None, 1, False)
    write(output, "archive/Gemfile.lock", "generated pins")
    assert obj._generation_recipe(targets, None, 1, False) == before
    real = write(tmp_path, "component/Gemfile.lock", "real pins")
    changed = obj._generation_recipe(targets, None, 1, False)
    assert changed["dependency_policy"] == checkpoints.DEPENDENCY_POLICY
    assert changed["dependencies"]["component/Gemfile.lock"] == checkpoints.file_hash(real)
    assert changed != before


def test_evaluation_copy_preserves_nested_resources_and_omits_root_archives(tmp_path):
    root = tmp_path / "repo"; root.mkdir()
    write(root, "run_results/old/Gemfile")
    write(root, "rejected_specs/old.rb")
    write(root, "output/archive/Gemfile")
    write(root, "component/run_results/Gemfile")
    write(root, "component/marta_specs/resource.txt")
    obj = SimpleNamespace(root_dir=str(root), out_root=lambda: str(root / "output"))
    destination = tmp_path / "copy"
    evaluation._copy_workspace(obj, destination)
    actual = {p.relative_to(destination).as_posix() for p in destination.rglob("*") if p.is_file()}
    assert actual == {"component/run_results/Gemfile", "component/marta_specs/resource.txt"}


@needs_ruby
def test_evaluation_manifest_uses_the_same_declaration_scope(tmp_path):
    _make_project(tmp_path)
    output = tmp_path / "out"
    real = write(tmp_path, "component/Gemfile.lock")
    write(tmp_path, "run_results/old/Gemfile.lock")
    write(output, "archive/Gemfile")
    obj = project.RubyProject(str(tmp_path), "src", output_root=str(output)).discover()
    report = evaluation.evaluate_project(obj)
    manifest = json.loads((report.parent / "manifest.json").read_text())
    assert manifest["dependency_policy"] == checkpoints.DEPENDENCY_POLICY
    assert str(real) in manifest["inputs"]
    assert not any("old/Gemfile" in name or "archive/Gemfile" in name for name in manifest["inputs"])
    assert "checkpoints.py" in manifest["implementation"]

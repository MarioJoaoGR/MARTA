"""Project-bound README context and cache/prompt consistency; no live model."""
import asyncio
import hashlib
import json
from pathlib import Path

import pytest

from marta.ruby_backend import project, readme
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok


def source_file(root, relative="lib/nested/calc.rb"):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("class Calc\n  def add(a, b); a + b; end\nend\n")
    return path


def test_source_boundary_remains_compatible_but_project_scope_finds_root(tmp_path):
    file = source_file(tmp_path)
    (tmp_path / "README.md").write_text("project requirements")
    assert readme.nearest_readme(str(file), str(tmp_path / "lib")) is None
    assert readme.nearest_readme(str(file), str(tmp_path / "lib"), project_root=str(tmp_path)) == str(tmp_path / "README.md")


def test_nearest_monorepo_document_wins_then_falls_back_to_project_root(tmp_path):
    root = tmp_path
    specific = source_file(root, "packages/payments/lib/payment.rb")
    other = source_file(root, "packages/accounts/lib/account.rb")
    (root / "README.md").write_text("whole project")
    local = root / "packages/payments/README.md"
    local.write_text("payments component")
    assert readme.nearest_readme(str(specific), str(specific.parent), project_root=str(root)) == str(local)
    assert readme.nearest_readme(str(other), str(other.parent), project_root=str(root)) == str(root / "README.md")


def test_no_readme_is_taken_from_outside_project_even_when_none_exists_inside(tmp_path):
    (tmp_path / "README.md").write_text("unrelated parent project")
    root = tmp_path / "project"
    file = source_file(root)
    assert readme.nearest_readme(str(file), str(root / "lib"), project_root=str(root)) is None
    outsider = source_file(tmp_path / "outside")
    assert readme.nearest_readme(str(outsider), str(root / "lib"), project_root=str(root)) is None


def test_symlink_to_external_readme_is_not_used_as_project_context(tmp_path):
    root = tmp_path / "project"
    file = source_file(root)
    external = tmp_path / "outside.md"
    external.write_text("external project context")
    (file.parent / "README.md").symlink_to(external)
    assert readme.nearest_readme(str(file), str(root / "lib"), project_root=str(root)) is None
    (root / "README.md").write_text("valid fallback")
    assert readme.nearest_readme(str(file), str(root / "lib"), project_root=str(root)) == str(root / "README.md")


def test_document_names_keep_the_existing_priority(tmp_path):
    file = source_file(tmp_path)
    for name in reversed(readme.README_NAMES):
        (tmp_path / name).write_text(name)
    assert readme.nearest_readme(str(file), str(tmp_path / "lib"), project_root=str(tmp_path)) == str(tmp_path / "README.md")


def test_snapshot_hashes_the_exact_utf8_bytes_later_given_to_the_model(tmp_path):
    file = source_file(tmp_path)
    data = "Requisitos: ação\r\nsegunda linha\r\n".encode("utf-8")
    path = tmp_path / "README.md"
    path.write_bytes(data)
    snapshot = readme.ReadmeOverviewCache(str(tmp_path / "lib"), project_root=str(tmp_path))
    manifest = snapshot.manifest_for([str(file)])
    assert manifest == {"lib/nested/calc.rb": {"path": "README.md", "sha256": hashlib.sha256(data).hexdigest()}}
    path.write_text("changed after snapshot")
    calls = []
    async def ask(system, user):
        calls.append(user)
        return "overview"
    assert asyncio.run(snapshot.overview_for(ask, str(file))) == "overview"
    assert data.decode("utf-8") in calls[0]
    assert "changed after snapshot" not in calls[0]
    assert snapshot.manifest_for([str(file)]) == manifest
    fresh = readme.ReadmeOverviewCache(str(tmp_path / "lib"), project_root=str(tmp_path))
    assert fresh.manifest_for([str(file)]) != manifest


def test_snapshot_preserves_a_missing_readme_until_next_analysis(tmp_path):
    file = source_file(tmp_path)
    snapshot = readme.ReadmeOverviewCache(str(tmp_path / "lib"), project_root=str(tmp_path))
    assert snapshot.manifest_for([str(file)]) == {"lib/nested/calc.rb": None}
    (tmp_path / "README.md").write_text("new requirements")
    async def forbidden(*args):
        pytest.fail("snapshot recorded no README, so no overview request is allowed")
    assert asyncio.run(snapshot.overview_for(forbidden, str(file))) is None
    fresh = readme.ReadmeOverviewCache(str(tmp_path / "lib"), project_root=str(tmp_path))
    assert fresh.manifest_for([str(file)])["lib/nested/calc.rb"]["path"] == "README.md"


needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def make_project(tmp_path):
    if not (tmp_path / "lib/calc.rb").exists():
        source_file(tmp_path, "lib/calc.rb")
    return project.RubyProject(str(tmp_path), "lib").discover()


@needs_ruby
def test_root_readme_reaches_requirement_prompt_and_saved_bundle(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "readme:test")
    (tmp_path / "README.md").write_text("ROOT_REQUIREMENTS")
    obj = make_project(tmp_path)
    prompts = []
    async def ask(system, user):
        prompts.append((obj._recorder().fase_atual, user))
        return "root-specific overview" if "ROOT_REQUIREMENTS" in user else "valid summary"
    asyncio.run(obj.analyze_summaries(ask=ask))
    assert any("ROOT_REQUIREMENTS" in user for _, user in prompts)
    assert any("Project Overview" in user and "root-specific overview" in user for _, user in prompts)
    bundle = json.loads(Path(obj._analysis_path("readme:test", True)).read_text())
    assert bundle["readme_policy"] == readme.README_POLICY
    assert bundle["readmes"] == {"lib/calc.rb": {"path": "README.md", "sha256": hashlib.sha256(b"ROOT_REQUIREMENTS").hexdigest()}}


@needs_ruby
@pytest.mark.parametrize("change", ["edit_root", "add_nearer", "remove_nearer"])
def test_used_document_content_or_selection_invalidates_analysis_cache(tmp_path, monkeypatch, change):
    monkeypatch.setenv("MODEL", "readme:test")
    (tmp_path / "README.md").write_text("initial requirements")
    obj = make_project(tmp_path)
    local = tmp_path / "lib/README.md"
    if change == "remove_nearer":
        local.write_text("initial requirements")
    calls = []
    async def ask(system, user):
        calls.append(user)
        return "valid summary"
    asyncio.run(obj.analyze_summaries(ask=ask))
    first = len(calls)
    asyncio.run(make_project(tmp_path).analyze_summaries(ask=ask))
    assert len(calls) == first
    if change == "edit_root":
        (tmp_path / "README.md").write_text("new requirements")
    elif change == "add_nearer":
        local.write_text("initial requirements")  # Same bytes, different selected document.
    else:
        local.unlink()
    asyncio.run(make_project(tmp_path).analyze_summaries(ask=ask))
    assert len(calls) > first


@needs_ruby
def test_editing_shadowed_root_readme_does_not_repeat_analysis(tmp_path):
    (tmp_path / "README.md").write_text("general requirements")
    obj = make_project(tmp_path)
    (tmp_path / "lib/README.md").write_text("specific library requirements")
    calls = []
    async def ask(system, user):
        calls.append(user)
        return "valid summary"
    asyncio.run(obj.analyze_summaries(ask=ask))
    first = len(calls)
    (tmp_path / "README.md").write_text("different general requirements")
    asyncio.run(make_project(tmp_path).analyze_summaries(ask=ask))
    assert len(calls) == first


@needs_ruby
def test_edit_during_analysis_cannot_change_context_under_a_saved_old_hash(tmp_path, monkeypatch):
    monkeypatch.setenv("MODEL", "readme:test")
    path = tmp_path / "README.md"
    path.write_text("ORIGINAL_REQUIREMENTS")
    obj = make_project(tmp_path)
    calls = []
    async def ask(system, user):
        if not calls:
            path.write_text("REVISED_REQUIREMENTS")
        calls.append(user)
        return "valid summary"
    asyncio.run(obj.analyze_summaries(ask=ask))
    assert any("ORIGINAL_REQUIREMENTS" in user for user in calls)
    assert not any("REVISED_REQUIREMENTS" in user for user in calls)
    bundle = json.loads(Path(obj._analysis_path("readme:test", True)).read_text())
    assert bundle["readmes"]["lib/calc.rb"]["sha256"] == hashlib.sha256(b"ORIGINAL_REQUIREMENTS").hexdigest()
    first = len(calls)
    asyncio.run(make_project(tmp_path).analyze_summaries(ask=ask))
    assert len(calls) > first and any("REVISED_REQUIREMENTS" in user for user in calls[first:])

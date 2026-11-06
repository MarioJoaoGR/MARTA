"""Offline environment/workspace boundaries with real Prism/RSpec/Coverage."""
import asyncio
import json
import os
from pathlib import Path
from unittest.mock import Mock

import pytest

from marta.ruby_backend import dependencies, execution, project, runner
from marta.ruby_backend.ablation import AblationOptions
from marta.ruby_backend.backend import RubyBackend
from marta.ruby_backend.tests.test_generate import (
    PLAN_RESPONSE, GOOD_SPEC, FAILING_SPEC, _make_project, _scripted_ask,
)
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok

needs_ruby = pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")


def make(tmp_path, **kwargs):
    _make_project(tmp_path)
    return project.RubyProject(str(tmp_path), "src", **kwargs).discover()


def run(obj, responses, *, rounds=1, attempts=1):
    ask, calls = _scripted_ask(responses)
    outcomes = asyncio.run(obj.generate_rounds(rounds, ask, attempts))
    return outcomes, calls


def test_environment_is_copied_validated_and_not_printed(tmp_path):
    supplied = {"PATH": "/private/ruby", "SECRET_API_TOKEN": "do-not-record"}
    obj = project.RubyProject(str(tmp_path), "src", subprocess_env=supplied)
    supplied["PATH"] = "/changed"
    assert obj._execution_environment()["PATH"] == "/private/ruby"
    with pytest.raises(TypeError):
        obj._execution_environment()["PATH"] = "/changed"
    assert "do-not-record" not in repr(obj)
    with pytest.raises(TypeError, match="must be strings"):
        project.RubyProject(str(tmp_path), "src", subprocess_env={"PATH": 123})


@needs_ruby
def test_two_projects_keep_their_environment_across_all_ruby_execution(tmp_path, monkeypatch):
    original_backend = RubyBackend()
    before = dict(os.environ)
    projects = []
    for name in ("alpha", "beta"):
        root = tmp_path / name
        root.mkdir()
        env = dict(os.environ, MARTA_ENV_PROBE=name)
        obj = make(root, subprocess_env=env, backend=original_backend)
        spec = root / "env_spec.rb"
        spec.write_text('require "calculator"\nRSpec.describe Calculator do\n'
                        f'  it("environment") {{ expect(ENV.fetch("MARTA_ENV_PROBE")).to eq("{name}"); '
                        'expect(Calculator.new.add(2, 3)).to eq(5) }\nend\n')
        projects.append((obj, spec))
    assert dict(os.environ) == before
    assert projects[0][0].backend is not projects[1][0].backend
    assert not hasattr(original_backend, "process_env")
    monkeypatch.setenv("MARTA_RUBY_BIN", "/invalid/global/ruby")
    monkeypatch.setenv("MARTA_RSPEC_BIN", "/invalid/global/rspec")
    monkeypatch.setenv("MARTA_ENV_PROBE", "unrelated")
    for obj, spec in reversed(projects):
        assert obj.backend.parse_file(str(Path(obj.abs_source) / "calculator.rb")).methods
        assert obj.backend.parse_source("class A; def x; end; end").methods
        assert obj.backend.syntax_check("def x; end") is None
        assert obj.backend.run_tests(str(spec), ["src"], obj.root_dir).all_passed
        result = obj.backend.run_coverage("src", [str(spec)], obj.root_dir)
        assert result.suite_result.all_passed
        assert result.files["calculator.rb"]


@needs_ruby
def test_default_environment_is_bound_at_first_discovery_and_recipe_uses_it(tmp_path, monkeypatch):
    monkeypatch.setenv("RUBYLIB", "initial-lib")
    monkeypatch.setenv("SECRET_API_TOKEN", "never-in-a-recipe")
    obj = make(tmp_path)
    bound = obj.backend.process_env["MARTA_RUBY_BIN"]
    monkeypatch.setenv("MARTA_RUBY_BIN", "/wrong/ruby")
    monkeypatch.setenv("RUBYLIB", "later-lib")
    assert obj.backend.syntax_check("def x; end") is None
    recipe = obj._generation_recipe(list(enumerate(obj.targets)), None, 1, False)
    assert recipe["environment"]["MARTA_RUBY_BIN"] == bound
    assert recipe["environment"]["RUBYLIB"] == "initial-lib"
    assert "never-in-a-recipe" not in json.dumps(recipe)
    obj._loading_dependency_index = {"stale": True}
    obj.discover()
    assert obj._loading_dependency_index is None
    assert obj.backend.process_env["RUBYLIB"] == "initial-lib"


def test_bundle_selection_uses_explicit_env_and_project_relative_gemfile(tmp_path, monkeypatch):
    (tmp_path / "nested").mkdir()
    (tmp_path / "nested/Gemfile").write_text("")
    env = {"BUNDLE_GEMFILE": "nested/Gemfile", "MARTA_RUBY_BIN": "/chosen/ruby"}
    query = Mock(return_value=[])
    monkeypatch.setattr(dependencies, "_query", query)
    monkeypatch.setenv("BUNDLE_GEMFILE", "/different/Gemfile")
    assert dependencies.bundle_index(tmp_path, env=env)["entries"] == []
    assert query.call_args.kwargs["env"] == env


@needs_ruby
def test_dependency_parser_uses_bound_ruby_without_mutating_rubyopt(tmp_path, monkeypatch):
    source = tmp_path / "a.rb"
    source.write_text("class A; end")
    env = dict(os.environ, RUBYOPT="-rdoes_not_exist")
    monkeypatch.setenv("MARTA_RUBY_BIN", "/wrong/ruby")
    facts = dependencies._query("--files", tmp_path, {"files": [str(source)]}, env=env)
    assert "A" in facts[str(source)]["definitions"]
    assert env["RUBYOPT"] == "-rdoes_not_exist"


@needs_ruby
def test_workspace_is_lazy_and_custom_backends_are_rejected_before_requests(tmp_path, monkeypatch):
    obj = make(tmp_path)
    copy = Mock(side_effect=AssertionError("unexpected project copy"))
    monkeypatch.setattr(execution.shutil, "copytree", copy)
    assert run(obj, [PLAN_RESPONSE, GOOD_SPEC])[0][0].success
    assert not copy.called
    class Custom(RubyBackend):
        pass
    obj.backend = Custom()
    obj.isolate_execution = True
    ask = Mock(side_effect=AssertionError("unexpected LLM request"))
    with pytest.raises(ValueError, match="native RubyBackend"):
        asyncio.run(obj.generate_all(ask=ask))
    assert not ask.called


@needs_ruby
def test_one_workspace_across_rounds_including_suite_validation(tmp_path, monkeypatch):
    output = tmp_path / "outputs"
    obj = make(tmp_path, isolate_execution=True, output_root=str(output),
               ablation_options=AblationOptions(no_coverage_feedback=True))
    before = (tmp_path / "src/calculator.rb").read_bytes()
    real_copy = execution.shutil.copytree
    copies = []
    def copy(*args, **kwargs):
        if len(args) >= 2 and Path(args[0]) == tmp_path:
            copies.append(Path(args[1]))
        return real_copy(*args, **kwargs)
    monkeypatch.setattr(execution.shutil, "copytree", copy)
    tests, coverage = [], []
    real_tests, real_coverage = RubyBackend.run_tests, RubyBackend.run_coverage
    def test_backend(self, *args, **kwargs):
        tests.append(kwargs.get("cwd") or args[2])
        return real_tests(self, *args, **kwargs)
    def cover_backend(self, *args, **kwargs):
        coverage.append(kwargs.get("cwd") or args[2])
        return real_coverage(self, *args, **kwargs)
    monkeypatch.setattr(RubyBackend, "run_tests", test_backend)
    monkeypatch.setattr(RubyBackend, "run_coverage", cover_backend)
    code = GOOD_SPEC.replace('require "calculator"', 'require "calculator"\nFile.write("workspace_scratch", "isolated")')
    outcomes, calls = run(obj, [PLAN_RESPONSE, code] * 3, rounds=3)
    assert [o.success for o in outcomes] == [True, True, True]
    assert calls["n"] == 6  # No added LLM requests or analysis.
    assert len(copies) == 1 and not copies[0].exists()
    assert set(tests + coverage) == {str(copies[0])}
    assert len(coverage) == 3
    assert not (tmp_path / "workspace_scratch").exists()
    assert (tmp_path / "src/calculator.rb").read_bytes() == before
    assert len(list((output / "marta_specs").glob("*.rb"))) == 3
    # An empty target population has no files to execute or copy.
    other = tmp_path / "empty"
    other.mkdir()
    empty = make(other, isolate_execution=True)
    empty.targets = []
    assert asyncio.run(empty.generate_all(ask=Mock())) == []
    assert len(copies) == 1


@needs_ruby
def test_single_round_api_uses_isolation_and_preserves_prompts(tmp_path):
    obj = make(tmp_path, isolate_execution=True)
    ask, calls = _scripted_ask([PLAN_RESPONSE, GOOD_SPEC])
    outcomes = asyncio.run(obj.generate_all(ask=ask, max_attempts=1))
    assert outcomes[0].success and calls["n"] == 2
    assert Path(obj.root_dir, outcomes[0].spec_path).read_text() == outcomes[0].spec_code + "\n"


@needs_ruby
def test_isolated_suite_gate_still_rolls_back_interacting_new_spec(tmp_path):
    obj = make(tmp_path, isolate_execution=True,
               ablation_options=AblationOptions(no_coverage_feedback=True))
    first = GOOD_SPEC.replace('RSpec.describe', '$mode = :first\nRSpec.describe').replace(
        'expect(described_class', 'expect($mode).to eq(:first)\n    expect(described_class')
    second = first.replace(':first', ':second')
    outcomes, _ = run(obj, [PLAN_RESPONSE, first, PLAN_RESPONSE, second], rounds=2)
    assert [o.success for o in outcomes] == [True, False]
    assert len(obj._all_spec_paths()) == 1
    assert list((tmp_path / "rejected_specs").glob("accumulated_*/*.rb"))


@needs_ruby
def test_interrupted_candidate_is_archived_and_private_copy_is_cleaned(tmp_path, monkeypatch):
    obj = make(tmp_path, isolate_execution=True)
    roots = []
    original = execution.GenerationWorkspace.ensure
    def ensure(self):
        original(self)
        roots.append(self.root)
    monkeypatch.setattr(execution.GenerationWorkspace, "ensure", ensure)
    responses = iter([PLAN_RESPONSE, FAILING_SPEC])
    async def ask(*args):
        try:
            return next(responses)
        except StopIteration:
            raise asyncio.CancelledError()
    with pytest.raises(asyncio.CancelledError):
        asyncio.run(obj.generate_rounds(1, ask, 2))
    assert not obj._all_spec_paths()
    assert list((tmp_path / "rejected_specs").glob("execution_*/*.rb"))
    assert roots and all(not p.exists() for p in roots)


@needs_ruby
def test_source_writes_are_detected_before_round_certification(tmp_path):
    obj = make(tmp_path, isolate_execution=True)
    original = (tmp_path / "src/calculator.rb").read_text()
    code = GOOD_SPEC.replace('RSpec.describe', 'File.write("src/calculator.rb", "class Changed; end")\nRSpec.describe')
    with pytest.raises(RuntimeError, match="Workspace input changed"):
        run(obj, [PLAN_RESPONSE, code])
    assert (tmp_path / "src/calculator.rb").read_text() == original
    assert not list((tmp_path / ".marta_generation").glob("*.json"))


@needs_ruby
@pytest.mark.parametrize("link", ["source", "output"])
def test_workspace_rejects_links_before_generation(tmp_path, link):
    obj = make(tmp_path, isolate_execution=True)
    outside = tmp_path.parent / (tmp_path.name + "_external")
    outside.mkdir()
    if link == "source":
        (tmp_path / "source_link").symlink_to(outside, target_is_directory=True)
    else:
        (tmp_path / "marta_specs").symlink_to(outside, target_is_directory=True)
    ask = Mock(side_effect=AssertionError("unexpected model call"))
    with pytest.raises(ValueError, match="symlink|publication"):
        asyncio.run(obj.generate_all(ask=ask))
    assert not ask.called
    assert not list(outside.iterdir())


@needs_ruby
def test_installed_environment_paths_stay_external_and_helpers_are_copied_once(tmp_path):
    helper = tmp_path.parent / (tmp_path.name + "_helper.rb")
    helper.write_text("# explicit helper")
    obj = make(tmp_path, isolate_execution=True)
    with execution.GenerationWorkspace(obj) as workspace:
        workspace.ensure()
        assert workspace.backend.process_env["GEM_HOME"] == obj.backend.process_env["GEM_HOME"]
        assert workspace.backend.process_env["TMPDIR"] != os.environ.get("TMPDIR")
        a = workspace.remap(str(helper), helper=True)
        b = workspace.remap(str(helper), helper=True)
        assert a == b and Path(a).read_text() == helper.read_text()
        with pytest.raises(ValueError, match="External load paths"):
            workspace.remap(str(helper.parent))
        (tmp_path / "src/calculator.rb").write_text("# changed outside")
        with pytest.raises(RuntimeError, match="Project input changed"):
            workspace.verify_inputs()


@needs_ruby
def test_two_isolated_projects_can_interleave_without_exchanging_env_or_outputs(tmp_path, monkeypatch):
    objects = []
    for name in ("alpha", "beta"):
        root = tmp_path / name
        root.mkdir()
        obj = make(root, isolate_execution=True,
                   subprocess_env=dict(os.environ, MARTA_ENV_PROBE=name))
        code = GOOD_SPEC.replace('expect(described_class',
            f'expect(ENV.fetch("MARTA_ENV_PROBE")).to eq("{name}")\n    expect(described_class')
        count = [0]
        async def ask(system, user, code=code, count=count):
            await asyncio.sleep(0)
            monkeypatch.setenv("MARTA_ENV_PROBE", "unrelated-parent")
            count[0] += 1
            return PLAN_RESPONSE if count[0] == 1 else code
        objects.append((obj, ask))
    async def together():
        return await asyncio.gather(*(obj.generate_all(ask=ask, max_attempts=1) for obj, ask in objects))
    result = asyncio.run(together())
    assert all(rows[0].success for rows in result)
    assert all(len(obj._all_spec_paths()) == 1 for obj, _ in objects)
    assert result[0][0].spec_code != result[1][0].spec_code


@needs_ruby
def test_changed_candidate_is_not_published_even_if_rspec_passes(tmp_path):
    obj = make(tmp_path, isolate_execution=True)
    code = GOOD_SPEC.replace('RSpec.describe', 'File.write(__FILE__, "# changed by test")\nRSpec.describe')
    with pytest.raises(RuntimeError, match="candidate changed"):
        run(obj, [PLAN_RESPONSE, code])
    assert not obj._all_spec_paths()
    assert list((tmp_path / "rejected_specs").glob("execution_*/*.rb"))


@needs_ruby
def test_native_post_evaluation_keeps_bound_env_after_parent_changes(tmp_path, monkeypatch):
    from marta.ruby_backend.evaluation import evaluate_project
    obj = make(tmp_path, subprocess_env=dict(os.environ, MARTA_ENV_PROBE="initial"))
    code = GOOD_SPEC.replace('expect(described_class',
        'expect(ENV.fetch("MARTA_ENV_PROBE")).to eq("initial")\n    expect(described_class')
    assert run(obj, [PLAN_RESPONSE, code])[0][0].success
    monkeypatch.setenv("MARTA_ENV_PROBE", "different")
    monkeypatch.setenv("MARTA_RUBY_BIN", "/wrong/ruby")
    report = json.loads(evaluate_project(obj).read_text())
    assert report["suite"]["valid"]


def test_environment_relocation_preserves_installations_and_remaps_local_paths(tmp_path):
    source, destination = tmp_path / "original", tmp_path / "copy"
    env = {"BUNDLE_GEMFILE": str(source / "Gemfile"), "GEM_HOME": "/installed/gems",
           "GEM_PATH": str(source / "vendor/gems") + os.pathsep + "/installed/gems",
           "PATH": str(source / "bin") + os.pathsep + "/usr/bin"}
    moved = execution.relocate_environment(env, source, destination)
    assert moved["BUNDLE_GEMFILE"] == str(destination / "Gemfile")
    assert moved["GEM_HOME"] == env["GEM_HOME"]
    assert moved["GEM_PATH"] == str(destination / "vendor/gems") + os.pathsep + "/installed/gems"
    assert moved["PATH"] == str(destination / "bin") + os.pathsep + "/usr/bin"
    assert env["BUNDLE_GEMFILE"] == str(source / "Gemfile")
    with pytest.raises(ValueError, match="RUBYOPT"):
        execution.relocate_environment(dict(env, RUBYOPT="-r" + str(source / "loader.rb")), source, destination)


@needs_ruby
def test_suite_cannot_certify_different_bytes_than_it_executed(tmp_path):
    obj = make(tmp_path, isolate_execution=True,
               ablation_options=AblationOptions(no_coverage_feedback=True))
    code = GOOD_SPEC.replace('    expect(described_class',
        '    File.write(__FILE__, "# modified only in accumulated suite") if RSpec.world.example_count > 1\n'
        '    expect(described_class')
    with pytest.raises(RuntimeError, match="Suite file changed"):
        run(obj, [PLAN_RESPONSE, code] * 2, rounds=2)
    state = json.loads((tmp_path / ".marta_generation/rounds.json").read_text())
    assert len(state["rounds"]) == 1  # Only the first unmodified suite was certified.

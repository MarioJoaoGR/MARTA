"""Definition-based output identity and exact RAG lookup, without live inference."""
import asyncio
from dataclasses import replace
import hashlib
import json
from pathlib import Path

import pytest

from marta.ruby_backend import project
from marta.ruby_backend.ruby_ast import ClassInfo, MethodInfo
from marta.ruby_backend.tests.test_suite_validation import toolchain_ok


def target(file="same.rb", name="run", singleton=False, start=3, end=5, owner="C", task_id=None):
    cls = ClassInfo(owner, owner, "class", None, 1, end + 1) if owner else None
    return project.MethodTarget(
        MethodInfo(name, owner, singleton, start, end), cls,
        "/checkout/lib/" + file, file.removesuffix(".rb"), rel_path=file, task_id=task_id)


@pytest.mark.parametrize("first,second", [
    ({"file": "a/same.rb"}, {"file": "b/same.rb"}),
    ({"singleton": False}, {"singleton": True}),
    ({"name": "ready?"}, {"name": "ready_q"}),
    ({"name": "+"}, {"name": "-"}),
    ({"name": "ação"}, {"name": "a__o"}),
    ({"start": 3, "end": 5}, {"start": 10, "end": 12}),
    ({"name": "run"}, {"name": "RUN"}),
])
def test_distinct_definitions_never_share_a_normal_output_path(first, second):
    a, b = target(**first), target(**second)
    assert a.analysis_id != b.analysis_id
    assert a.spec_path.casefold() != b.spec_path.casefold()
    assert a.spec_path_for_round(0).casefold() != b.spec_path_for_round(0).casefold()
    assert a.spec_path != b.spec_path_for_round(0)


def test_normal_filename_binds_the_full_definition_and_is_bounded_ascii():
    t = target(file="funções[base].rb", name="ação" + "x" * 200, owner="C" + "X" * 200)
    name = Path(t.spec_path).name
    digest = hashlib.sha256(t.analysis_id.encode("utf-8")).hexdigest()
    assert name.endswith("__def_" + digest + "_spec.rb")
    assert name.isascii() and len(name.encode()) < 200
    assert Path(t.spec_path_for_round(123)).name.endswith("_r123_spec.rb")


def test_identity_is_stable_across_workspaces_output_roots_and_selections():
    t = target(file="a/same.rb")
    moved = replace(t, file_path="/other/workspace/lib/a/same.rb", spec_dir="/output/marta_specs")
    assert t.analysis_id == moved.analysis_id
    assert Path(t.spec_path).name == Path(moved.spec_path).name
    assert Path(t.spec_path_for_round(2)).name == Path(moved.spec_path_for_round(2)).name


@pytest.mark.parametrize("task_id", [0, 172, "external-task", "tarefa-ação"])
def test_existing_task_filenames_are_preserved_exactly(task_id):
    t = target(task_id=task_id)
    digest = hashlib.sha256(json.dumps([task_id, t.analysis_id]).encode()).hexdigest()[:20]
    assert t.spec_path == f"marta_specs/same__C__run__task_{digest}_spec.rb"
    assert t.spec_path_for_round(0) == f"marta_specs/same__C__run__task_{digest}_r0_spec.rb"
    assert t.spec_path != replace(t, task_id=None).spec_path


def test_rag_ignores_legacy_prefix_neighbours_and_non_round_suffixes(tmp_path):
    root = tmp_path / "repo[one]"
    directory = root / "marta_specs"
    directory.mkdir(parents=True)
    t = target()
    obj = project.RubyProject(str(root), "lib", targets=[t])
    for name in ("same__C__run_spec.rb", t._spec_stem + "extra_spec.rb",
                 t._spec_stem + "_rno_spec.rb", t._spec_stem + "_r-1_spec.rb"):
        (directory / name).write_text("wrong definition or suffix")
    assert obj._example_passing_spec(t) is None
    (directory / Path(t.spec_path_for_round(2)).name).write_text("right definition")
    assert obj._example_passing_spec(t) == "right definition"


def test_rag_recovers_task_output_for_the_same_production_definition_only(tmp_path):
    definition = target(file="a/same.rb")
    selected = replace(definition, task_id="task-a")
    other = target(file="b/same.rb", task_id="task-b")
    obj = project.RubyProject(str(tmp_path), "lib", targets=[selected, other])
    directory = tmp_path / "marta_specs"
    directory.mkdir()
    (tmp_path / other.spec_path_for_round(0)).write_text("other file")
    assert obj._example_passing_spec(definition) is None
    (tmp_path / selected.spec_path_for_round(0)).write_text("matching task file")
    assert obj._example_passing_spec(definition) == "matching task file"


def test_rag_skips_empty_matching_files_and_reads_single_round_helper_output(tmp_path):
    t = target()
    obj = project.RubyProject(str(tmp_path), "lib", targets=[t])
    (tmp_path / "marta_specs").mkdir()
    (tmp_path / t.spec_path_for_round(0)).write_text(" \n")
    (tmp_path / t.spec_path).write_text("complete helper output")
    assert obj._example_passing_spec(t) == "complete helper output"


@pytest.mark.skipif(not toolchain_ok(), reason="no Ruby/RSpec toolchain")
@pytest.mark.parametrize("entry_point", ["generate_all", "generate_rounds"])
@pytest.mark.parametrize("case", ["directories", "singleton", "sanitization"])
def test_previously_colliding_methods_generate_two_independent_valid_files(tmp_path, case, entry_point):
    src = tmp_path / "src"
    src.mkdir()
    if case == "directories":
        for directory in ("a", "b"):
            (src / directory).mkdir()
            (src / directory / "same.rb").write_text("class C\n  def run; 1; end\nend\n")
    elif case == "singleton":
        (src / "same.rb").write_text("class C\n  def run; 1; end\n  def self.run; 1; end\nend\n")
    else:
        (src / "same.rb").write_text("class C\n  def ready?; 1; end\n  def ready_q; 1; end\nend\n")
    obj = project.RubyProject(str(tmp_path), "src").discover()
    assert len(obj.targets) == 2
    responses = []
    expected = []
    for t in obj.targets:
        receiver = "C" if t.method.singleton else "C.new"
        code = (f'require "{t.require_target}"\nRSpec.describe C do\n'
                f'  it("{t.analysis_id.replace(chr(34), chr(39))}") '
                f'{{ expect({receiver}.{t.method.name}).to eq(1) }}\nend\n')
        expected.append(code)
        responses += ['[{"name":"exercise", "desc":"test method", "setup":"None"}]', code]
    calls = []
    async def ask(system, user):
        calls.append(user)
        return responses.pop(0)
    kwargs = {"rounds": 1} if entry_point == "generate_rounds" else {}
    outcomes = asyncio.run(getattr(obj, entry_point)(ask=ask, max_attempts=1, **kwargs))
    assert len(outcomes) == 2 and all(o.success for o in outcomes)
    assert len(calls) == 4  # One Planner and one Dev call per definition.
    paths = [tmp_path / o.spec_path for o in outcomes]
    assert len(set(paths)) == 2
    assert [path.read_text() for path in paths] == expected
    assert len(obj._all_spec_paths()) == 2
    assert obj.measure_coverage()  # Both files execute together successfully.

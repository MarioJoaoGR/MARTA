import json
import pytest
from deucalion.xrepotest_ablation_subset import select, save


def tasks():
    return [{"task_id": i, "file_path": name + "/lib/example.rb"}
            for name, ids in (("a", range(0, 30)), ("b", range(30, 40)), ("c", range(40, 42)))
            for i in ids]


def test_subset_is_reproducible_and_outcome_independent():
    original = tasks()
    chosen, counts = select(original, 5, "fixed")
    assert len(chosen) == len(set(chosen)) == 12
    assert counts == {"a": 5, "b": 5, "c": 2}
    assert chosen == sorted(chosen)
    decorated = [{**t, "result": "changed", "response": []} for t in reversed(original)]
    assert select(decorated, 5, "fixed") == (chosen, counts)
    assert select(original, 5, "other")[0] != chosen


def test_entire_dataset_and_singleton_projects():
    chosen, counts = select(tasks(), 30, "fixed")
    assert chosen == list(range(42))
    assert counts == {"a": 30, "b": 10, "c": 2}
    assert select([{ "task_id": 3, "file_path": "a/a.rb"},
                   { "task_id": 8, "file_path": "b/b.rb"}], 10, "fixed")[0] == [3, 8]


@pytest.mark.parametrize("count", [0, -1, True])
def test_invalid_size_refused(count):
    with pytest.raises(ValueError):
        select(tasks(), count, "fixed")


def test_duplicate_ids_refused():
    with pytest.raises(ValueError, match="Duplicate"):
        select(tasks() + [tasks()[0]], 5, "fixed")


def test_saved_selection_is_immutable_and_idempotent(tmp_path):
    path = tmp_path / "ids.json"
    save(path, [1, 3])
    before = path.read_bytes()
    save(path, [1, 3])
    assert path.read_bytes() == before
    with pytest.raises(ValueError, match="Refusing"):
        save(path, [2, 3])
    assert json.loads(path.read_text()) == [1, 3]


def test_ten_projects_with_small_pundit_yield_97():
    original = [{"task_id": project * 100 + i, "file_path": str(project) + "/lib/a.rb"}
                for project in range(10) for i in range(7 if project == 9 else 20)]
    ids, counts = select(original, 10, "fixed")
    assert len(ids) == 97 and counts["9"] == 7
    assert all(count == 10 for project, count in counts.items() if project != "9")
    assert set(range(900, 907)) <= set(ids)

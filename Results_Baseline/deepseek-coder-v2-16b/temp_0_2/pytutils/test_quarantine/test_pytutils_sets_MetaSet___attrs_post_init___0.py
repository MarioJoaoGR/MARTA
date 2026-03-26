
import pytest
import random
import attr
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet()

def test_initialization(meta_set):
    assert isinstance(meta_set._store, set)
    assert isinstance(meta_set._meta, dict)
    assert meta_set._initial is None

def test_update_with_list(meta_set):
    meta_set.update([1, 2, 3])
    assert list(meta_set._store) == [1, 2, 3]

def test_add_element(meta_set):
    meta_set.add("example_value")
    assert "example_value" in meta_set._store

def test_discard_element(meta_set):
    meta_set.update([1, 2, 3])
    meta_set.discard(1)
    assert list(meta_set._store) == [2, 3]

def test_contains_method(meta_set):
    meta_set.update([1, 2, 3])
    assert 2 in meta_set

def test_iter_method(meta_set):
    meta_set.update([1, 2, 3])
    assert list(meta_set) == [1, 2, 3]

def test_len_method(meta_set):
    meta_set.update([1, 2, 3])
    assert len(meta_set) == 3

def test_metadata_dictionary(meta_set):
    meta_set.update([1, 2, 3])
    metadata = {item: random.randint(0, 1) for item in [1, 2, 3]}
    assert meta_set._asdict() == metadata

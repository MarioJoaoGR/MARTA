
import pytest
from pytutils.sets import MetaSet

@pytest.fixture
def meta_set():
    return MetaSet(initial={1, 2, 3})

def test_update_during_init(meta_set):
    assert list(meta_set._store) == [1, 2, 3]
    with pytest.raises(AttributeError):
        assert meta_set._initial

@pytest.fixture
def empty_meta_set():
    return MetaSet()

def test_update_with_empty_init(empty_meta_set):
    empty_meta_set.update({})
    assert list(empty_meta_set._store) == []

def test_update_with_none_init(empty_meta_set):
    with pytest.raises(TypeError, match=".*not iterable"):
        empty_meta_set.update(None)

def test_update_with_iterable(meta_set):
    meta_set.update([4, 5, 6])
    assert list(meta_set._store) == [1, 2, 3, 4, 5, 6]

def test_update_with_duplicate_elements(meta_set):
    meta_set.update([1, 2, 2, 3, 3])
    assert list(meta_set._store) == [1, 2, 3]

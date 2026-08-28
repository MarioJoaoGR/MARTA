
import pytest
from flutes.iterator import LazyList

def test_access_elements():
    lazy_list = LazyList(range(5))
    assert lazy_list[0] == 0
    assert lazy_list[3] == 3

def test_iterate_over_lazylist():
    lazy_list = LazyList(range(5))
    expected = [0, 1, 2, 3, 4]
    for i, value in enumerate(lazy_list):
        assert value == expected[i]

def test_convert_to_list():
    lazy_list = LazyList(range(5))
    full_list = list(lazy_list)
    assert full_list == [0, 1, 2, 3, 4]

def test_exhausted_length():
    lazy_list = LazyList(range(5))
    # Exhaust the iterator
    _ = list(lazy_list)
    assert len(lazy_list) == 5

def test_non_exhausted_length():
    lazy_list = LazyList(range(5))
    with pytest.raises(TypeError):
        _ = len(lazy_list)

def test_empty_lazylist():
    lazy_list = LazyList([])
    full_list = list(lazy_list)
    assert full_list == []

def test_empty_lazylist_length():
    lazy_list = LazyList([])
    # Exhaust the iterator
    _ = list(lazy_list)
    assert len(lazy_list) == 0

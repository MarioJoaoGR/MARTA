
import pytest
from flutes.iterator import LazyList

def test_lazy_list_initialization():
    lazy_list = LazyList([1, 2, 3, 4])
    assert isinstance(lazy_list, LazyList)
    actual_items = []
    for item in lazy_list:
        actual_items.append(item)
    assert actual_items == [1, 2, 3, 4]

def test_lazy_list_indexing():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1

def test_lazy_list_iteration():
    lazy_list = LazyList([1, 2, 3, 4])
    actual_items = []
    for item in lazy_list:
        actual_items.append(item)
    assert actual_items == [1, 2, 3, 4]

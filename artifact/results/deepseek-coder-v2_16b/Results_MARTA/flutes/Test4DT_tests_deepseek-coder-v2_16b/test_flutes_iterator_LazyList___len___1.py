
import pytest
from flutes.iterator import LazyList

def test_lazy_list_iteration():
    lazy_list = LazyList([1, 2, 3, 4])
    iterated_elements = []
    for item in lazy_list:
        iterated_elements.append(item)
    assert iterated_elements == [1, 2, 3, 4]

def test_lazy_list_index_access():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3


import pytest
from flutes.iterator import LazyList

# Test initialization with an iterable
def test_lazy_list_initialization():
    lazy_list = LazyList([1, 2, 3, 4])
    assert isinstance(lazy_list, LazyList)
    assert list(lazy_list) == [1, 2, 3, 4]

# Test accessing elements by index
def test_lazy_list_index():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3

# Test converting the entire lazy list to a regular list
def test_lazy_list_to_list():
    lazy_list = LazyList([1, 2, 3, 4])
    regular_list = list(lazy_list)
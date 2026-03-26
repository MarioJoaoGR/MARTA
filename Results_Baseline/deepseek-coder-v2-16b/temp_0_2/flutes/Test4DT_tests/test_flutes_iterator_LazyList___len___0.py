
import pytest
from flutes.iterator import LazyList

# Test creating a LazyList from an iterable
def test_lazy_list_creation():
    lazy_list = LazyList([1, 2, 3, 4])
    assert isinstance(lazy_list, LazyList)

# Test iterating over a LazyList and ensuring StopIteration is raised when exhausted
def test_iterating_over_lazy_list():
    lazy_list = LazyList([1, 2, 3, 4])
    iterator = iter(lazy_list)
    assert next(iterator) == 1
    assert next(iterator) == 2
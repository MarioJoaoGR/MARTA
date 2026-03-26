
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
    assert next(iterator) == 3
    assert next(iterator) == 4
    with pytest.raises(StopIteration):
        next(iterator)

# Test __len__ method when the iterable is exhausted
def test_lazy_list_len_after_exhaustion():
    lazy_list = LazyList([1, 2, 3, 4])
    iterator = iter(lazy_list)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    with pytest.raises(TypeError):
        len(lazy_list)

# Test __len__ method when the iterable is not exhausted, should raise TypeError
def test_lazy_list_len_not_exhausted():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(TypeError):
        len(lazy_list)

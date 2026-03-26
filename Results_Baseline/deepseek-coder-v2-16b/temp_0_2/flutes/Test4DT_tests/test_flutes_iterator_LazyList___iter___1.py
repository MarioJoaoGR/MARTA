
# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

# Test initialization with an iterable
def test_lazy_list_initialization():
    lazy_list = LazyList([1, 2, 3, 4])
    assert list(lazy_list) == [1, 2, 3, 4]

# Test iteration over a lazy list
def test_lazy_list_iteration():
    lazy_list = LazyList([1, 2, 3, 4])
    iterator = iter(lazy_list)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    with pytest.raises(StopIteration):
        next(iterator)

# Test accessing elements by index
def test_lazy_list_index_access():
    lazy_list = LazyList([10, 20, 30])
    assert lazy_list[0] == 10
    assert lazy_list[1] == 20
    assert lazy_list[2] == 30

# Test slicing a lazy list
def test_lazy_list_slicing():
    lazy_list = LazyList([10, 20, 30, 40])
    assert list(lazy_list[0:2]) == [10, 20]

# Test iteration over an empty lazy list
def test_empty_lazy_list():
    lazy_list = LazyList([])
    iterator = iter(lazy_list)
    with pytest.raises(StopIteration):
        next(iterator)

# Test using a generator to create a lazy list
def test_lazy_list_from_generator():
    def generate_numbers():
        yield 5
        yield 6
        yield 7
    
    lazy_list = LazyList(generate_numbers())
    iterator = iter(lazy_list)
    assert next(iterator) == 5
    assert next(iterator) == 6
    assert next(iterator) == 7

# Test that __iter__ returns an iterator when the list is exhausted
def test_lazy_list_exhausted():
    lazy_list = LazyList([1, 2, 3, 4])
    iterator = iter(lazy_list)
    for _ in range(4):
        next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)
    assert list(lazy_list) == [1, 2, 3, 4]  # Ensure the list is not exhausted after iteration

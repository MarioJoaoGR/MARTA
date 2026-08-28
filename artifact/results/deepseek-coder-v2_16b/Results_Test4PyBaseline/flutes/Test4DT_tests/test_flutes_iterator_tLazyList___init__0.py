# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

# Test initialization with a list
def test_lazy_list_with_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert isinstance(lazy_list.iter, type(iter(my_list))), "The iterator should be the same as the one from the iterable"
    assert not lazy_list.exhausted, "The list should not be exhausted after initialization"
    assert len(lazy_list.list) == 0, "The internal list should be empty initially"

# Test initialization with a tuple
def test_lazy_list_with_tuple():
    my_tuple = (10, 20, 30, 40, 50)
    lazy_list = LazyList(my_tuple)
    assert isinstance(lazy_list.iter, type(iter(my_tuple))), "The iterator should be the same as the one from the iterable"
    assert not lazy_list.exhausted, "The tuple should not be exhausted after initialization"
    assert len(lazy_list.list) == 0, "The internal list should be empty initially"

# Test initialization with a set
def test_lazy_list_with_set():
    my_set = {100, 200, 300, 400, 500}
    lazy_list = LazyList(my_set)
    assert isinstance(lazy_list.iter, type(iter(my_set))), "The iterator should be the same as the one from the iterable"
    assert not lazy_list.exhausted, "The set should not be exhausted after initialization"
    assert len(lazy_list.list) == 0, "The internal list should be empty initially"

# Test initialization with a generator
def test_lazy_list_with_generator():
    def my_generator():
        yield 1000
        yield 2000
        yield 3000
        yield 4000
        yield 5000
    
    lazy_list = LazyList(my_generator())
    assert isinstance(lazy_list.iter, type(my_generator())), "The iterator should be the same as the one from the iterable"
    assert not lazy_list.exhausted, "The generator should not be exhausted after initialization"
    assert len(lazy_list.list) == 0, "The internal list should be empty initially"

# Test iteration over a LazyList
def test_lazy_list_iteration():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    iterated_elements = []
    for element in lazy_list:
        iterated_elements.append(element)
    assert iterated_elements == my_list, "The elements should be the same as in the original list"
    assert lazy_list.exhausted, "The iterator should be exhausted after iteration"
    assert len(lazy_list.list) == len(my_list), "The internal list should contain all elements after iteration"

# Test accessing beyond the end of the iterable
def test_lazy_list_access_beyond_end():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    with pytest.raises(StopIteration):
        while True:
            next(lazy_list.iter)

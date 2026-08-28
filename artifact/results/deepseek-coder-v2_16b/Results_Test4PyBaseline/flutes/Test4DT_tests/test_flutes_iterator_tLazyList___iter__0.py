# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

# Test initialization with a list
def test_lazy_list_initialization_with_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert isinstance(lazy_list, LazyList)
    assert list(lazy_list) == [1, 2, 3, 4, 5]

# Test initialization with a generator
def test_lazy_list_initialization_with_generator():
    def my_generator():
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5
    
    lazy_list = LazyList(my_generator())
    assert isinstance(lazy_list, LazyList)
    assert list(lazy_list) == [1, 2, 3, 4, 5]

# Test iteration over a lazy list
def test_iteration_over_lazy_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    iterated_elements = []
    for element in lazy_list:
        iterated_elements.append(element)
    assert iterated_elements == [1, 2, 3, 4, 5]

# Test accessing elements by index
def test_accessing_elements_by_index():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4
    assert lazy_list[4] == 5

# Test accessing an out-of-range index raises IndexError
def test_accessing_out_of_range_index():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    with pytest.raises(IndexError):
        lazy_list[5]

# Test converting a lazy list to a regular list
def test_converting_lazy_list_to_regular_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert list(lazy_list) == [1, 2, 3, 4, 5]

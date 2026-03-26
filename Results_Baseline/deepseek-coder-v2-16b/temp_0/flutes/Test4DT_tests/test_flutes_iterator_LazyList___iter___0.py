
# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList
import bisect  # Importing the necessary module for test_map_list_bisect_left

# Test initialization with an iterable
def test_lazy_list_initialization():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert isinstance(lazy_list, LazyList)

# Test iteration over the lazy list
def test_lazy_list_iteration():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    iterated_elements = []
    for element in lazy_list:
        iterated_elements.append(element)
    assert iterated_elements == [1, 2, 3, 4, 5]

# Test accessing elements by index
def test_lazy_list_index_access():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert lazy_list[0] == 1
    assert lazy_list[2] == 3

# Test converting the lazy list to a regular Python list
def test_lazy_list_to_list():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    regular_list = list(lazy_list)
    assert regular_list == [1, 2, 3, 4, 5]

# Test creating a MapList and transforming elements
def test_map_list():
    def square(x):
        return x * x

    transformed_list = LazyList([1, 2, 3, 4, 5])
    mapped_list = [square(element) for element in transformed_list]
    assert mapped_list == [1, 4, 9, 16, 25]

# Test using MapList with bisect_left to find the index of an element whose transformation meets a certain condition
def test_map_list_bisect_left():
    def square(x):
        return x * x

    transformed_list = LazyList([1, 2, 3, 4, 5])
    mapped_list = [square(element) for element in transformed_list]
    pos = bisect.bisect_left(mapped_list, 10)
    assert pos == 3

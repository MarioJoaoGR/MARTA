# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

# Test creating a LazyList from an iterable
def test_lazy_list_creation():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert isinstance(lazy_list, LazyList)
    assert list(lazy_list) == [1, 2, 3, 4, 5]

# Test accessing elements by index
def test_lazy_list_getitem():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert lazy_list[0] == 1
    assert lazy_list[1:3] == [2, 3]

# Test using __len__ method before the iterable is depleted
def test_lazy_list_len():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    with pytest.raises(TypeError):
        len(lazy_list)

# Test iterating over a lazy list and performing operations
def test_lazy_list_iteration():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    squared_elements = []
    for element in lazy_list:
        squared_elements.append(element ** 2)
    assert squared_elements == [1, 4, 9, 16, 25]

# Test accessing elements by slice
def test_lazy_list_slice():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    assert lazy_list[1:4] == [2, 3, 4]

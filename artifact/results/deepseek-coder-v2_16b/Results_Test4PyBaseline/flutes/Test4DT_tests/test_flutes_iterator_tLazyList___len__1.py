
# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

# Test initialization with an iterable
def test_lazy_list_initialization():
    lazy_list = LazyList([1, 2, 3, 4])
    assert isinstance(lazy_list, LazyList)
    assert list(lazy_list) == [1, 2, 3, 4]

# Test iteration over the lazy list
def test_lazy_list_iteration():
    lazy_list = LazyList([1, 2, 3, 4])
    iterated_elements = []
    for element in lazy_list:
        iterated_elements.append(element)
    assert iterated_elements == [1, 2, 3, 4]

# Test accessing elements using indexing
def test_lazy_list_indexing():
    lazy_list = LazyList([1, 2, 3, 4])
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[3] == 4

# Test accessing out-of-range index raises IndexError
def test_lazy_list_out_of_range_index():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(IndexError):
        lazy_list[4]

# Test converting the lazy list to a regular Python list
def test_lazy_list_to_list():
    lazy_list = LazyList([1, 2, 3, 4])
    assert list(lazy_list) == [1, 2, 3, 4]

# Test getting the length of the lazy list raises TypeError when not exhausted
def test_lazy_list_len_not_exhausted():
    lazy_list = LazyList([1, 2, 3, 4])
    with pytest.raises(TypeError):
        len(lazy_list)

# Test getting the length of the lazy list returns correct length when exhausted
def test_lazy_list_len_exhausted():
    lazy_list = LazyList([1, 2, 3, 4])
    # Force exhaustion by iterating over the entire list
    for _ in lazy_list:
        pass
    assert len(lazy_list) == 4

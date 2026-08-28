# Module: flutes.iterator
import pytest
from flutes.iterator import LazyList

# Test creating a LazyList from an iterable
def test_lazylist_creation():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    
    # Access elements of the lazy list one by one
    result = []
    for element in lazy_list:
        result.append(element)
    
    assert result == [1, 2, 3, 4, 5]

# Test accessing elements using indexing
def test_lazylist_getitem():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Access the first element
    assert lazy_list[0] == 1
    
    # Access the second element
    assert lazy_list[1] == 2
    
    # Access the third element
    assert lazy_list[2] == 3
    
    # Access the fourth element
    assert lazy_list[3] == 4

# Test accessing an out-of-range index (will trigger iteration until that point)
def test_lazylist_getitem_out_of_range():
    lazy_list = LazyList([1, 2, 3, 4])
    
    with pytest.raises(IndexError):
        lazy_list[4]

# Test converting the lazy list to a regular Python list
def test_lazylist_to_list():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Convert the lazy list to a regular Python list
    assert list(lazy_list) == [1, 2, 3, 4]


import pytest
from flutes.iterator import LazyList

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

# Test accessing elements using slice indexing
def test_lazylist_slice():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Access the first two elements
    assert lazy_list[0:2] == [1, 2]
    
    # Access the middle two elements
    assert lazy_list[1:3] == [2, 3]
    
    # Access the last two elements

import pytest
from flutes.iterator import LazyList

def test_valid_inputs():
    my_list = [1, 2, 3, 4, 5]
    lazy_list = LazyList(my_list)
    
    # Check if the list is empty initially
    assert len(lazy_list.list) == 0
    
    # Access elements of the lazy list one by one
    for i in range(len(my_list)):
        assert lazy_list[i] == my_list[i]
    
    # Check if the list is populated correctly after iteration
    assert len(lazy_list.list) == len(my_list)

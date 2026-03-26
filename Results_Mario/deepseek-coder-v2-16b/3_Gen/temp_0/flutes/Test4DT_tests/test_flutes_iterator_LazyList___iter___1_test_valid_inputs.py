
import pytest
from flutes.iterator import LazyList

def test_valid_inputs():
    my_list = [1, 2, 3, 4]
    lazy_list = LazyList(my_list)
    
    # Check the length of the list is equal to the number of elements accessed
    assert len(lazy_list.list) == 0
    
    # Iterate through the lazy list and check if it produces the expected values
    iterated_values = []
    for item in lazy_list:
        iterated_values.append(item)
        if item == 3:
            break
    
    assert iterated_values == [1, 2, 3]
    assert len(lazy_list.list) == 3

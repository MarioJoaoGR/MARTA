
import pytest
from flutes.iterator import LazyList

def test_valid_inputs():
    lazy_list = LazyList([1, 2, 3, 4])
    expected_output = [1, 2, 3, 4]
    actual_output = []
    
    for item in lazy_list:
        actual_output.append(item)
        if item == 4:
            break
    
    assert actual_output == expected_output

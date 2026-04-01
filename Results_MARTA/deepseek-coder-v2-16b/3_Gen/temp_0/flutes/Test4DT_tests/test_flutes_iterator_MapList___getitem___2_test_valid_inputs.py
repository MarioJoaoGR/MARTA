
import pytest
from flutes.iterator import MapList
from typing import List, Callable

# Define the square function as given in the setup
def square(x: int) -> int: return x * x

def test_valid_inputs():
    # Test with a list of integers and a lambda function to square each element
    ml = MapList(square, [1, 2, 3, 4, 5])
    
    # Check the transformed values using indexing
    assert ml[0] == 1
    assert ml[1] == 4
    assert ml[2] == 9
    assert ml[3] == 16
    assert ml[4] == 25
    
    # Test with a list of integers and a lambda function to square each element using __getitem__ method
    ml = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
    
    # Check the transformed values using indexing
    assert ml[0] == 1
    assert ml[1] == 4
    assert ml[2] == 9
    assert ml[3] == 16
    assert ml[4] == 25

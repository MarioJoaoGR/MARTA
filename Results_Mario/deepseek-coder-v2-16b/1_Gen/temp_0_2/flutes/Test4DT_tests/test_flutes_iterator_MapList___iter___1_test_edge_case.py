
from flutes.iterator import MapList
import pytest
from typing import Callable, Iterator, Sequence, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_edge_case():
    # Define a simple function and list for testing
    def square(x: T) -> R:
        return x * x  # Assuming x is of type int or float
    
    lst = [1, 2, 3, 4, 5]
    
    # Create an instance of MapList with the square function and list
    map_list = MapList(square, lst)
    
    # Use iter to get the iterator and convert it to a list to check the results
    result_list = list(map(lambda x: square(x), lst))  # Expected output is [1, 4, 9, 16, 25]
    
    # Check if the MapList iterator produces the expected results
    assert list(map_list) == result_list

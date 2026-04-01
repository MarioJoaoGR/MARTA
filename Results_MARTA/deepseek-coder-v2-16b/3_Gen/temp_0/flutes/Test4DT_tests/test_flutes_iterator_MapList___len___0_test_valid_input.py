
import pytest
from flutes.iterator import MapList

def test_valid_input():
    # Create a sample list
    lst = [1, 2, 3, 4, 5]
    
    # Initialize MapList with a lambda function that doubles each element
    maplist = MapList(lambda x: x * 2, lst)
    
    # Check the length of the transformed list
    assert len(maplist) == len(lst)

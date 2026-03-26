
import pytest
from flutes.iterator import MapList
from typing import Callable, Sequence

# Define the test case
def test_valid_case():
    func = lambda x: x * 2
    lst = [1, 2, 3, 4, 5]
    maplist_instance = MapList(func, lst)
    
    # Check if the instance is iterable
    assert hasattr(maplist_instance, '__iter__')
    
    # Convert to list and check the transformed values
    mapped_values = list(maplist_instance)
    expected_values = [2, 4, 6, 8, 10]
    assert mapped_values == expected_values

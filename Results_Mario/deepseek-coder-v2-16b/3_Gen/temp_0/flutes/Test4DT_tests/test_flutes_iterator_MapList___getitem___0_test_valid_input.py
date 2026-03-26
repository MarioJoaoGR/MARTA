
import pytest
from flutes.iterator import MapList
from typing import List, Callable

def test_valid_input():
    func = lambda x: x * 2
    lst = [1, 2, 3]
    map_list = MapList(func, lst)
    
    # Check the length of the transformed list
    assert len(map_list) == len(lst)
    
    # Check individual elements in the transformed list
    for i in range(len(lst)):
        assert map_list[i] == func(lst[i])

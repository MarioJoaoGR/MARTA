
import pytest
from flutes.iterator import MapList

def test_valid_input():
    lst = [1, 2, 3, 4, 5]
    func = lambda x: x * x
    map_list = MapList(func, lst)
    
    assert len(map_list) == len(lst)

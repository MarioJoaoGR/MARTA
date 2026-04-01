
import pytest
from flutes.iterator import MapList

def test_valid_input():
    func = lambda x: x * x
    lst = [1, 2, 3, 4, 5]
    maplist = MapList(func, lst)
    
    # Test indexing
    assert maplist[0] == 1
    assert maplist[1] == 4
    assert maplist[2] == 9
    assert maplist[3] == 16
    assert maplist[4] == 25
    
    # Test slicing
    assert list(maplist[:]) == [1, 4, 9, 16, 25]
    assert list(maplist[1:4]) == [4, 9, 16]

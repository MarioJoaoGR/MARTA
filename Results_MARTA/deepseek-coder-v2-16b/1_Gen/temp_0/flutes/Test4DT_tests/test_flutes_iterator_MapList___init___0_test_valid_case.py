
import pytest
from flutes.iterator import MapList

def test_valid_case():
    func = lambda x: x * x
    lst = [1, 2, 3, 4, 5]
    
    maplist = MapList(func, lst)
    
    # Check the transformed list elements
    assert list(maplist) == [1, 4, 9, 16, 25]
    
    # Check indexing
    assert maplist[0] == 1
    assert maplist[1] == 4
    assert maplist[2] == 9
    assert maplist[3] == 16
    assert maplist[4] == 25

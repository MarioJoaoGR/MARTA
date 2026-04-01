
import pytest
from flutes.iterator import MapList

def test_valid_input():
    func = lambda x: x * x
    lst = [1, 2, 3, 4, 5]
    maplist = MapList(func, lst)
    
    # Test indexing access
    assert maplist[0] == 1
    assert maplist[1] == 4
    assert maplist[2] == 9
    assert maplist[3] == 16
    assert maplist[4] == 25
    
    # Test slicing access
    assert list(maplist[:]) == [1, 4, 9, 16, 25]
    assert list(maplist[1:]) == [4, 9, 16, 25]
    assert list(maplist[:3]) == [1, 4, 9]
    assert list(maplist[1:4]) == [4, 9, 16]
    
    # Test invalid index access raises IndexError
    with pytest.raises(IndexError):
        maplist[5]

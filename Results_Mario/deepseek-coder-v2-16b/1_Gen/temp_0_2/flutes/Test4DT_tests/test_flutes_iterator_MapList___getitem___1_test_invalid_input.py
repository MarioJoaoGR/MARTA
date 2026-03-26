
import pytest
from flutes.iterator import MapList

def test_invalid_input():
    func = lambda x: 'a'
    lst = [1, 2]
    maplist = MapList(func, lst)
    
    with pytest.raises(IndexError):
        # Attempt to access an invalid index
        _ = maplist[3]

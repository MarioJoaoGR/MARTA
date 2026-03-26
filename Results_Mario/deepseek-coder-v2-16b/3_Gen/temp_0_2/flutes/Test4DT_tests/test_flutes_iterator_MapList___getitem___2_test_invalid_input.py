
import pytest
from flutes.iterator import MapList

def test_invalid_input():
    func = lambda x: x * x
    lst = [1, 2, 3]
    maplist = MapList(func, lst)
    
    with pytest.raises(TypeError):
        # Test invalid index access
        maplist[None]
        
    with pytest.raises(IndexError):
        # Test out of bounds index access
        maplist[-4]


import pytest
from flutes.iterator import MapList

def test_invalid_inputs():
    # Test with None as the transformation function
    lst = [1, 2, 3, 4, 5]
    maplist = MapList(None, lst)
    
    with pytest.raises(TypeError):
        _ = maplist[0]  # Accessing an item should trigger a TypeError due to the invalid transformation function


import pytest
from flutes.iterator import MapList

def test_invalid_input():
    # Create a MapList instance with a lambda function and an empty list
    maplist = MapList(lambda x: x * 2, [])
    
    # Attempt to access an item using an invalid index type (e.g., None)
    with pytest.raises(TypeError):
        _ = maplist[None]


import pytest
from flutes.iterator import MapList

def test_invalid_inputs():
    with pytest.raises(TypeError):
        ml = MapList(lambda x: x * x, [1, 2, 3, 4, 5])
        _ = ml[None]  # This should raise a TypeError as the index is not an integer

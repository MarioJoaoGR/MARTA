
import pytest
from flutes.iterator import LazyList

def test_invalid_inputs():
    # Test with None as iterable
    with pytest.raises(TypeError):
        LazyList(None)
    
    # Test with an integer (not iterable)
    with pytest.raises(TypeError):
        LazyList(12345)

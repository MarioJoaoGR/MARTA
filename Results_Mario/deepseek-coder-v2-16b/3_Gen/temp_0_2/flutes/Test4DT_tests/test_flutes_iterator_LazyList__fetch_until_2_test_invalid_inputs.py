
import pytest
from flutes.iterator import LazyList

def test_invalid_inputs():
    # Test with None as input
    with pytest.raises(TypeError):
        LazyList(None)  # This should raise a TypeError because the iterable is not provided

    # Test with an integer (which is not iterable)
    with pytest.raises(TypeError):
        LazyList(12345)  # This should raise a TypeError because 12345 is not iterable

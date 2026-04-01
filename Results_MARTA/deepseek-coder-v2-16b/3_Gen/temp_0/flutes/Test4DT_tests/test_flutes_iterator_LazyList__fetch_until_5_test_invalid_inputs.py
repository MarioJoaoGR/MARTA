
import pytest
from flutes.iterator import LazyList

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Passing an invalid input that is not an iterable should raise a TypeError
        LazyList(12345)  # Example of an invalid input (integer)

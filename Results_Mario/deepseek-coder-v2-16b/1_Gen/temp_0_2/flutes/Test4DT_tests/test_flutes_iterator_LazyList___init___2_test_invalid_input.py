
import pytest
from flutes.iterator import LazyList

def test_invalid_input():
    # Test initializing LazyList with an invalid iterable (e.g., a non-iterable)
    with pytest.raises(TypeError):
        LazyList(42)  # Passing an integer, which is not iterable


import pytest
from flutes.iterator import LazyList

def test_none_input():
    # Test that passing None to LazyList raises a TypeError
    with pytest.raises(TypeError):
        LazyList(None)

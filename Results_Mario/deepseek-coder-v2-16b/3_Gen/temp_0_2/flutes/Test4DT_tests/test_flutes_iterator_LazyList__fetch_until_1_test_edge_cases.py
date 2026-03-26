
import pytest
from flutes.iterator import LazyList

def test_edge_cases():
    with pytest.raises(TypeError):
        lst = LazyList(None)  # Passing None should raise a TypeError as per the error message provided

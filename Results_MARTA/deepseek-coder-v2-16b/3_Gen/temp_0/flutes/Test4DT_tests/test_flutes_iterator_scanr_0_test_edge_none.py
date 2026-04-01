
import pytest
from typing import Callable, Iterable, List
from flutes.iterator import scanr

def test_edge_none():
    # Test with None as input
    def add(x, y):
        return x + y
    
    with pytest.raises(TypeError):
        result = scanr(add, None)


import pytest
from typing import Callable, Iterable, List
from flutes.iterator import scanr

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test with a non-callable function
        result = scanr("not callable", [1, 2, 'a'], 0)
        
        # Test with an invalid iterable type (string instead of list)
        result = scanr(lambda x, y: x - y, "invalid iterable", 0)

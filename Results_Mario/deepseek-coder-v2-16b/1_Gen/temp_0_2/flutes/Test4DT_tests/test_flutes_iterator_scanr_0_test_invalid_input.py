
import pytest
from typing import Callable, Iterable, List, Any
from flutes.iterator import scanr

def test_invalid_input():
    func = lambda x, y: x + y
    iterable = None
    
    with pytest.raises(TypeError):
        scanr(func, iterable)

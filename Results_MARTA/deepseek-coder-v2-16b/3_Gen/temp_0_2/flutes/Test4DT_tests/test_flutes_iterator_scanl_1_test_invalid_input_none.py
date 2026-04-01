
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_invalid_input_none():
    func = lambda x, y: x + y
    iterable = None
    
    with pytest.raises(TypeError):
        list(scanl(func, iterable))

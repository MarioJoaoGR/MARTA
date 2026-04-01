
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_invalid_input():
    with pytest.raises(TypeError):
        # Passing None instead of a callable function
        list(scanl(None, [1, 2, 3]))
    
    with pytest.raises(TypeError):
        # Passing a non-callable object (e.g., an integer)
        list(scanl(42, [1, 2, 3]))

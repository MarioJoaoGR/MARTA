
from flutes.iterator import scanr
from typing import Callable, Iterable, List
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test that passing a non-callable function raises a TypeError
        scanr(123, [1, 2, 3])

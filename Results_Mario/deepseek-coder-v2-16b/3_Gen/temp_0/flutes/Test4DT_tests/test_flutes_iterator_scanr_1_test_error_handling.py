
import pytest
from flutes.iterator import scanr
from typing import Callable, Iterable, List

def test_error_handling():
    with pytest.raises(TypeError):
        # Test case for non-callable function
        scanr(None, [1, 2, 3], 0)

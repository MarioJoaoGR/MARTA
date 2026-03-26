
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_error_case_invalid_input():
    with pytest.raises(TypeError):
        # Test case for invalid input types
        list(scanl(lambda acc, x: acc + x, "not an iterable", 0))

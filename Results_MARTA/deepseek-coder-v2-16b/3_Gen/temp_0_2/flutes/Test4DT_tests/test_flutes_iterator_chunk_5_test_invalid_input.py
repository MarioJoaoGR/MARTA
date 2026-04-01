
import pytest
from flutes.iterator import chunk
from typing import List, Iterable

def test_invalid_input():
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))  # Test with n = 0
        list(chunk(-1, range(10)))  # Test with negative n

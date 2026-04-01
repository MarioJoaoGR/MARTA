
from flutes.iterator import chunk
import pytest
from typing import Iterable, List, Iterator

def test_invalid_inputs():
    with pytest.raises(ValueError):
        list(chunk(-1, range(5)))  # Test with negative number
        list(chunk(0, range(5)))   # Test with zero
        list(chunk(-1, "string"))  # Test with negative number and string
        list(chunk(0, "string"))    # Test with zero and string


import pytest
from typing import Iterable, List, Iterator, TypeVar
from flutes.iterator import chunk

T = TypeVar('T')

def test_chunk_invalid_n():
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))  # Test when n is zero

    with pytest.raises(ValueError):
        list(chunk(-1, range(10)))  # Test when n is negative

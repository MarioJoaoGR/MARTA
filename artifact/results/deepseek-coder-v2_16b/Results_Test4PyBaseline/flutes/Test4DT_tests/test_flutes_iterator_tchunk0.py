
import pytest
from typing import Iterable, List, Iterator, TypeVar
from flutes.iterator import chunk

T = TypeVar('T')

def test_chunk_basic():
    assert list(chunk(3, range(10))) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

def test_chunk_non_positive_integer():
    with pytest.raises(ValueError) as e:
        list(chunk(-1, range(10)))
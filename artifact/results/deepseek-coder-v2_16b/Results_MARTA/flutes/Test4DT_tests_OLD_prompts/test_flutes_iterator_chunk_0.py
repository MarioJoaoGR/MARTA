
import pytest
from flutes.iterator import chunk
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def test_positive_number():
    iterable = range(10)
    n = 3
    result = list(chunk(n, iterable))
    assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

def test_negative_number():
    iterable = range(10)
    n = -1
    with pytest.raises(ValueError):
        list(chunk(n, iterable))

def test_zero():
    iterable = range(10)
    n = 0
    with pytest.raises(ValueError):
        list(chunk(n, iterable))

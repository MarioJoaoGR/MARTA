
import pytest
from flutes.iterator import drop
from typing import Iterator, Iterable, TypeVar

T = TypeVar('T')

def test_drop_positive_n():
    result = drop(5, range(10))
    assert list(result) == [5, 6, 7, 8, 9]

def test_drop_zero_n():
    result = drop(0, [1, 2, 3, 4, 5])
    assert list(result) == [1, 2, 3, 4, 5]

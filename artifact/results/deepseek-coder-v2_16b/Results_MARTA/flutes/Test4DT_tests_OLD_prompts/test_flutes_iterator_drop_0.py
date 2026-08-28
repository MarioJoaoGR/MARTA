
import pytest
from flutes.iterator import drop
from typing import Iterator, Iterable

def test_drop_positive_n():
    result = drop(5, range(1000000))
    assert next(result) == 5

def test_drop_zero_n():
    result = drop(0, [1, 2, 3, 4, 5])
    assert list(result) == [1, 2, 3, 4, 5]

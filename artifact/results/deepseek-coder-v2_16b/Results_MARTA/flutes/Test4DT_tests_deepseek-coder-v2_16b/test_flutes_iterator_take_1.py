
import pytest
from flutes.iterator import take
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_none_iterable():
    with pytest.raises(TypeError):
        list(take(5, None))

def test_negative_n():
    with pytest.raises(ValueError):
        list(take(-1, range(10)))

def test_zero_n():
    assert list(take(0, range(10))) == []

def test_positive_n():
    iterable = [1, 2, 3, 4, 5]
    expected = [1, 2, 3]
    result = list(take(3, iterable))
    assert result == expected

def test_large_n():
    iterable = [10, 20, 30, 40, 50]
    expected = [10, 20, 30, 40, 50]
    result = list(take(10, iterable))
    assert result == expected

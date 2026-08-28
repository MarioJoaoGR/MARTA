
import pytest
from flutes.iterator import scanr
from typing import Callable, Iterable, List
import operator

def test_scanr_basic():
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

def test_scanr_lambda():
    result = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result == ['abcd', 'bcd', 'cd', 'd']

def test_scanr_different_initial():
    result = scanr(operator.add, [1, 2, 3, 4], 5)
    assert result == [15, 14, 12, 9, 5]

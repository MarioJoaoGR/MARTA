
import pytest
from flutes.iterator import scanr
import operator

# Test cases for scanr function
def test_scanr_basic():
    result = scanr(operator.add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0]

def test_scanr_lambda():
    result = scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
    assert result == ['abcd', 'bcd', 'cd', 'd']

def test_scanr_no_initial():
    result = scanr(operator.add, [1, 2, 3, 4])
    assert result == [10, 9, 7, 4]

def test_scanr_different_iterable():
    result = scanr(lambda s, x: s + x, (5, 6, 7, 8))
    assert result == [26, 21, 15, 8]

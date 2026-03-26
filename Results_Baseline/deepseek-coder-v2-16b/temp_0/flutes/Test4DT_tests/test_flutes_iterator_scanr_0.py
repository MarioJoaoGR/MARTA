
import pytest
from typing import Callable, Iterable, List
from flutes.iterator import scanr
import operator

# Helper function to add two numbers
def add(x: int, y: int) -> int:
    return x + y

# Helper function to multiply two numbers
def mul(x: int, y: int) -> int:
    return x * y

# Test cases for scanr with add function
@pytest.mark.parametrize("func, iterable, initial, expected", [
    (add, [1, 2, 3], 0, [6, 5, 3, 0]),
])
def test_scanr_with_add(func, iterable, initial, expected):
    result = scanr(func, iterable, initial)
    assert result == expected

# Test cases for scanr with mul function
@pytest.mark.parametrize("func, iterable, initial, expected", [
    (mul, [1, 2, 3], 1, [1, 2, 6, 24]),
])
def test_scanr_with_mul(func, iterable, initial, expected):
    result = scanr(func, iterable, initial)  
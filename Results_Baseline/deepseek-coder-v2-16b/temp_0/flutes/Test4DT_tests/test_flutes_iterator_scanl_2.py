# Module: flutes.iterator
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

# Helper functions for testing
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Test cases for scanl function
@pytest.mark.parametrize("func, iterable, expected", [
    (add, [1, 2, 3, 4], [1, 3, 6, 10]),
    (multiply, [1, 2, 3, 4], [1, 2, 6, 24]),
    (lambda x, y: x + y, [1, 2, 3, 4], [1, 3, 6, 10]),  # Lambda function for addition test
    (lambda x, y: x * y, [1, 2, 3, 4], [1, 2, 6, 24]),  # Lambda function for multiplication test
])
def test_scanl(func, iterable, expected):
    result = list(scanl(func, iterable))
    assert result == expected, f"Expected {expected} but got {result}"

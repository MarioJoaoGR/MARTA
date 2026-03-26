
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

# Helper functions for testing
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Test cases for scanl function
def test_scanl_addition():
    result = list(scanl(add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]

def test_scanl_multiplication():
    result = list(scanl(multiply, [1, 2, 3, 4]))
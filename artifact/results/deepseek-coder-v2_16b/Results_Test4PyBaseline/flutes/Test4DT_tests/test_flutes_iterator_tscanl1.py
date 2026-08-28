
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

# Helper function to convert iterator to list for easy comparison
def list_from_scanl(func, iterable):
    result = []
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return []
    for item in it:
        result.append(prev)
        prev = func(prev, item)
    result.append(prev)
    return result

# Test cases for scanl function
def test_scanl_basic():
    def add(x, y):
        return x + y
    
    numbers = [1, 2, 3, 4]
    expected = list_from_scanl(add, numbers)
    result = list(scanl(add, numbers))
    assert result == expected

def test_scanl_lambda():
    numbers = [5, 10, 15, 20]
    expected = list_from_scanl(lambda x, y: x + y, numbers)
    result = list(scanl(lambda x, y: x + y, numbers))
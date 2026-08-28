
# Module: flutes.iterator
# Import the function using its provided module name.
from flutes.iterator import drop
import pytest
import itertools

# Test cases for the `drop` function.

def test_drop_from_list():
    result = drop(3, [0, 1, 2, 3, 4, 5])
    assert list(result) == [3, 4, 5]

def test_drop_from_tuple():
    result = drop(2, (0, 1, 2, 3, 4, 5))
    assert list(result) == [2, 3, 4, 5]

def test_drop_from_range():
    result = drop(5, range(10))
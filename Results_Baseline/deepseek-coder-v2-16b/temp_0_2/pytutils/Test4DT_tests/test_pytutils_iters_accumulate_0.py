# Module: pytutils.iters
import pytest
import operator
from pytutils.iters import accumulate

# Test cases for the default addition function
def test_accumulate_default():
    result = list(accumulate([1, 2, 3, 4, 5]))
    assert result == [1, 3, 6, 10, 15]

# Test cases for the custom multiplication function
def test_accumulate_custom_function():
    result = list(accumulate([1, 2, 3, 4, 5], operator.mul))
    assert result == [1, 2, 6, 24, 120]

# Test case for an empty iterable
def test_accumulate_empty():
    result = list(accumulate([]))
    assert result == []

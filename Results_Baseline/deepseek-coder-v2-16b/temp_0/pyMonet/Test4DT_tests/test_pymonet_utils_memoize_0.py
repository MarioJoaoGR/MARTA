
import pytest
from pymonet.utils import memoize
from typing import Callable, List, Any
from operator import eq

# Assuming the find function is defined elsewhere in the module or context
def find(lst, predicate):
    for item in lst:
        if predicate(item):
            return item
    return None

# Test cases for memoize function
@pytest.fixture
def add():
    def _add(x):
        print("Calculating...")
        return x + 1
    return _add

@pytest.fixture
def custom_key():
    return lambda a, b: a == b

# Test basic memoization behavior
def test_memoize_basic(add):
    memoized_add = memoize(add)
    assert memoized_add(5) == 6  # First call calculates and caches the result for 5.
    assert memoized_add(5) == 6  # Second call returns cached result since 5 was already calculated.

# Test with custom key function
def test_memoize_custom_key(add, custom_key):
    memoized_add = memoize(add, key=custom_key)
    assert memoized_add(5) == 6  # First call calculates and caches the result for 5 using the custom key function.
    assert memoized_add(5) == 6  # Subsequent calls return cached results since 5 was already calculated.

# Test with lambda key function
def test_memoize_lambda_key(add):
    memoized_add = memoize(add, key=lambda a, b: a == b)
    assert memoized_add(5) == 6  # First call calculates and caches the result for 5 using a lambda key function.
    assert memoized_add(5) == 6  # Subsequent calls return cached results since 5 was already calculated.

# Edge case: Test with None as an argument
def test_memoize_none_argument(add):
    memoized_add = memoize(add)
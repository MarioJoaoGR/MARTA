
import pytest
from pymonet.utils import memoize
from functools import cmp_to_key

# Mocking necessary functions or classes if required by your environment
def slow_function(x):
    # Imagine this is a computation-heavy function
    return x * 2

def test_valid_input():
    memoized_slow_function = memoize(slow_function, key=lambda x, y: x == y)
    
    # First call will compute the result
    assert memoized_slow_function(5) == 10
    
    # Second call with the same argument uses the cached result
    assert memoized_slow_function(5) == 10

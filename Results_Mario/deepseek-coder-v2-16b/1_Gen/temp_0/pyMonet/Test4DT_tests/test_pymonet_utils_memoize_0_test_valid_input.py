
import pytest
from pymonet.utils import memoize
from typing import Callable, List, Any
from operator import eq

def find(lst, fn):
    for item in lst:
        if fn(item):
            return item
    return None

def test_valid_input():
    def add(x):
        print("Calculating...")
        return x + 1
    
    memoized_add = memoize(add, key=eq)
    
    # First call should calculate the result
    assert memoized_add(5) == 6
    # Second call with the same argument should return the cached result
    assert memoized_add(5) == 6
    # Call with a different argument should calculate the result again
    assert memoized_add(10) == 11

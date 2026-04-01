
import pytest
from pymonet.utils import curried_filter

def is_even(n):
    return n % 2 == 0

def test_valid_input():
    # Test case 1: Filtering even numbers from a list of integers
    result = curried_filter(is_even, [1, 2, 3, 4])
    assert result == [2, 4]
    
    # Test case 2: Filtering integers from a mixed iterable
    result = curried_filter(lambda x: isinstance(x, int), ['a', 1, 'b', 2])
    assert result == [1, 2]

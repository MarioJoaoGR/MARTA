
import pytest
from pytutils.iters import accumulate
import operator

def test_valid_inputs():
    # Test with default function (addition)
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    
    # Test with multiplication function
    assert list(accumulate([1, 2, 3, 4, 5], operator.mul)) == [1, 2, 6, 24, 120]
    
    # Test with custom function
    def multiply_by_two(x, y):
        return x * y
    
    assert list(accumulate([1, 2, 3, 4, 5], multiply_by_two)) == [1, 2, 6, 24, 120]
    
    # Test with empty iterable
    assert list(accumulate([])) == []

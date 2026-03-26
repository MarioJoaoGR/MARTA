
import pytest
from pytutils.iters import accumulate
import operator

def test_valid_input():
    # Test with a list of numbers and default addition function
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    
    # Test with a list of numbers and multiplication function
    assert list(accumulate([1, 2, 3, 4, 5], operator.mul)) == [1, 2, 6, 24, 120]

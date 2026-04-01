
import pytest
from itertools import accumulate
from operator import mul
from flutes.iterator import scanl

def test_valid_multiplication():
    # Test case 1: Multiplying a list of numbers [1, 2, 3, 4]
    result = list(scanl(mul, [1, 2, 3, 4]))
    assert result == list(accumulate(range(1, 5), mul))
    
    # Test case 2: Multiplying a list of numbers [5, 10, 15]
    result = list(scanl(mul, [5, 10, 15]))
    assert result == list(accumulate([5, 10, 15], mul))
    
    # Test case 3: Multiplying a list of numbers [7, 8]
    result = list(scanl(mul, [7, 8]))
    assert result == list(accumulate([7, 8], mul))


import pytest
from flutes.iterator import scanl

def test_valid_case():
    # Test case 1: Summation with initial value 0
    result = list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]
    
    # Test case 2: Multiplication with initial value 1
    result = list(scanl(lambda acc, x: acc * x, [1, 2, 3, 4], 1))
    assert result == [1, 1, 2, 6, 24]
    
    # Test case 3: Max with initial value -inf
    result = list(scanl(max, [1, 3, 2, 5, 4], float('-inf')))
    assert result == [-float('inf'), 1, 3, 3, 5, 5]

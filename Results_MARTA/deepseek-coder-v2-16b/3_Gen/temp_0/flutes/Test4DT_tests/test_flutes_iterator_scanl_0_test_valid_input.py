
import pytest
from flutes.iterator import scanl

def test_valid_input():
    # Test case 1: Adding numbers with an initial value of 0
    result = list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]
    
    # Test case 2: Multiplying numbers with an initial value of 1
    result = list(scanl(lambda acc, x: acc * x, [1, 2, 3, 4], 1))
    assert result == [1, 1, 2, 6, 24]
    
    # Test case 3: Using max function with an initial value of negative infinity
    result = list(scanl(max, [1, 3, 2, 5, 4], float('-inf')))
    assert result == [-float('inf'), 1, 3, 3, 5, 5]

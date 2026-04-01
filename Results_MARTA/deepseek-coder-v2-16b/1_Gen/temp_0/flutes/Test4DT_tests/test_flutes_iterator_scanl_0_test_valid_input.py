
import pytest
from flutes.iterator import scanl
from typing import Callable, Iterable, Iterator

def test_valid_input():
    # Test case 1: Summing cumulative values
    result = list(scanl(lambda acc, x: acc + x, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]
    
    # Test case 2: Multiplying cumulative values
    result = list(scanl(lambda acc, x: acc * x, [1, 2, 3, 4], 1))
    assert result == [1, 1, 2, 6, 24]
    
    # Test case 3: Using max function with initial value of negative infinity
    result = list(scanl(max, [1, 3, 2, 5, 4], float('-inf')))
    assert result == [-float('inf'), 1, 3, 3, 5, 5]

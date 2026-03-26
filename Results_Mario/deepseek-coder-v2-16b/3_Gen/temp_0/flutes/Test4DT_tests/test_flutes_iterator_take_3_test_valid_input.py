
import pytest
from flutes.iterator import take
from typing import Iterable, Iterator, TypeVar

T = TypeVar('T')

def test_valid_input():
    # Test case with valid input
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]
    
    # Test case with n greater than the length of the iterable
    result = list(take(15, range(10)))
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Test case with n equal to zero
    result = list(take(0, range(10)))
    assert result == []
    
    # Test case with negative n, should raise ValueError
    with pytest.raises(ValueError):
        list(take(-5, range(10)))

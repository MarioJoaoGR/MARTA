
from flutes.iterator import take  # Importing the take function from the iterator module
import pytest
from typing import Iterator, Iterable

def test_valid_input():
    T = type(None)  # Assuming T is a type variable for the iterable elements
    
    # Test case with valid input
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]

    # Test case with n=0
    result_zero = list(take(0, range(10)))
    assert result_zero == []

    # Test case with negative n
    with pytest.raises(ValueError):
        list(take(-1, range(10)))

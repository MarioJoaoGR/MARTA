
import pytest
from flutes.iterator import take

def test_valid_input():
    # Test case for valid input where n is greater than the length of the iterable
    result = list(take(5, range(10)))
    assert result == [0, 1, 2, 3, 4]

    # Test case for valid input where n is equal to the length of the iterable
    result = list(take(10, range(10)))
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case for valid input where n is less than the length of the iterable
    result = list(take(3, range(10)))
    assert result == [0, 1, 2]

    # Test case for valid input where n is zero
    result = list(take(0, range(10)))
    assert result == []

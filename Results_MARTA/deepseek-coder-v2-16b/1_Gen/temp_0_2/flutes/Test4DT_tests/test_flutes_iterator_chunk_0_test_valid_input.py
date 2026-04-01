
from flutes.iterator import chunk
from typing import Iterable, List, Iterator, Type
import pytest

def test_valid_input():
    # Test with a valid input where n is greater than 0
    iterable = range(10)
    n = 3
    expected_output = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    result = list(chunk(n, iterable))
    assert result == expected_output

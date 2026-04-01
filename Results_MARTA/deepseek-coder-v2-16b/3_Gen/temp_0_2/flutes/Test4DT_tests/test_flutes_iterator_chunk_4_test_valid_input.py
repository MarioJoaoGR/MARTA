
import pytest
from flutes.iterator import chunk
from typing import List, Iterable

def test_valid_input():
    # Test case 1: Chunking a range into chunks of 3 elements each
    test_iterable = range(10)
    n = 3
    expected_output = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    result = list(chunk(n, test_iterable))
    assert result == expected_output


import pytest
from typing import Iterable, List, Iterator
from flutes.iterator import chunk

def test_valid_input():
    test_iterable = range(10)
    n = 3
    expected_output = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
    result = list(chunk(n, test_iterable))
    
    assert result == expected_output

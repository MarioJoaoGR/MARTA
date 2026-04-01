
import pytest
from flutes.iterator import split_by
from typing import List, Iterable

def test_valid_case_criterion():
    iterable = range(10)
    criterion = lambda x: x % 3 == 0
    expected_output = [[1, 2], [4, 5], [7, 8]]
    
    result = list(split_by(iterable, criterion=criterion))
    assert result == expected_output

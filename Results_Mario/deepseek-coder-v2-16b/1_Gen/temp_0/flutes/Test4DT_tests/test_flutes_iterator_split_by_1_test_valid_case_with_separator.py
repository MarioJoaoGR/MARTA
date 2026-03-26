
import pytest
from flutes.iterator import split_by
from typing import List, Iterable

def test_valid_case_with_separator():
    iterable = ' Split by: '
    expected_output = [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]
    
    result = list(split_by(iterable, empty_segments=True, separator=' '))
    
    assert result == expected_output

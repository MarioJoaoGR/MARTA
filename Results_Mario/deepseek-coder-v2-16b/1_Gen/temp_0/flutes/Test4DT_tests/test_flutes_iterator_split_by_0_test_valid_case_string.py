
import pytest
from flutes.iterator import split_by

def test_valid_case_string():
    iterable = 'hello world'
    separator = ' '
    expected_output = [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']]
    
    result = list(split_by(iterable, empty_segments=False, separator=separator))
    
    assert result == expected_output

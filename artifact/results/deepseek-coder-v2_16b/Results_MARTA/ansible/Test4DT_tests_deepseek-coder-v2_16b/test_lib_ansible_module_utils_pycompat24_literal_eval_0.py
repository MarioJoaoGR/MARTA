
import pytest
from ast import literal_eval

def test_valid_case_string():
    result = literal_eval('1 + 2')
    assert result == 3

def test_edge_case_none():
    result = literal_eval('None')
    assert result is None

def test_invalid_input():
    with pytest.raises(ValueError):
        literal_eval('invalid input')

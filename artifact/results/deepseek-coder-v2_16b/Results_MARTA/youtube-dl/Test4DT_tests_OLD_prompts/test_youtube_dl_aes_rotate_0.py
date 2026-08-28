
import pytest
from unittest.mock import patch

def rotate(data):
    if isinstance(data, list) and len(data) > 0:
        return data[1:] + [data[0]]
    elif not isinstance(data, list):
        raise ValueError("Input must be a list")
    else:
        return []

# Test cases for rotate function

def test_valid_input():
    assert rotate([1, 2, 3]) == [2, 3, 1]
    assert rotate(['a', 'b', 'c']) == ['b', 'c', 'a']

def test_empty_list():
    assert rotate([]) == []

def test_invalid_input():
    with pytest.raises(ValueError):
        rotate("not a list")


import pytest
from youtube_dl.aes import xor

# Test cases for the xor function

def test_basic_usage():
    result = xor([1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 5]

def test_boolean_values():
    result = xor([True, False], [False, True])
    assert result == [True, True]

def test_different_lengths():
    result = xor([1, 2], [3, 4, 5])
    assert len(result) == 2 and all(r == expected for r, expected in zip(result, [2]))

def test_empty_lists():
    result = xor([], [])
    assert result == []

def test_one_empty_list():
    result = xor([1, 2, 3], [])
    assert result == []

def test_non_integer_types():
    with pytest.raises(TypeError):
        xor([True, "string"], [False, True])

def test_non_list_input():
    with pytest.raises(TypeError):
        xor("not a list", [1, 2, 3])

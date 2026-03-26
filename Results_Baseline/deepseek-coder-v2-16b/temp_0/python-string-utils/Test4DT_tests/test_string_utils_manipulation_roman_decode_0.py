# Module: string_utils.manipulation
# test_string_utils.py
from string_utils import manipulation
import pytest

def test_roman_decode_valid():
    assert manipulation.roman_decode('VII') == 7

def test_roman_decode_invalid_none():
    with pytest.raises(ValueError):
        manipulation.roman_decode(None)

def test_roman_decode_invalid_empty():
    with pytest.raises(ValueError):
        manipulation.roman_decode('')

def test_roman_decode_invalid_whitespace():
    with pytest.raises(ValueError):
        manipulation.roman_decode(' ')

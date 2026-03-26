# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode_integer():
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'

def test_roman_encode_string():
    assert roman_encode('2020') == 'MMXX'
    assert roman_encode('37') == 'XXXVII'

def test_roman_encode_invalid_integer():
    with pytest.raises(ValueError):
        roman_encode(-5)

def test_roman_encode_invalid_string():
    with pytest.raises(ValueError):
        roman_encode('abcd')

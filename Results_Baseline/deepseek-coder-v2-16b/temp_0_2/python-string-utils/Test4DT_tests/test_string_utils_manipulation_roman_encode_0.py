# Module: string_utils.manipulation
# test_string_utils_manipulation.py
from string_utils.manipulation import roman_encode
import pytest
from typing import Union

def test_roman_encode_integer():
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode(2020) == 'MMXX'

def test_roman_encode_string():
    assert roman_encode('37') == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'

def test_roman_encode_invalid_number():
    with pytest.raises(ValueError):
        roman_encode(-1)
    with pytest.raises(ValueError):
        roman_encode('abc')

def test_roman_encode_non_integer_input():
    with pytest.raises(ValueError):
        roman_encode('123a')

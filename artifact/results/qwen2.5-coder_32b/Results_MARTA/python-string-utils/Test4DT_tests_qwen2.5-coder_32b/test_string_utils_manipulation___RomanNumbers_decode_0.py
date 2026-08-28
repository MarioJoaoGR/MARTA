
import pytest
from string_utils.manipulation import __RomanNumbers

def test_decode_valid_roman_numeral():
    assert __RomanNumbers.decode('III') == 3

def test_decode_subtractive_combination():
    assert __RomanNumbers.decode('IX') == 9

def test_decode_complex_roman_numeral():
    assert __RomanNumbers.decode('MCMXCIV') == 1994

def test_decode_large_number():
    assert __RomanNumbers.decode('MMXXIII') == 2023


def test_decode_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        __RomanNumbers.decode('')


def test_decode_mixed_case_roman_numeral():
    assert __RomanNumbers.decode('mCmXcIv') == 1994
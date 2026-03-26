
import pytest
from string_utils.manipulation import roman_decode

def test_valid_roman_numeral():
    assert roman_decode('VII') == 7
    assert roman_decode('IV') == 4
    assert roman_decode('IX') == 9
    assert roman_decode('LVIII') == 58
    assert roman_decode('MCMXCIV') == 1994

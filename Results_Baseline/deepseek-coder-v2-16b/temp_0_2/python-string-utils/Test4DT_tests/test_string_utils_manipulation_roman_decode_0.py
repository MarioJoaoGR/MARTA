
import pytest
from string_utils.manipulation import roman_decode

def test_roman_decode_valid():
    assert roman_decode('VII') == 7
    assert roman_decode('XIV') == 14
    assert roman_decode('XXVI') == 26
    assert roman_decode('XLII') == 42
    assert roman_decode('LVIII') == 58
    assert roman_decode('XCIV') == 94
    assert roman_decode('CDXLIV') == 444
    assert roman_decode('MMMCMXCIX') == 3999

def test_roman_decode_invalid_empty():
    with pytest.raises(ValueError) as e:
        roman_decode('')
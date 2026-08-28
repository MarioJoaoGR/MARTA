# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import roman_encode

def test_roman_encode_valid_integers():
    assert roman_encode(1) == 'I'
    assert roman_encode(4) == 'IV'
    assert roman_encode(9) == 'IX'
    assert roman_encode(58) == 'LVIII'
    assert roman_encode(1994) == 'MCMXCIV'
    assert roman_encode(3999) == 'MMMCMXCIX'

def test_roman_encode_valid_strings():
    assert roman_encode('1') == 'I'
    assert roman_encode('4') == 'IV'
    assert roman_encode('9') == 'IX'
    assert roman_encode('58') == 'LVIII'
    assert roman_encode('1994') == 'MCMXCIV'
    assert roman_encode('3999') == 'MMMCMXCIX'

def test_roman_encode_invalid_integers():
    with pytest.raises(ValueError):
        roman_encode(0)
    with pytest.raises(ValueError):
        roman_encode(4000)

def test_roman_encode_invalid_strings():
    with pytest.raises(ValueError):
        roman_encode('0')
    with pytest.raises(ValueError):
        roman_encode('4000')

def test_roman_encode_non_numeric_string():
    with pytest.raises(ValueError):
        roman_encode('abc')
    with pytest.raises(ValueError):
        roman_encode('123a')

def test_roman_encode_negative_numbers():
    with pytest.raises(ValueError):
        roman_encode(-1)
    with pytest.raises(ValueError):
        roman_encode('-500')

def test_roman_encode_floats():
    with pytest.raises(ValueError):
        roman_encode(1.5)
    with pytest.raises(ValueError):
        roman_encode('2.3')


import pytest
from string_utils.manipulation import __RomanNumbers  # Assuming this is the correct module path

def test_decode_valid_roman():
    assert __RomanNumbers.decode('XIV') == 14
    assert __RomanNumbers.decode('XXVII') == 27
    assert __RomanNumbers.decode('XLII') == 42
    assert __RomanNumbers.decode('XCIV') == 94
    assert __RomanNumbers.decode('CDXLIII') == 443
    assert __RomanNumbers.decode('MMXVIII') == 2018

def test_decode_invalid_input():
    with pytest.raises(ValueError):
        __RomanNumbers.decode('')
    with pytest.raises(ValueError):
        __RomanNumbers.decode(None)
    with pytest.raises(ValueError):
        __RomanNumbers.decode(1234)  # Non-string input

def test_decode_edge_cases():
    assert __RomanNumbers.decode('I') == 1
    assert __RomanNumbers.decode('V') == 5
    assert __RomanNumbers.decode('X') == 10
    assert __RomanNumbers.decode('L') == 50
    assert __RomanNumbers.decode('C') == 100
    assert __RomanNumbers.decode('D') == 500
    assert __RomanNumbers.decode('M') == 1000

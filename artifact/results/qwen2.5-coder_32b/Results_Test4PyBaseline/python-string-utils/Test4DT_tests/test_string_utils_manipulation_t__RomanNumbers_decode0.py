
# Test case  
import pytest
from string_utils.manipulation import __RomanNumbers

def test_decode_valid_roman_numerals():
    assert __RomanNumbers.decode('IX') == 9
    assert __RomanNumbers.decode('XIV') == 14
    assert __RomanNumbers.decode('XLII') == 42
    assert __RomanNumbers.decode('MCMXCIV') == 1994
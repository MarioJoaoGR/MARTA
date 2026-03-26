# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __RomanNumbers

# Test cases for valid Roman numeral conversions
def test_valid_roman_numerals():
    assert __RomanNumbers().decode('IX') == 9
    assert __RomanNumbers().decode('MCMXCIV') == 1994

# Test cases for invalid input (empty string)
def test_invalid_input():
    with pytest.raises(ValueError) as e:
        __RomanNumbers().decode('')
    assert str(e.value) == 'Input must be a non empty string'

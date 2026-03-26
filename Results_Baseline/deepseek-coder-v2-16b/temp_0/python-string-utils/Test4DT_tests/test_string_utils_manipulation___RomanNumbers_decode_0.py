# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __RomanNumbers

# Helper function to check if the input is a non-empty string
def is_full_string(input_str):
    return isinstance(input_str, str) and len(input_str.strip()) > 0

# Helper function to reverse a string
def reverse(s):
    return s[::-1]

# Test cases for the decode method of __RomanNumbers class
@pytest.mark.parametrize("roman_numeral, expected", [
    ('IX', 9),
    ('XIV', 14),
    ('XXVII', 27),
    ('XLII', 42),
    ('XCIX', 99),
    ('CDXLIV', 444),
    ('MMMCMXCIX', 3999)
])
def test_decode_valid_numerals(roman_numeral, expected):
    assert __RomanNumbers().decode(roman_numeral) == expected

@pytest.mark.parametrize("invalid_input", [
    '',
    None,
    ' ',
    'ABC'
])
def test_decode_invalid_inputs(invalid_input):
    with pytest.raises(ValueError):
        __RomanNumbers().decode(invalid_input)

# Additional edge cases to cover potential issues
def test_decode_empty_string():
    with pytest.raises(ValueError):
        __RomanNumbers().decode('')

def test_decode_none_input():
    with pytest.raises(ValueError):
        __RomanNumbers().decode(None)

def test_decode_whitespace_only():
    with pytest.raises(ValueError):
        __RomanNumbers().decode(' ')

def test_decode_non_roman_numeral():
    with pytest.raises(ValueError):
        __RomanNumbers().decode('ABC')

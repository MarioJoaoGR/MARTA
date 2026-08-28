# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __RomanNumbers

# Helper function to check if the input string is non-empty and contains only valid Roman numeral characters
def is_full_string(input_string):
    return len(input_string) > 0 and all(c in 'IVXLCDM' for c in input_string.upper())

# Helper function to reverse a string
def reverse(s):
    return s[::-1]

# Test cases for the decode method of __RomanNumbers class
@pytest.mark.parametrize("input_string, expected", [
    ('XIV', 14),
    ('MCMXCIV', 1994),
])
def test_decode_valid(input_string, expected):
    assert __RomanNumbers.decode(input_string) == expected

@pytest.mark.parametrize("input_string", [
    '', 'ABCD'
])
def test_decode_invalid(input_string):
    with pytest.raises(ValueError):
        if not is_full_string(input_string):
            __RomanNumbers.decode(input_string)

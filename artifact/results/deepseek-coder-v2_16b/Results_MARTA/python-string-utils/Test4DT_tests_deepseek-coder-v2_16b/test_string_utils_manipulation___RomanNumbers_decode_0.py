
import pytest
from string_utils.manipulation import __RomanNumbers

# Helper function to check if a string is non-empty
def is_full_string(input_string: str) -> bool:
    return len(input_string) > 0 and isinstance(input_string, str)

# Test for valid Roman numeral conversion
def test_valid_roman_numeral():
    roman_decoder = __RomanNumbers()
    assert roman_decoder.decode('XIV') == 14

# Test for invalid input (empty string)
def test_invalid_input_empty_string():
    with pytest.raises(ValueError):
        __RomanNumbers().decode('')

# Test for valid conversion with mixed case
def test_valid_mixed_case_conversion():
    roman_decoder = __RomanNumbers()
    assert roman_decoder.decode('xIv') == 14

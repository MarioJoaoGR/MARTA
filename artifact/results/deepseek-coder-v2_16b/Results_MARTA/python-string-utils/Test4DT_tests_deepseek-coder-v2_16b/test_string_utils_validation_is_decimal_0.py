
import pytest
from string_utils.validation import is_decimal

# Test valid decimal numbers including signed and scientific notation
def test_valid_decimal_numbers():
    input_string = '42.0'
    assert is_decimal(input_string) == True, f"Expected True for {input_string}, but got False"

# Test invalid strings that are not decimal numbers
def test_invalid_strings():
    input_string = 'abc'
    assert is_decimal(input_string) == False, f"Expected False for {input_string}, but got True"

# Test handling of None input
def test_none_input():
    input_string = None
    with pytest.raises(TypeError):
        is_decimal(input_string)

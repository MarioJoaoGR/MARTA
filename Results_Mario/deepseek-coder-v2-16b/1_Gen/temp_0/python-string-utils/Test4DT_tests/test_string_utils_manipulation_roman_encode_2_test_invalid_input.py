
import pytest
from string_utils.manipulation import roman_encode

def test_invalid_input():
    # Test cases with invalid inputs
    invalid_inputs = [
        "0",  # Zero is not a valid Roman numeral
        "-1", # Negative numbers are not allowed
        "4000", # Numbers greater than 3999 are not allowed
        "abc", # Non-numeric string
        None, # None is an invalid input type
        3.14, # Float is not a valid input type
    ]
    
    for input_value in invalid_inputs:
        with pytest.raises(ValueError):  # Expecting a ValueError for invalid inputs
            roman_encode(input_value)

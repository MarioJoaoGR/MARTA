
from string_utils.manipulation import roman_encode  # Importing the function from its module
import pytest
from typing import Union

# Test case for invalid inputs
def test_invalid_inputs():
    with pytest.raises(ValueError):
        assert roman_encode("0")  # Zero is not a valid input
        assert roman_encode(-1)   # Negative numbers are not valid
        assert roman_encode(4000) # Numbers greater than 3999 are not valid
        assert roman_encode("abc")# Non-numeric strings are not valid

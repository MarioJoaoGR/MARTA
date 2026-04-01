
import pytest
from string_utils.manipulation import roman_encode

def test_invalid_input():
    # Test cases for invalid input
    with pytest.raises(ValueError):
        assert roman_encode("abc")  # Invalid Roman numeral string
        assert roman_encode(-1)     # Negative number
        assert roman_encode(0)      # Zero is not a valid Roman numeral
        assert roman_encode(4000)   # Number greater than 3999

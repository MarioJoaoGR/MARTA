
import pytest
from string_utils.manipulation import roman_encode

def test_invalid_integer_out_of_range():
    with pytest.raises(ValueError):
        # Test an integer out of range
        roman_encode(4000)  # Should raise ValueError
        
        # Test a string representation of an integer out of range
        roman_encode('4000')  # Should raise ValueError

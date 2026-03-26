
import pytest
from unittest.mock import patch
from string_utils.manipulation import roman_encode

def test_invalid_string_non_integer():
    with pytest.raises(ValueError):
        # Test with an invalid non-integer string
        roman_encode("abc")

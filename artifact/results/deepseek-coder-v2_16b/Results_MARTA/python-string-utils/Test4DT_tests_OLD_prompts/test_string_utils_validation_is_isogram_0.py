
import pytest
from string_utils.validation import is_isogram

# Test valid isogram input
def test_valid_isogram():
    assert is_isogram('dermatoglyphics') == True

# Test invalid non-isogram input
def test_invalid_non_isogram():
    assert is_isogram('hello') == False

# Test invalid input type (None)

# Test invalid input type (integer)
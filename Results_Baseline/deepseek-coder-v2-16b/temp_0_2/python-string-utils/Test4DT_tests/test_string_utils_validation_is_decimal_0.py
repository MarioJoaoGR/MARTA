
import pytest
from string_utils.validation import is_decimal

# Test cases for the `is_decimal` function
def test_valid_decimal():
    assert is_decimal('42.0') == True
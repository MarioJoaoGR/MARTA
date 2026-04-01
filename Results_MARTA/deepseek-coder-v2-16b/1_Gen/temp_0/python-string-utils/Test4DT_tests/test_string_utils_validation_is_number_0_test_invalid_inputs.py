
import pytest
from string_utils.validation import is_number

def test_invalid_inputs():
    # Test cases where input should be considered invalid
    assert not is_number('1 2 3')  # Contains spaces, which is invalid
    assert not is_number('abc')    # Not a number at all
    assert not is_number('1a2b3c') # Contains alphabetic characters, which is invalid
    assert not is_number('')       # Empty string is not a valid number
    assert not is_number('e5')     # 'e' without preceding digits is invalid
    assert not is_number('.')      # A single dot is not a valid number
    assert not is_number('-')      # A single minus sign is not a valid number
    assert not is_number('+')      # A single plus sign is not a valid number

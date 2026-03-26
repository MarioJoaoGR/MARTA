
import pytest
from string_utils.validation import is_number

def test_invalid_inputs():
    # Test cases with invalid inputs
    assert not is_number('1 2 3')  # Contains spaces
    assert not is_number('abc')    # Not a number
    assert not is_number('1a2b3c') # Contains alphabets
    assert not is_number('')       # Empty string
    assert not is_number(' ')      # Whitespace only

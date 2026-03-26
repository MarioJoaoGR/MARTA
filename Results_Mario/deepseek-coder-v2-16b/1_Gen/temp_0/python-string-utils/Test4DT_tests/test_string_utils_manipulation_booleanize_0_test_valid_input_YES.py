
import pytest
from string_utils.manipulation import booleanize, InvalidInputError

def test_valid_input_YES():
    # Test with a valid input that should return True
    assert booleanize('YES') == True

# Add more tests as needed to cover different scenarios and edge cases


import pytest
from unittest.mock import patch
from string_utils.manipulation import asciify, InvalidInputError
import unicodedata

# Helper function to check if the input is a string
def is_string(input_str):
    return isinstance(input_str, str)

# Test valid ASCII input

# Test non-ASCII input

# Test invalid input type
def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        asciify(12345)  # Should raise InvalidInputError for non-string input
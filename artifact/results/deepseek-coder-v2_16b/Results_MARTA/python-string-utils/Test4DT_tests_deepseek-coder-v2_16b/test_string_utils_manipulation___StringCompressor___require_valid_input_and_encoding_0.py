
import pytest
from string_utils.manipulation import __StringCompressor

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

class InvalidInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Expected "str", received "{type(self.value).__name__}"'

# Test for valid input
def test_valid_input():
    instance = __StringCompressor()
    input_string = 'example'
    encoding = 'utf-8'
    try:
        instance._StringCompressor__require_valid_input_and_encoding(input_string, encoding)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")

# Test for empty string input
def test_empty_string():
    instance = __StringCompressor()
    input_string = ''
    encoding = 'utf-8'
    with pytest.raises(ValueError) as excinfo:
        instance._StringCompressor__require_valid_input_and_encoding(input_string, encoding)
    assert str(excinfo.value) == 'Input string cannot be empty'

# Test for invalid encoding type
def test_invalid_encoding():
    instance = __StringCompressor()
    input_string = 'example'
    encoding = b'utf-8'
    with pytest.raises(ValueError) as excinfo:
        instance._StringCompressor__require_valid_input_and_encoding(input_string, encoding)
    assert str(excinfo.value) == 'Invalid encoding'

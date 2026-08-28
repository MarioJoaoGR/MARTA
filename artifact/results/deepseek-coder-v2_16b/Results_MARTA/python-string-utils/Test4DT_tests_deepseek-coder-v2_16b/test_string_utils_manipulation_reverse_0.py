
import pytest
from string_utils.manipulation import reverse, InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

# Test for valid input string
def test_valid_string():
    input_string = 'hello'
    assert reverse(input_string) == 'olleh', f"Expected 'olleh' but got {reverse(input_string)}"

# Test for None input, which should raise InvalidInputError
def test_none_input():
    input_string = None
    with pytest.raises(InvalidInputError):
        reverse(input_string)

# Test for invalid type (non-string), which should raise InvalidInputError
def test_invalid_type():
    input_string = 12345
    with pytest.raises(InvalidInputError):
        reverse(input_string)

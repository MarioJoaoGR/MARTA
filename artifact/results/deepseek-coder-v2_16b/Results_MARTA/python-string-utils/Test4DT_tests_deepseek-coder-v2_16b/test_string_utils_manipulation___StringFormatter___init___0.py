
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

# Test for valid input
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test for invalid input (non-string type)
def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        __StringFormatter(12345)
    assert str(exc_info.value) == 'Expected "str", received "int"'

# Test for None input (should raise InvalidInputError)
def test_none_input():
    with pytest.raises(InvalidInputError) as exc_info:
        __StringFormatter(None)
    assert str(exc_info.value) == 'Expected "str", received "NoneType"'

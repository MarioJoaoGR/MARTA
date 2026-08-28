
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

# Test for initialization with a valid string
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test for initialization with an invalid type (should raise InvalidInputError)
def test_invalid_type():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

# Test for initialization with None (should raise InvalidInputError)
def test_none_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

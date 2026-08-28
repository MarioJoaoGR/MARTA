
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

# Test for valid initialization with a string
def test_valid_initialization():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test for invalid initialization with None
def test_invalid_initialization_with_none():
    try:
        formatter = __StringFormatter(None)
    except InvalidInputError as e:
        assert str(e) == "Expected \"str\", received \"NoneType\""

# Test for invalid initialization with an integer
def test_invalid_initialization_with_integer():
    try:
        formatter = __StringFormatter(12345)
    except InvalidInputError as e:
        assert str(e) == "Expected \"str\", received \"int\""

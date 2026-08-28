
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Test valid initialization with a string
def test_valid_initialization():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test invalid initialization with an integer
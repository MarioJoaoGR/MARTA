
import pytest
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Test initialization with a valid string
def test_valid_initialization():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test initialization with an invalid type (should raise InvalidInputError)

# Test the format method to ensure it capitalizes the first character of each word
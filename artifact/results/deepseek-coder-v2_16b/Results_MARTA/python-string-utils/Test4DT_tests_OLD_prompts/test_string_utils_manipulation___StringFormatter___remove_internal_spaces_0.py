
import pytest
from unittest.mock import patch
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Test initialization with a valid string
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test initialization with an invalid input type (should raise InvalidInputError)

# Test initialization with an invalid input type (mocked)
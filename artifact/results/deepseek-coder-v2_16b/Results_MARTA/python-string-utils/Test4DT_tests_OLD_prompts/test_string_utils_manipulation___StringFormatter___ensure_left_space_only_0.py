
import pytest
from unittest.mock import patch
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Test initialization with valid input string
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test initialization with invalid input (not a string)
def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

# Test ensure_left_space_only method
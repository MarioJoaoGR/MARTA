
import pytest
from unittest.mock import patch, MagicMock
from string_utils.manipulation import __StringFormatter
from string_utils.errors import InvalidInputError

# Test initialization with valid input
def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"

# Test initialization with None input

# Test initialization with invalid input type (int)
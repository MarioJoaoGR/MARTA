
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError
from unittest.mock import patch

# Test initialization with valid string
def test_valid_string_initialization():
    formatter = __StringFormatter("valid input")
    assert formatter.input_string == "valid input"

# Test initialization with invalid input (should raise InvalidInputError)

# Test initialization with valid string mocked
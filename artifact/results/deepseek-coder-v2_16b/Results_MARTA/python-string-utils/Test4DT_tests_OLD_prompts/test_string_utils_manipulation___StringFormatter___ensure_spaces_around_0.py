
import pytest
from unittest.mock import patch
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Test initialization with a valid string
def test_valid_string_initialization():
    formatter = __StringFormatter('This is a test string.')
    assert formatter.input_string == 'This is a test string.'

# Test initialization with an invalid type, expecting InvalidInputError
def test_invalid_type_initialization():
    try:
        __StringFormatter(12345)
    except InvalidInputError as e:
        assert str(e) == 'Expected "str", received "int"'

# Test the error message for invalid input type
def test_invalid_input_error_message():
    try:
        __StringFormatter('valid string')
    except InvalidInputError as e:
        assert str(e) == 'Expected "str", received "NoneType"'

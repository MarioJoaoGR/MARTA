
import pytest
from unittest.mock import patch, MagicMock
from string_utils.manipulation import __StringFormatter, InvalidInputError
from uuid import uuid4

# Test for valid input initialization
def test_valid_input():
    with patch('string_utils.manipulation.__StringFormatter', return_value=MagicMock()):
        formatter = __StringFormatter("hello world")
        assert formatter.input_string == "hello world"

# Test for invalid input type raises InvalidInputError
def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

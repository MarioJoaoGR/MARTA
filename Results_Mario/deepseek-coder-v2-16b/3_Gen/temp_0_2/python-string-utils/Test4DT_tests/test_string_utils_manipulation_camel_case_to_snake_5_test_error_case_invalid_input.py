
import re
import pytest
from string_utils.manipulation import camel_case_to_snake, is_string, is_camel_case, InvalidInputError

# Mocking the necessary functions and constants if needed
class MockInvalidInputError(Exception):
    pass

def test_error_case_invalid_input():
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(12345)  # Invalid input type (int)

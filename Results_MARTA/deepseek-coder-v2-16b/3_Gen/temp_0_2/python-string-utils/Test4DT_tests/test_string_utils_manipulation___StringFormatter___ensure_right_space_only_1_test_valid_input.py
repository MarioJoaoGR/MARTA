
import re
from unittest.mock import patch
from string_utils.manipulation import InvalidInputError, is_string

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
        self.input_string = input_string + ' '  # Ensure the string ends with a space

    def format_string(self):
        return self.input_string

def test_valid_input():
    with patch('string_utils.manipulation.is_string', return_value=True):
        formatter = __StringFormatter("Hello World")
        assert formatter.format_string() == "Hello World "

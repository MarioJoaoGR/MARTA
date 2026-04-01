
import re
from string_utils.manipulation import is_string

class InvalidInputError(Exception):
    def __init__(self, received_type):
        self.message = f"Expected 'str', received '{received_type.__name__}'"
        super().__init__(self.message)

class __StringFormatter:
    """
    A class for formatting input strings by ensuring spaces around specified substrings.

    Parameters:
        input_string (str): The string to be formatted. Must be a valid Python string.

    Raises:
        InvalidInputError: If the provided `input_string` is not a valid string.
    """
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(type(input_string))

        self.input_string = input_string

    def __ensure_spaces_around(self, regex_match):
        return ' ' + regex_match.group(1).strip() + ' '

def test_valid_input():
    formatter = __StringFormatter("Hello World")
    assert formatter.input_string == "Hello World"

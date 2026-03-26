
import pytest
from string_utils.manipulation import is_string, InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(f"Expected a string but got {type(input_string).__name__}")
        self.input_string = input_string

def test_valid_input():
    input_string = "Hello, World!"
    formatter = __StringFormatter(input_string)
    assert formatter.input_string == input_string

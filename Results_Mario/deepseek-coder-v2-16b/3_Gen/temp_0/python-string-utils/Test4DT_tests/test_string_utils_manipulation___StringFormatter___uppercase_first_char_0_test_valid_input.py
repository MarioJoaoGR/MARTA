
import pytest
from string_utils.manipulation import is_string, InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(f"Expected 'str', received '{type(input_string).__name__}'")
        self.input_string = input_string

    def format(self):
        return ' '.join(word.capitalize() for word in self.input_string.split())

def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"
    assert formatter.format() == "Hello World"

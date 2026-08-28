
import pytest
from string_utils.manipulation import __StringFormatter

class InvalidInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Expected "str", received "{type(self.value).__name__}"'

def test_valid_input():
    formatter = __StringFormatter("hello world")
    assert formatter.input_string == "hello world"


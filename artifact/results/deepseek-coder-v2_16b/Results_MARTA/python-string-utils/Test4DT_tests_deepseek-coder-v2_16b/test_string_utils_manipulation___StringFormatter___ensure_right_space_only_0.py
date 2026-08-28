
import pytest
from string_utils.manipulation import __StringFormatter

def is_string(obj):
    return isinstance(obj, str)

class InvalidInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Expected "str", received "{type(self.value).__name__}"'

# Test for valid input initialization
def test_valid_input():
    formatter = __StringFormatter("valid input")
    assert isinstance(formatter.input_string, str)
    assert formatter.input_string == "valid input"

# Test for invalid input raises InvalidInputError
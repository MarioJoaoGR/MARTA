
import pytest
from string_utils.manipulation import camel_case_to_snake

def is_string(obj):
    return isinstance(obj, str)

def is_camel_case(input_string):
    return re.match(r'^[a-z]+([A-Z][a-z]*)*$', input_string) is not None

class InvalidInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Expected "str", received "{type(self.value).__name__}"'

# Test for camel_case_to_snake function with default separator
def test_camel_case_to_snake_default_separator():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'

# Test for camel_case_to_snake function with custom separator
def test_camel_case_to_snake_custom_separator():
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'

# Test for invalid input to camel_case_to_snake function

# Test for non-camel case input to camel_case_to_snake function
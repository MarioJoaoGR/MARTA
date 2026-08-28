
import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

def is_camel_case(s):
    if not isinstance(s, str):
        return False
    return s != s.lower() and s != s.upper() and '_' not in s

# Test for valid input with default separator
def test_valid_input_default_separator():
    result = camel_case_to_snake('ThisIsACamelStringTest')
    assert result == 'this_is_a_camel_string_test', f"Expected 'this_is_a_camel_string_test' but got {result}"

# Test for valid input with custom separator
def test_valid_input_custom_separator():
    result = camel_case_to_snake('ThisIsACamelStringTest', separator='-')
    assert result == 'this-is-a-camel-string-test', f"Expected 'this-is-a-camel-string-test' but got {result}"

# Test for invalid input (None)
def test_invalid_input_none():
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(None)

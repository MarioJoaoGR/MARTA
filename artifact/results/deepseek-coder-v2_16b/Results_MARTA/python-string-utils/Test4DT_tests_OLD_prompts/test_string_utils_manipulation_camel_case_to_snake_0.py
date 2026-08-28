
import pytest
from unittest.mock import patch
from string_utils.manipulation import camel_case_to_snake, is_camel_case

# Helper function to check if the input is a string
def is_string(input_str):
    return isinstance(input_str, str)

# Test for valid camel case conversion
@patch('string_utils.manipulation.is_camel_case', return_value=True)
def test_valid_camel_case_conversion(mock_is_camel_case):
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'

# Test for invalid input (non-string)

# Test for non-camel case input
@patch('string_utils.manipulation.is_camel_case', return_value=False)
def test_non_camel_case_input(mock_is_camel_case):
    assert camel_case_to_snake('thisIsNotACamelString') == 'thisIsNotACamelString'

# Test for custom separator
@patch('string_utils.manipulation.is_camel_case', return_value=True)
def test_custom_separator(mock_is_camel_case):
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'
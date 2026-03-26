
import pytest
from string_utils.manipulation import camel_case_to_snake
from string_utils.errors import InvalidInputError

def test_camel_case_to_snake():
    # Test a valid camel case string
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    
    # Test with custom separator
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'
    
    # Test an already snake case string (should return the original)
    assert camel_case_to_snake('this_is_a_snake_case_string') == 'this_is_a_snake_case_string'
    
    # Test a non-camel case string with letters and numbers (should return the original)
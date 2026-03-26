
import re
import pytest
from string_utils.manipulation import camel_case_to_snake, is_string, is_camel_case
from string_utils.errors import InvalidInputError

def test_valid_input():
    # Test a valid camel case input
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    
    # Additional tests with different separators
    assert camel_case_to_snake('AnotherCamelCaseExample', separator='-') == 'another-camel-case-example'
    assert camel_case_to_snake('YetAnotherCamelCaseTest', separator='.') == 'yet.another.camel.case.test'

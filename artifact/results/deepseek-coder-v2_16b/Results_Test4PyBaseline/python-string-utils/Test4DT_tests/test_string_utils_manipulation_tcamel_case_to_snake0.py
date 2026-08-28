
import pytest
from string_utils.manipulation import camel_case_to_snake

# Test cases for camel_case_to_snake function
def test_camel_case_to_snake_basic():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'

def test_camel_case_to_snake_custom_separator():
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'

def test_camel_case_to_snake_non_camel_case():
    assert camel_case_to_snake('ThisIsNotACamelString') == 'this_is_not_a_camel_string'

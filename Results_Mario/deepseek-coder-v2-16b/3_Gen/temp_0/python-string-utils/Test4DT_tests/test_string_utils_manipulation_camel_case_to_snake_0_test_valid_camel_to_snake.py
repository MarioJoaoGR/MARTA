
import pytest
from string_utils.manipulation import camel_case_to_snake, is_camel_case

def test_valid_camel_to_snake():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'


import re
import pytest
from string_utils.manipulation import camel_case_to_snake

def test_valid_case_standard_input():
    # Test a valid camel case string
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'

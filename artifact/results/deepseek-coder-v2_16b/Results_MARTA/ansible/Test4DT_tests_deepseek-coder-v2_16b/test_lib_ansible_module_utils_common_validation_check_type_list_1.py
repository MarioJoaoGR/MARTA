
import pytest
from ansible.module_utils.common.validation import check_type_list

def test_valid_input_list():
    value = [1, 2, 3]
    assert check_type_list(value) == value

def test_valid_input_comma_separated_string():
    value = "4,5,6"
    assert check_type_list(value) == ["4", "5", "6"]

def test_valid_input_integer():
    value = 123
    assert check_type_list(value) == ["123"]

def test_valid_input_float():
    value = 123.0
    assert check_type_list(value) == ["123.0"]

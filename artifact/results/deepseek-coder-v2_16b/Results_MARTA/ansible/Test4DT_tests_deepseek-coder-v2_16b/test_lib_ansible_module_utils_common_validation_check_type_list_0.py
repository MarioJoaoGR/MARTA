
import pytest
from ansible.module_utils.common.validation import check_type_list

def test_valid_input_list():
    assert check_type_list([1, 2, 3]) == [1, 2, 3]

def test_valid_input_comma_separated_string():
    assert check_type_list("4,5,6") == ['4', '5', '6']

def test_valid_input_integer():
    assert check_type_list(123) == ['123']

def test_valid_input_float():
    assert check_type_list(123.0) == ['123.0']

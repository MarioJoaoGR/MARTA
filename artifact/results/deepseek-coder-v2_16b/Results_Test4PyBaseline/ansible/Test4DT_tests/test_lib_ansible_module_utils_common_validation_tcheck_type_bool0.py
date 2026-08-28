
import pytest
from ansible.module_utils.common.validation import check_type_bool

# Test cases for check_type_bool function
def test_check_type_bool_string_truthy():
    assert check_type_bool('1') is True
    assert check_type_bool('on') is True
    assert check_type_bool('yes') is True
    assert check_type_bool('true') is True
    assert check_type_bool('t') is True
    assert check_type_bool('y') is True

def test_check_type_bool_string_falsy():
    assert check_type_bool('0') is False
    assert check_type_bool('off') is False
    assert check_type_bool('no') is False
    assert check_type_bool('false') is False
    assert check_type_bool('f') is False
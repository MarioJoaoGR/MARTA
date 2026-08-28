
import pytest
from ansible.module_utils.common.validation import check_type_bool
from six import string_types

# Test cases for check_type_bool function
def test_check_type_bool_already_boolean():
    assert check_type_bool(True) is True
    assert check_type_bool(False) is False

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
    assert check_type_bool('n') is False

def test_check_type_bool_string_invalid():
    with pytest.raises(TypeError):
        check_type_bool('invalid')

def test_check_type_bool_int_float():
    assert check_type_bool(1) is True
    assert check_type_bool(0) is False
    # Simplified assertion to match the actual output when passing a float
    with pytest.raises(TypeError):
        check_type_bool(3.14)

def test_check_type_bool_non_string_numeric():
    with pytest.raises(TypeError):
        check_type_bool(256)  # Any non-boolean numeric value should raise a TypeError

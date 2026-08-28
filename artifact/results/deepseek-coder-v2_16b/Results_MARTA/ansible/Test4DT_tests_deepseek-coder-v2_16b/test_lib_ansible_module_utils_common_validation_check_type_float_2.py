
import pytest
from ansible.module_utils.common.validation import check_type_float



def test_integer():
    value = 123
    result = check_type_float(value)
    assert isinstance(result, float), f"Expected {value} to be converted to float but got {result}"

def test_string_number():
    value = '123'
    result = check_type_float(value)
    assert isinstance(result, float), f"Expected '{value}' to be converted to float but got {result}"

def test_bytes_number():
    value = b'123'
    result = check_type_float(value)
    assert isinstance(result, float), f"Expected '{value}' to be converted to float but got {result}"

import pytest
from ansible.module_utils.common.validation import check_type_float

def test_valid_float():
    value = 3.14
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float type"
    assert result == 3.14, "Expected the same float value"

def test_valid_int():
    value = 123
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float type"
    assert result == 123.0, "Expected int to be converted to float"

def test_valid_str():
    value = '123'
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float type"
    assert result == 123.0, "Expected string representation of number to be converted to float"

def test_valid_bytes():
    value = b'123'
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float type"
    assert result == 123.0, "Expected bytes representation of number to be converted to float"

def test_invalid_str():
    value = 'abc'
    with pytest.raises(TypeError) as excinfo:
        check_type_float(value)
    assert str(excinfo.value) == "<class 'str'> cannot be converted to a float", "Expected TypeError message for invalid string input"

def test_none_input():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_float(value)
    assert str(excinfo.value) == "<class 'NoneType'> cannot be converted to a float", "Expected TypeError message for None input"

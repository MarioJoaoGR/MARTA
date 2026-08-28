
import pytest
from ansible.module_utils.common.validation import check_type_float

def test_check_type_float_with_float():
    value = 3.14
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float"
    assert result == 3.14, "Expected the same float value"

def test_check_type_float_with_int():
    value = 123
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float after conversion from int"
    assert result == 123.0, "Expected the same float value after conversion"

def test_check_type_float_with_str():
    value = '123'
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float after conversion from str"
    assert result == 123.0, "Expected the same float value after conversion"

def test_check_type_float_with_bytes():
    value = b'123'
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float after conversion from bytes"
    assert result == 123.0, "Expected the same float value after conversion"

def test_check_type_float_with_invalid_str():
    value = 'abc'
    with pytest.raises(TypeError) as excinfo:
        check_type_float(value)
    assert str(excinfo.value) == "<class 'str'> cannot be converted to a float"

def test_check_type_float_with_none():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_float(value)
    assert str(excinfo.value) == "<class 'NoneType'> cannot be converted to a float"

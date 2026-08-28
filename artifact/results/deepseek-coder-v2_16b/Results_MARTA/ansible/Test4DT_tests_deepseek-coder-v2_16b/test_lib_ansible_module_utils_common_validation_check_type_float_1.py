
import pytest
from ansible.module_utils.common.validation import check_type_float

def test_valid_float():
    value = 3.14
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float"
    assert result == 3.14, "Expected the same float value"

def test_valid_integer():
    value = 123
    result = check_type_float(value)
    assert isinstance(result, float), "Expected a float after conversion from integer"
    assert result == 123.0, "Expected the same float value after conversion"

def test_invalid_string():
    value = 'abc'
    with pytest.raises(TypeError):
        check_type_float(value)

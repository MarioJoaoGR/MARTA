
import pytest
from ansible.module_utils.common.validation import check_type_str
from six import string_types

# Test cases for check_type_str function

def test_check_type_str_with_string():
    value = "Hello, World!"
    result = check_type_str(value)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == "Hello, World!", f"Expected 'Hello, World!' but got {result}"

def test_check_type_str_with_non_string():
    value = 12345
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False)
    assert str(excinfo.value) == "'12345' is not a string and conversion is not allowed"

def test_check_type_str_with_non_string_and_allow_conversion():
    value = 12345
    result = check_type_str(value, allow_conversion=True)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == "12345", f"Expected '12345' but got {result}"

def test_check_type_str_with_none():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False)
    assert str(excinfo.value) == "'None' is not a string and conversion is not allowed"

def test_check_type_str_with_none_and_allow_conversion():
    value = None
    result = check_type_str(value, allow_conversion=True)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == "None", f"Expected 'None' but got {result}"

def test_check_type_str_with_param():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False, param="value")
    assert str(excinfo.value) == "'None' is not a string and conversion is not allowed"

def test_check_type_str_with_custom_prefix():
    value = 12345
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False, prefix="Custom prefix: ")
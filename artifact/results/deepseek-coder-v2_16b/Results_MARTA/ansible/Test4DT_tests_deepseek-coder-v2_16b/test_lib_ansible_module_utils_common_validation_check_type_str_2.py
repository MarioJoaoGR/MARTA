
import pytest
from ansible.module_utils.common.validation import check_type_str

# Test valid input string
def test_valid_input_string():
    value = 'Hello, World!'
    result = check_type_str(value)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == 'Hello, World!', "Expected the same string to be returned"

# Test invalid input None
def test_invalid_input_none():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False)
    assert str(excinfo.value) == "'None' is not a string and conversion is not allowed"

# Test invalid input list
def test_invalid_input_list():
    value = []
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False)
    assert str(excinfo.value) == "'[]' is not a string and conversion is not allowed"

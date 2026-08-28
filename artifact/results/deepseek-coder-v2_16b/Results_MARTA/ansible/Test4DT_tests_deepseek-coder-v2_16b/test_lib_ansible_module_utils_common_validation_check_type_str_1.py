
import pytest
from ansible.module_utils.common.validation import check_type_str

# Test valid input where value is a string
def test_valid_input():
    value = 'Hello, World!'
    result = check_type_str(value)
    assert isinstance(result, str), f"Expected {type('Hello, World!')} but got {type(result)}"
    assert result == 'Hello, World!', f"Expected 'Hello, World!' but got '{result}'"

# Test handling of None input without conversion allowed
def test_none_input():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False)
    assert str(excinfo.value) == "'None' is not a string and conversion is not allowed"

# Test invalid input where allow_conversion is False
def test_invalid_input():
    value = 12345
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False)
    assert str(excinfo.value) == "'12345' is not a string and conversion is not allowed"

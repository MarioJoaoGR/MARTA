
import pytest
from ansible.module_utils.common.validation import check_type_str

def test_valid_string():
    value = "Hello, World!"
    result = check_type_str(value)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == "Hello, World!", f"Expected 'Hello, World!' but got '{result}'"

def test_invalid_input():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_str(value, allow_conversion=False)
    assert str(excinfo.value) == "'None' is not a string and conversion is not allowed"

def test_allow_conversion():
    value = 12345
    result = check_type_str(value, allow_conversion=True)
    assert isinstance(result, str), f"Expected a string but got {type(result)}"
    assert result == "12345", f"Expected '12345' but got '{result}'"

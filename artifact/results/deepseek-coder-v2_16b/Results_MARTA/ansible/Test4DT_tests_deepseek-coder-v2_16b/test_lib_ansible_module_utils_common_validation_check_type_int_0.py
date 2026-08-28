
import pytest
from ansible.module_utils.common.validation import check_type_int

# Test valid integer input
def test_valid_int():
    value = 123
    assert check_type_int(value) == 123

# Test conversion from string to integer
def test_valid_str_to_int():
    value = '456'
    assert check_type_int(value) == 456

# Test error handling for invalid string that cannot be converted to integer
def test_invalid_str_to_int():
    value = 'abc'
    with pytest.raises(TypeError):
        check_type_int(value)

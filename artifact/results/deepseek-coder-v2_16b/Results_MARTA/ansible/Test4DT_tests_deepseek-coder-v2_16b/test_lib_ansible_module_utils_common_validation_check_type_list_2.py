
import pytest
from ansible.module_utils.common.validation import check_type_list

# Test valid input - list
def test_valid_input_list():
    value = [1, 2, 3]
    assert check_type_list(value) == [1, 2, 3]

# Test valid input - comma-separated string
def test_valid_input_comma_separated_string():
    value = '4,5,6'
    assert check_type_list(value) == ['4', '5', '6']

# Test valid input - integer
def test_valid_input_integer():
    value = 123
    assert check_type_list(value) == ['123']

# Test valid input - float
def test_valid_input_float():
    value = 123.0
    assert check_type_list(value) == ['123.0']

# Test invalid input - string that cannot be converted to list
def test_invalid_input_string():
    value = 'hello world'
    with pytest.raises(TypeError):
        check_type_list(value)

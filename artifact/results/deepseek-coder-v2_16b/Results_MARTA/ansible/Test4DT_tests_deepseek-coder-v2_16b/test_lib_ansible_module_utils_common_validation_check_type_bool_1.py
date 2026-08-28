
import pytest
from ansible.module_utils.common.validation import check_type_bool

# Test valid input 'true'
def test_valid_input_true():
    result = check_type_bool('true')
    assert isinstance(result, bool) and result is True

# Test valid input 1
def test_valid_input_1():
    result = check_type_bool(1)
    assert isinstance(result, bool) and result is True

# Test valid input '0'
def test_valid_input_false():
    result = check_type_bool('0')
    assert isinstance(result, bool) and result is False

# Test valid input 'yes'
def test_valid_input_yes():
    result = check_type_bool('yes')
    assert isinstance(result, bool) and result is True

# Test invalid input that cannot be converted to bool
def test_invalid_input():
    with pytest.raises(TypeError):
        check_type_bool('invalid')

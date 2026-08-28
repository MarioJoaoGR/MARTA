
import pytest
from ansible.module_utils.common.validation import check_type_int

def test_valid_integer():
    value = 123
    assert check_type_int(value) == 123

def test_valid_string_to_int():
    value = '456'
    assert check_type_int(value) == int(value)

def test_invalid_type():
    value = None
    with pytest.raises(TypeError):
        check_type_int(value)

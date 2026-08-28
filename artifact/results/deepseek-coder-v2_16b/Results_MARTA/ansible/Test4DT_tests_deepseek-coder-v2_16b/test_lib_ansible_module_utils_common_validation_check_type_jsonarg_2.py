
import pytest
from ansible.module_utils.common.validation import check_type_jsonarg

def test_valid_string():
    value = "   some text with spaces   "
    result = check_type_jsonarg(value)
    assert result == 'some text with spaces'

def test_invalid_type():
    value = 12345
    with pytest.raises(TypeError):
        check_type_jsonarg(value)

def test_none_input():
    value = None
    with pytest.raises(TypeError):
        check_type_jsonarg(value)

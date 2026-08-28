
import pytest
from ansible.module_utils.common.validation import check_type_bool

def test_valid_inputs():
    value = 'true'
    result = check_type_bool(value)
    assert isinstance(result, bool), f"Expected a boolean type but got {type(result)} for input '{value}'"
    assert result is True, f"Expected True for input '{value}' but got {result}"

def test_none_case():
    value = None
    with pytest.raises(TypeError) as excinfo:
        check_type_bool(value)
    assert str(excinfo.value) == "'NoneType' cannot be converted to a bool"

def test_invalid_input():
    value = 'invalid'
    with pytest.raises(TypeError) as excinfo:
        check_type_bool(value)
    assert str(excinfo.value) == "'<class 'str'> cannot be converted to a bool'"

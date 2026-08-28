
import pytest
from ansible.module_utils.common.validation import check_type_bool

def test_valid_inputs():
    value = 'true'
    result = check_type_bool(value)
    assert isinstance(result, bool), f"Expected bool but got {type(result)}"
    assert result is True, "Expected True for valid input 'true'"

def test_edge_cases():
    value = None
    with pytest.raises(TypeError):
        check_type_bool(value)
    
    value = []
    with pytest.raises(TypeError):
        check_type_bool(value)

def test_invalid_inputs():
    value = 'invalid'
    with pytest.raises(TypeError):
        check_type_bool(value)

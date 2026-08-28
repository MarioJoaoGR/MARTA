
import pytest
from ansible.module_utils.common.parameters import _list_no_log_values

# Test valid inputs
def test_valid_inputs():
    arg_spec = {
        'username': {'type': 'str', 'no_log': True},
        'password': {'options': {'secret': {'type': 'str', 'no_log': True}}}
    }
    params = {'username': 'admin', 'password': {'secret': 'supersecret'}}
    
    no_log_values = _list_no_log_values(arg_spec, params)
    assert set(no_log_values) == {'admin', 'supersecret'}

# Test edge cases
def test_edge_cases():
    arg_spec = {
        'database': {'type': 'dict', 'options': {
            'host': {'type': 'str'},
            'port': {'type': 'int'},
            'username': {'type': 'str', 'no_log': True},
            'password': {'type': 'str', 'no_log': True}
        }}
    }
    params = None
    
    no_log_values = _list_no_log_values(arg_spec, params)
    assert set(no_log_values) == set()

# Test invalid inputs
def test_invalid_inputs():
    arg_spec = {
        'username': {'type': 'str', 'no_log': True},
        'password': {'options': {'secret': {'type': 'int', 'no_log': True}}}
    }
    params = {'username': 'admin', 'password': {'secret': 'supersecret'}}
    
    with pytest.raises(TypeError):
        _list_no_log_values(arg_spec, params)


import pytest
from ansible.module_utils.common.parameters import _list_no_log_values

# Test cases for _list_no_log_values function
def test_list_no_log_values():
    # Test case 1: Basic no_log parameter in argument_spec
    argument_spec = {'param1': {'no_log': True}}
    params = {'param1': "sensitive data"}
    result = _list_no_log_values(argument_spec, params)
    assert set(result) == {"sensitive data"}

    # Test case 2: no_log parameter in nested dictionary within argument_spec
    argument_spec = {'param1': {}, 'param2': {'options': {'subparam': {'no_log': True}}}}
    params = {'param1': "data", 'param2': {'subparam': 'secret'}}
    result = _list_no_log_values(argument_spec, params)
    assert set(result) == {"secret"}

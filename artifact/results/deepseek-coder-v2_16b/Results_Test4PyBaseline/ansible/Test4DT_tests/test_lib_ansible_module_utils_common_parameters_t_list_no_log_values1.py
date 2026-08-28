
import pytest
from ansible.module_utils.common.parameters import _list_no_log_values

# Test case 3: No no_log parameter in argument_spec
def test_no_no_log_parameter():
    argument_spec = {'param1': {}}
    params = {'param1': "data"}
    result = _list_no_log_values(argument_spec, params)
    assert set(result) == set()

# Test case 4: no_log parameter in nested list within argument_spec
def test_no_log_in_nested_list():
    argument_spec = {'param1': {}, 'param2': {'options': {'subparam': []}}}
    params = {'param1': "data", 'param2': {'subparam': ['secret', 'more_secret']}}
    result = _list_no_log_values(argument_spec, params)
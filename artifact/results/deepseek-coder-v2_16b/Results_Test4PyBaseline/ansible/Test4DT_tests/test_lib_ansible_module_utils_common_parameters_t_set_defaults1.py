
import pytest
from ansible.module_utils.common.parameters import _set_defaults

# Test cases for _set_defaults function
def test_set_defaults_with_no_log():
    argument_spec = {'param1': {'default': 1, 'no_log': False}, 'param2': {'default': None, 'no_log': True}}
    parameters = {}
    returned_values = _set_defaults(argument_spec, parameters)
    assert parameters == {'param1': 1, 'param2': None}

import pytest
from ansible.module_utils.common.parameters import _list_deprecations

# Test cases for _list_deprecations function
def test_no_deprecated_parameters():
    argument_spec = {
        'param1': {'options': {}},
        'param2': {'options': {}}
    }
    parameters = {'param1': {}, 'param2': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 0

def test_deprecated_parameter_with_date():
    argument_spec = {
        'param1': {'removed_at_date': '2023-01-01', 'options': {}}
    }
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1
    assert deprecations[0]['msg'] == "Param 'param1' is deprecated. See the module docs for more information"
    assert deprecations[0]['date'] == '2023-01-01'

def test_deprecated_parameter_with_version():
    argument_spec = {
        'param1': {'removed_in_version': '2.8', 'options': {}}
    }
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1
    assert deprecations[0]['msg'] == "Param 'param1' is deprecated. See the module docs for more information"
    assert deprecations[0]['version'] == '2.8'

def test_nested_deprecated_parameter():
    argument_spec = {
        'param1': {'options': {
            'subparam1': {'removed_in_version': '2.9', 'options': {}}
        }}
    }
    parameters = {'param1': {'subparam1': {}}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1
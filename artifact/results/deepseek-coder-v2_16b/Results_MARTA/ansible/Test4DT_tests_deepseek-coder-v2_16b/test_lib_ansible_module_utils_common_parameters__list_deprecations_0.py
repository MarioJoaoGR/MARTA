
import pytest
from ansible.module_utils.common.parameters import _list_deprecations


def test_valid_inputs():
    argument_spec = {
        'deptest': {'removed_in_version': '2.9'},
    }
    parameters = {
        'deptest': True,
    }
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1
    assert 'msg' in deprecations[0]
    assert 'version' in deprecations[0]
    assert deprecations[0]['msg'] == "Param 'deptest' is deprecated. See the module docs for more information"
    assert deprecations[0]['version'] == '2.9'

def test_nested_inputs():
    argument_spec = {
        'subtest': {'options': {'nested_arg': {'removed_in_version': '3.0'}}},
    }
    parameters = {}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 0

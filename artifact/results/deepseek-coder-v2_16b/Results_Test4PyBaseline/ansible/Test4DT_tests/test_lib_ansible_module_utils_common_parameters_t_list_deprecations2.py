
import pytest
from ansible.module_utils.common.parameters import _list_deprecations

# Test case for line 266: deprecations = []
def test_initialization_of_deprecations():
    argument_spec = {'param1': {}}
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 0

# Test case for line 267: for arg_name, arg_opts in argument_spec.items():
def test_loop_through_argument_spec():
    argument_spec = {'param1': {'removed_in_version': '2.8', 'options': {}}}
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1

# Test case for line 268: if arg_name in parameters:
def test_check_if_parameter_exists():
    argument_spec = {'param1': {}}
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 0

# Test case for line 269: if prefix:
def test_handle_prefix():
    argument_spec = {'param1': {'options': {}}}
    parameters = {'param1': {'subparam1': {}}}
    deprecations = _list_deprecations(argument_spec, parameters, prefix='param1')
    assert len(deprecations) == 0

# Test case for line 270: sub_prefix = '%s["%s"]' % (prefix, arg_name)
def test_format_sub_prefix():
    argument_spec = {'param1': {'options': {}}}
    parameters = {'param1': {'subparam1': {}}}
    deprecations = _list_deprecations(argument_spec, parameters, prefix='param1')
    assert len(deprecations) == 0

# Test case for line 272: sub_prefix = arg_name
def test_no_prefix():
    argument_spec = {'param1': {'options': {}}}
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 0

# Test case for line 273: if arg_opts.get('removed_at_date') is not None:
def test_deprecated_by_date():
    argument_spec = {'param1': {'removed_at_date': '2023-01-01', 'options': {}}}
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1
    assert deprecations[0]['msg'] == "Param 'param1' is deprecated. See the module docs for more information"
    assert deprecations[0]['date'] == '2023-01-01'

# Test case for line 279: elif arg_opts.get('removed_in_version') is not None:
def test_deprecated_by_version():
    argument_spec = {'param1': {'removed_in_version': '2.8', 'options': {}}}
    parameters = {'param1': {}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1
    assert deprecations[0]['msg'] == "Param 'param1' is deprecated. See the module docs for more information"
    assert deprecations[0]['version'] == '2.8'

# Test case for line 286: sub_argument_spec = arg_opts.get('options')
def test_check_sub_argument_spec():
    argument_spec = {'param1': {'options': {
        'subparam1': {'removed_in_version': '2.9', 'options': {}}}
    }}
    parameters = {'param1': {'subparam1': {}}}
    deprecations = _list_deprecations(argument_spec, parameters)
    assert len(deprecations) == 1
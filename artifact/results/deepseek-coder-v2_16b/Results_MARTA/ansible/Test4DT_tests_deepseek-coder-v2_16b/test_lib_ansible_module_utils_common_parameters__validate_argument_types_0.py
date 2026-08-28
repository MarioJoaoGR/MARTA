
import pytest
from ansible.module_utils.common.parameters import _validate_argument_types, ArgumentTypeError
from ansible.errors import AnsibleValidationErrorMultiple

# Test valid input happy path
def test_valid_input_happy_path():
    argument_spec = {'param1': {'type': 'int'}, 'param2': {'type': 'str'}}
    parameters = {'param1': 1, 'param2': 'string'}
    validated_params, errors = _validate_argument_types(argument_spec, parameters)
    assert 'param1' in validated_params
    assert validated_params['param1'] == 1
    assert 'param2' in validated_params
    assert validated_params['param2'] == 'string'
    assert not errors.messages()

# Test edge case with None values
def test_edge_case_none_values():
    argument_spec = {'param1': {'type': 'int'}, 'param2': {'type': 'str'}}
    parameters = {'param1': None, 'param2': 'string'}
    validated_params, errors = _validate_argument_types(argument_spec, parameters)
    assert 'param1' not in validated_params
    assert 'param2' in validated_params
    assert validated_params['param2'] == 'string'
    assert len(errors.messages()) == 1
    assert "Invalid type <class 'NoneType'> for option 'param1'" in errors.messages()[0]

# Test invalid input causing errors
def test_invalid_input_error_handling():
    argument_spec = {'param1': {'type': 'list', 'elements': 'int'}}
    parameters = {'param1': [1, 'string', 3.14]}
    validated_params, errors = _validate_argument_types(argument_spec, parameters)
    assert not validated_params
    assert len(errors.messages()) == 1
    assert "Invalid type <class 'str'> for option 'param1'" in errors.messages()[0]

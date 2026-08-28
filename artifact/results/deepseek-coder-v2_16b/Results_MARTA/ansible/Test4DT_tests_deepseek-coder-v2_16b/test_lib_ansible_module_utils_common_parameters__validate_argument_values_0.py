
import pytest
from ansible.module_utils.common.parameters import _validate_argument_values, AnsibleValidationErrorMultiple, ArgumentValueError, ArgumentTypeError

def test_valid_parameter():
    argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'val1', 'param2': 5}
    errors = AnsibleValidationErrorMultiple()
    
    _validate_argument_values(argument_spec, parameters, errors=errors)
    
    assert not errors.messages, f"Errors encountered: {errors.messages}"


def test_invalid_choice():
    argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
    parameters = {'param1': 'val3', 'param2': 5}
    errors = AnsibleValidationErrorMultiple()
    
    _validate_argument_values(argument_spec, parameters, errors=errors)
    
    assert len(errors.messages) == 1, f"Expected one error, but got: {len(errors.messages)}"
    assert "value of param1 must be one of: val1, val2" in errors.messages[0]
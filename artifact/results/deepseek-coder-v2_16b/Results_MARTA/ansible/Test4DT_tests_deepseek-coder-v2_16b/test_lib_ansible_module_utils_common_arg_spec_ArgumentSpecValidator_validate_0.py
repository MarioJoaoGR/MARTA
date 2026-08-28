
import pytest
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

# Test valid inputs scenario
def test_valid_inputs():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int', 'aliases': ['p2']},
        'param3': {'type': 'float'}
    }
    
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {
        'param1': 'value1',
        'param2': 42,
        'param3': 3.14
    }
    
    result = validator.validate(parameters)
    
    assert not result.errors, f"Validation failed with errors: {result.errors}"
    assert result.validated_parameters == parameters, "Validated parameters do not match expected values."

# Test edge cases scenario
def test_edge_cases():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int', 'aliases': ['p2']},
        'param3': {'type': 'float'}
    }
    
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {
        'param1': None,
        'param2': '',
        'param3': 0.0
    }
    
    result = validator.validate(parameters)
    
    assert not result.errors, f"Validation failed with errors: {result.errors}"
    assert result.validated_parameters == {'param1': None, 'param2': '', 'param3': 0.0}, "Validated parameters do not match expected values."

# Test invalid inputs scenario
def test_invalid_inputs():
    argument_spec = {
        'param1': {'type': 'str'},
        'param2': {'type': 'int', 'aliases': ['p2']},
        'param3': {'type': 'float'}
    }
    
    validator = ArgumentSpecValidator(argument_spec, mutually_exclusive=['param1', 'param2'])
    parameters = {
        'param1': 'value1',
        'param2': 42,
        'param3': 3.14
    }
    
    result = validator.validate(parameters)
    
    assert len(result.errors) == 1, "Expected one error for mutually exclusive parameters."
    assert "mutually_exclusive" in result.errors[0].message, f"Error message does not indicate mutual exclusivity: {result.errors}"

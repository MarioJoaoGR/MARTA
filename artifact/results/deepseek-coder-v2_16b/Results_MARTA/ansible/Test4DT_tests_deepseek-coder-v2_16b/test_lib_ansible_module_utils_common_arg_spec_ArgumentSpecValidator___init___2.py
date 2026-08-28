
import pytest
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

# Test valid inputs
def test_valid_inputs():
    argument_spec = {
        'param1': {'type': 'int'},
        'param2': {'type': 'str', 'aliases': ['p2']},
        'param3': {'type': 'float'}
    }
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {
        'param1': 42,
        'param2': 'test',
        'param3': 3.14
    }
    result = validator.validate(parameters)
    assert not result.error_messages, "Validation failed: " + ", ".join(result.error_messages)

# Test edge cases
def test_edge_cases():
    argument_spec = {
        'param1': {'type': 'int'},
        'param2': {'type': 'str', 'aliases': ['p2']},
        'param3': {'type': 'float'}
    }
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {
        'param1': None,
        'param2': '',
        'param3': 0.0
    }
    result = validator.validate(parameters)
    assert not result.error_messages, "Validation failed: " + ", ".join(result.error_messages)

# Test invalid inputs
def test_invalid_inputs():
    argument_spec = {
        'param1': {'type': 'int'},
        'param2': {'type': 'str', 'aliases': ['p2']},
        'param3': {'type': 'float'}
    }
    validator = ArgumentSpecValidator(argument_spec)
    parameters = {
        'param1': 'not an int',
        'param2': 42,
        'param3': 'not a float'
    }
    result = validator.validate(parameters)
    assert len(result.error_messages) == 2, "Validation should fail for incorrect types"


import pytest
from ansible.module_utils.common.parameters import _get_unsupported_parameters

# Test Scenario 1: Valid Inputs
def test_valid_inputs():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
    unsupported_params = _get_unsupported_parameters(argument_spec, parameters)
    assert len(unsupported_params) == 0, f"Expected no unsupported parameters but got {unsupported_params}"

# Test Scenario 2: Edge Cases
def test_edge_cases():
    argument_spec = {}
    parameters = {}
    legal_inputs = []
    options_context = []
    
    unsupported_params = _get_unsupported_parameters(argument_spec, parameters, legal_inputs, options_context)
    assert len(unsupported_params) == 0, f"Expected no unsupported parameters but got {unsupported_params}"

# Test Scenario 3: Invalid Inputs
def test_invalid_inputs():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'invalid_key': 'value'}
    
    unsupported_params = _get_unsupported_parameters(argument_spec, parameters)
    assert len(unsupported_params) == 1, f"Expected one unsupported parameter but got {unsupported_params}"

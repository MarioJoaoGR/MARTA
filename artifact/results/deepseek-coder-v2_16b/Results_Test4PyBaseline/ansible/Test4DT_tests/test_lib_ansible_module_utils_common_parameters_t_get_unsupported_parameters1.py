
import pytest
from ansible.module_utils.common.parameters import _get_unsupported_parameters, _get_legal_inputs

# Test cases for _get_unsupported_parameters function

def test_no_unsupported_parameters():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'option1': 'value1', 'option2': 'value2'}
    
    result = _get_unsupported_parameters(argument_spec, parameters)
    assert result == set()

def test_with_legal_inputs():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    legal_inputs = ['option1', 'option2']
    
    result = _get_unsupported_parameters(argument_spec, parameters, legal_inputs=legal_inputs)
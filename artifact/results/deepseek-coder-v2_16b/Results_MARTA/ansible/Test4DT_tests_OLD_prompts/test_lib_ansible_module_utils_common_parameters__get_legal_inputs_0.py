
import pytest
from unittest.mock import patch
from ansible.module_utils.common.parameters import _get_legal_inputs, _handle_aliases

# Test Scenario 1: Basic Usage
def test__get_legal_inputs_basic():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
    with patch('ansible.module_utils.common.parameters._handle_aliases', return_value={}):
        legal_inputs = _get_legal_inputs(argument_spec, parameters)
        assert set(legal_inputs) == {'option1', 'option2'}, f"Expected ['option1', 'option2'], but got {legal_inputs}"

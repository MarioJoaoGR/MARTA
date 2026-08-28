
import pytest
from unittest.mock import patch
from ansible.module_utils.common.parameters import _get_unsupported_parameters, _get_legal_inputs



def test_no_parameters():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {}
    
    with patch('ansible.module_utils.common.parameters._get_legal_inputs', return_value={'option1', 'option2'}):
        unsupported_params = _get_unsupported_parameters(argument_spec, parameters)
        assert not unsupported_params, f"Unsupported parameters found: {unsupported_params}"
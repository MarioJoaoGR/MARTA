
import pytest
from ansible.module_utils.common.parameters import _get_unsupported_parameters


def test_all_valid_parameters():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
    unsupported_params = _get_unsupported_parameters(argument_spec, parameters)
    assert len(unsupported_params) == 0

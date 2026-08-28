
import pytest
from ansible.module_utils.common.parameters import set_fallbacks

def test_set_fallbacks_basic():
    argument_spec = {
        'param1': {'fallback': (str.upper,)},
        'param2': {'fallback': (lambda x: x * 2,), 'no_log': True}
    }
    parameters = {}
    
    result = set_fallbacks(argument_spec, parameters)
    
    assert len(parameters) == 1
    assert 'param1' in parameters
    assert parameters['param1'] is None
    
    assert len(result) == 1
    assert None in result

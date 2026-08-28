# Module: ansible.module_utils.common.parameters
import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs

# Test cases for _get_legal_inputs function

def test_basic_usage():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
    result = _get_legal_inputs(argument_spec, parameters)
    assert set(result) == {'option1', 'option2'}, f"Expected ['option1', 'option2'], but got {result}"

def test_usage_with_provided_aliases():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    aliases = {'alias1': 'option1', 'alias2': 'option1', 'alias3': 'option2'}
    parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
    result = _get_legal_inputs(argument_spec, parameters, aliases)
    assert set(result) == {'option1', 'option2'}, f"Expected ['option1', 'option2'], but got {result}"

def test_usage_with_no_aliases_provided():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    parameters = {'option1': 'value1', 'option2': 'value2'}  # No aliases in parameters
    
    result = _get_legal_inputs(argument_spec, parameters)
    assert set(result) == {'option1', 'option2'}, f"Expected ['option1', 'option2'], but got {result}"

def test_usage_with_empty_aliases_dictionary():
    argument_spec = {
        'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
        'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
    }
    aliases = {}  # No aliases provided
    parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
    result = _get_legal_inputs(argument_spec, parameters, aliases)
    assert set(result) == {'option1', 'option2'}, f"Expected ['option1', 'option2'], but got {result}"

# Additional test cases can be added to cover more edge cases and scenarios.

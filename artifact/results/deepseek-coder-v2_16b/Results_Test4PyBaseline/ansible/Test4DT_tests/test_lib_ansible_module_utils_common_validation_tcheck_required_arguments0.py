# Module: ansible.module_utils.common.validation
import pytest
from ansible.module_utils.common.validation import check_required_arguments

# Test Case 1: Providing All Required Parameters
def test_check_required_arguments_all_required():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': False}
    }
    parameters = {'param1': 'value1'}
    
    missing_params = check_required_arguments(argument_spec, parameters)
    assert missing_params == ['param2'], "Expected to find param2 as missing"

# Test Case 2: Providing No Required Parameters
def test_check_required_arguments_no_required():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': True}
    }
    parameters = {}
    
    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters)
    assert str(excinfo.value) == "missing required arguments: param1, param2"

# Test Case 3: Providing All Required Parameters and Optional Parameter
def test_check_required_arguments_all_and_optional():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': True}
    }
    parameters = {'param1': 'value1', 'param2': 'value2'}
    
    missing_params = check_required_arguments(argument_spec, parameters)
    assert missing_params == [], "Expected no missing parameters"

# Test Case 4: Providing Conditional Required Parameter
def test_check_required_arguments_conditional():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': False},
        'param3': {'required': True, 'if': lambda params: params.get('param1') == 'specific_value'}
    }
    parameters = {'param1': 'specific_value', 'param3': 'value3'}
    
    missing_params = check_required_arguments(argument_spec, parameters)
    assert missing_params == [], "Expected no missing parameters"

# Test Case 5: Providing Parameters in a Sub-specification Context
def test_check_required_arguments_sub_spec():
    argument_spec = {
        'parent': {
            'required': True,
            'children': {
                'param1': {'required': True},
                'param2': {'required': False}
            }
        }
    }
    parameters = {'parent': {'children': {'param1': 'value1'}}}
    
    missing_params = check_required_arguments(argument_spec, parameters, options_context=['parent', 'children'])
    assert missing_params == ['param2'], "Expected to find param2 as missing"


import pytest
from ansible.module_utils.common.validation import check_required_arguments

# Test Case 6: Argument spec is None
def test_check_required_arguments_argument_spec_is_none():
    argument_spec = None
    parameters = {'param1': 'value1'}
    
    missing_params = check_required_arguments(argument_spec, parameters)
    assert missing_params == [], "Expected no missing parameters when argument spec is None"

# Test Case 7: Argument spec does not contain required parameters
def test_check_required_arguments_no_required_in_spec():
    argument_spec = {
        'param1': {'optional': True},
        'param2': {'optional': True}
    }
    parameters = {}
    
    missing_params = check_required_arguments(argument_spec, parameters)
    assert missing_params == [], "Expected no missing parameters when none are required"

# Test Case 8: Argument spec contains a single required parameter not in parameters
def test_check_required_arguments_single_missing_required():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'optional': True}
    }
    parameters = {}
    
    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters)
    assert str(excinfo.value).startswith("missing required arguments:"), "Expected a TypeError indicating missing required arguments"

# Test Case 9: Argument spec contains multiple missing required parameters
def test_check_required_arguments_multiple_missing_required():
    argument_spec = {
        'param1': {'required': True},
        'param2': {'required': True},
        'param3': {'optional': True}
    }
    parameters = {'param1': 'value1'}
    
    with pytest.raises(TypeError) as excinfo:
        check_required_arguments(argument_spec, parameters)
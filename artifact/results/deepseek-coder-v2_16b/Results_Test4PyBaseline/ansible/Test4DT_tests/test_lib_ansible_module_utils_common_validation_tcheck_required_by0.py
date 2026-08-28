# Module: ansible.module_utils.common.validation
import pytest
from ansible.module_utils.common.validation import check_required_by

# Example 1: All required parameters are present
def test_check_required_by_all_present():
    requirements = {'param1': ['sub_param1', 'sub_param2'], 'param2': 'sub_param3'}
    parameters = {'param1': {'sub_param1': 1, 'sub_param2': None}, 'param2': {'sub_param3': True}}
    
    result = check_required_by(requirements, parameters)
    assert result == {}

# Example 2: Missing a required parameter
def test_check_required_by_missing_parameter():
    requirements = {'param1': ['sub_param1', 'sub_param2'], 'param2': 'sub_param3'}
    parameters = {'param1': {'sub_param1': 1}}
    
    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters)
    assert str(excinfo.value) == "missing parameter(s) required by 'param2': sub_param3"

# Example 3: Missing a nested required parameter
def test_check_required_by_nested_missing_parameter():
    requirements = {'param1': ['sub_param1', 'sub_param2'], 'param2': 'sub_param3'}
    parameters = {'param1': {'sub_param1': 1, 'sub_param2': None}, 'param2': {}}
    
    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters)
    assert str(excinfo.value) == "missing parameter(s) required by 'param2': sub_param3"

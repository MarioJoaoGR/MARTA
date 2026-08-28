
import pytest
from ansible.module_utils.common.validation import check_required_by

# Test case for when requirements is None
def test_check_required_by_requirements_is_none():
    requirements = None
    parameters = {'param1': 'value1'}
    
    result = check_required_by(requirements, parameters)
    assert result == {}

# Test case for when a parameter is missing in the main dictionary but present in nested dictionaries
def test_check_required_by_missing_in_nested():
    requirements = {'param1': ['sub_param1', 'sub_param2']}
    parameters = {'param1': {'sub_param3': True}}
    
    with pytest.raises(TypeError) as excinfo:
        check_required_by(requirements, parameters)

import pytest
from ansible.module_utils.common.validation import check_required_by

def test_check_required_by_basic():
    requirements = {'param1': ['req1', 'req2'], 'param2': 'req3'}
    parameters = {'param1': [1, 2], 'param2': 3, 'req1': 1, 'req2': 2, 'req3': 3}
    
    result = check_required_by(requirements, parameters)
    assert result == {}

    # Test with missing parameter
    requirements = {'param1': ['req1', 'req2'], 'param2': 'req3'}
    parameters = {'param1': [1, 2], 'param2': 3}
    
    with pytest.raises(TypeError) as exc_info:
        check_required_by(requirements, parameters)
    
    assert str(exc_info.value) == "missing parameter(s) required by 'param1': req1, req2 found in -> param1"


import pytest
from ansible.module_utils.common.validation import check_required_by


def test_missing_parameter():
    requirements = {'param1': ['req1', 'req2'], 'param2': 'req3'}
    parameters = {'param1': [1, 2], 'param2': 3}
    with pytest.raises(TypeError):
        check_required_by(requirements, parameters)

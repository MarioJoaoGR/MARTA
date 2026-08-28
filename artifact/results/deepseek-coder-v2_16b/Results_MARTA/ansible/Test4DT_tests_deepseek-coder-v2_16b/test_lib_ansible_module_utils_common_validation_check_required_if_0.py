
import pytest
from ansible.module_utils.common.validation import check_required_if


def test_missing_requirement():
    requirements = [
        ['state', 'present', ('path',)],
        ['someint', 99, ('bool_param', 'string_param')],
    ]
    parameters = {'state': 'present'}
    with pytest.raises(TypeError) as excinfo:
        check_required_if(requirements, parameters)
    assert "all of the following are missing" in str(excinfo.value)

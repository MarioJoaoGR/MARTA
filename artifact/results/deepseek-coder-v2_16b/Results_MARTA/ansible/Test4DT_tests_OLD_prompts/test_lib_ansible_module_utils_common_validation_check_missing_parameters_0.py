
import pytest
from ansible.module_utils.common.validation import check_missing_parameters


def test_valid_input():
    parameters = {'a': 1, 'b': 2}
    required_parameters = ['a', 'b']
    result = check_missing_parameters(parameters, required_parameters)
    assert result == []

def test_invalid_input():
    parameters = {'a': 1}
    required_parameters = ['a', 'b']
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    assert str(excinfo.value) == "missing required arguments: b"
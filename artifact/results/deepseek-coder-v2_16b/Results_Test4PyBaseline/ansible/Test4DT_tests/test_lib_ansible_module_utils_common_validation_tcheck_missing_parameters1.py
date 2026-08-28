
# Module: ansible.module_utils.common.validation
import pytest
from ansible.module_utils.common.validation import check_missing_parameters

# Test cases for check_missing_parameters function

def test_check_missing_parameters_empty_parameters():
    parameters = {}
    required_parameters = ['a', 'b']
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    assert str(excinfo.value) == "missing required arguments: a, b"

def test_check_missing_parameters_none_required():
    parameters = {'a': 1, 'b': 2}
    required_parameters = None
    result = check_missing_parameters(parameters, required_parameters)
    assert result == []

def test_check_missing_parameters_one_present_one_missing():
    parameters = {'a': 1}
    required_parameters = ['a', 'b']
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    assert str(excinfo.value) == "missing required arguments: b"

def test_check_missing_parameters_all_present():
    parameters = {'a': 1, 'b': 2}
    required_parameters = ['a', 'b']
    result = check_missing_parameters(parameters, required_parameters)
    assert result == []

def test_check_missing_parameters_none_present():
    parameters = {}
    required_parameters = ['a', 'b']
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    assert str(excinfo.value) == "missing required arguments: a, b"

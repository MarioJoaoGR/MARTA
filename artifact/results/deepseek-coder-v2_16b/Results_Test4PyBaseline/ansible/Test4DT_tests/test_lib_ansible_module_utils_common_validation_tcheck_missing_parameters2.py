
# Module: ansible.module_utils.common.validation
import pytest
from ansible.module_utils.common.validation import check_missing_parameters

# Test cases for check_missing_parameters function

def test_check_missing_parameters_no_params():
    """Test when no parameters are provided."""
    parameters = {}
    required_parameters = ['a', 'b']
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    assert str(excinfo.value) == "missing required arguments: a, b"

def test_check_missing_parameters_all_params():
    """Test when all required parameters are provided."""
    parameters = {'a': 1, 'b': 2}
    required_parameters = ['a', 'b']
    result = check_missing_parameters(parameters, required_parameters)
    assert result == []

def test_check_missing_parameters_one_param_missing():
    """Test when one of the required parameters is missing."""
    parameters = {'a': 1}
    required_parameters = ['a', 'b']
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    assert str(excinfo.value) == "missing required arguments: b"

def test_check_missing_parameters_all_params_missing():
    """Test when none of the required parameters are provided."""
    parameters = {}
    required_parameters = ['a', 'b']
    with pytest.raises(TypeError) as excinfo:
        check_missing_parameters(parameters, required_parameters)
    assert str(excinfo.value) == "missing required arguments: a, b"

def test_check_missing_parameters_none_required():
    """Test when no required parameters are specified."""
    parameters = {'a': 1, 'b': 2}
    required_parameters = None
    result = check_missing_parameters(parameters, required_parameters)
    assert result == []

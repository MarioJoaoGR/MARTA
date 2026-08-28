
import pytest
from ansible.module_utils.common.validation import check_mutually_exclusive

# Test Scenario 1: Basic valid input
def test_valid_input_basic():
    terms = [['param1', 'param2'], ['param3']]
    parameters = {'param1': 1, 'param2': 2, 'param3': 3}
    result = check_mutually_exclusive(terms, parameters)
    assert result == []

# Test Scenario 2: Error input due to conflict
def test_error_input_conflict():
    terms = ['param1', 'param1']
    parameters = {'param1': 1, 'param2': 2}
    with pytest.raises(TypeError) as excinfo:
        check_mutually_exclusive(terms, parameters)
    assert str(excinfo.value) == "parameters are mutually exclusive: param1|param1"

# Test Scenario 3: Error input due to missing lines coverage
def test_error_input_missing_lines():
    terms = None
    parameters = {'param1': 1, 'param2': 2}
    with pytest.raises(TypeError) as excinfo:
        check_mutually_exclusive(terms, parameters)
    assert str(excinfo.value) == "parameters are mutually exclusive: param1|param2"

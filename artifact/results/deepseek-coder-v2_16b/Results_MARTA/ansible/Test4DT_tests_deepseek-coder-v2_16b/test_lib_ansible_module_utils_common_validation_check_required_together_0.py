
import pytest
from your_module import check_required_together  # Replace 'your_module' with the actual module name where `check_required_together` is defined.

# Test for valid input
def test_valid_input():
    terms = [["param1", "param2"], ["param3"]]
    parameters = {"param1": 1, "param2": 2, "param3": 3}
    result = check_required_together(terms, parameters)
    assert result == []

# Test for None input
def test_none_input():
    terms = None
    parameters = {"param1": 1, "param2": 2}
    result = check_required_together(terms, parameters)
    assert result == []

# Test for missing parameter in terms
def test_missing_parameter():
    terms = [["param1", "param2"], ["param4"]]
    parameters = {"param1": 1, "param3": 3}
    with pytest.raises(TypeError) as excinfo:
        check_required_together(terms, parameters)
    assert str(excinfo.value) == 'parameters are required together: param2, param4'

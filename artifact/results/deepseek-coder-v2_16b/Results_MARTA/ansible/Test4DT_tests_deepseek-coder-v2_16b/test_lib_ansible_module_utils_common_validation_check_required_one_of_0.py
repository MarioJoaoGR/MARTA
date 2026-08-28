
import pytest
from ansible.module_utils.common.validation import check_required_one_of

# Test case 1: All required terms are present in the parameters dictionary
def test_valid_case_all_terms_present():
    terms = [["param1", "param2"], ["foo", "bar"]]
    parameters = {"param1": 1, "param2": 2, "foo": 3, "bar": 4}
    result = check_required_one_of(terms, parameters)
    assert result == []

# Test case 2: None of the required terms are present in the parameters dictionary
def test_error_case_none_of_the_terms_present():
    terms = [["missing1", "missing2"], ["foo", "bar"]]
    parameters = {"param1": 1, "param2": 2, "foo": 3, "bar": 4}
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of(terms, parameters)
    assert str(excinfo.value) == 'one of the following is required: missing1, missing2 found in terms -> options_context'

# Test case 3: Invalid input (None) provided
def test_error_case_invalid_input():
    terms = None
    parameters = {"param1": 1, "param2": 2, "foo": 3, "bar": 4}
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of(terms, parameters)
    assert str(excinfo.value) == 'one of the following is required: param1, param2 found in terms -> options_context'

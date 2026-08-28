# Module: ansible.module_utils.common.validation
import pytest
from ansible.module_utils.common.validation import check_required_together

# Test cases for check_required_together function

def test_all_required_parameters_are_present():
    terms = [["a", "b"], ["c"]]
    parameters = {"a": 1, "b": 2, "c": 3}
    result = check_required_together(terms, parameters)
    assert result == []

def test_one_of_the_required_parameters_is_missing():
    terms = [["a", "b"], ["c"]]
    parameters = {"a": 1}
    with pytest.raises(TypeError) as excinfo:
        check_required_together(terms, parameters)
    assert str(excinfo.value) == 'parameters are required together: b'

def test_parameters_from_different_lists_are_present():
    terms = [["a", "b"], ["c"]]
    parameters = {"a": 1, "c": 3}
    with pytest.raises(TypeError) as excinfo:
        check_required_together(terms, parameters)
    assert str(excinfo.value) == 'parameters are required together: b'

def test_using_options_context_to_indicate_a_sub_specification():
    terms = [["a", "b"], ["c"]]
    parameters = {"a": 1, "b": 2}
    options_context = ["parent_key"]
    result = check_required_together(terms, parameters, options_context)
    assert result == []

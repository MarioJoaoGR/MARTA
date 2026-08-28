# Module: ansible.module_utils.common.validation
import pytest
from ansible.module_utils.common.validation import check_required_one_of

# Helper function to count terms in parameters for testing purposes
def count_terms(terms, parameters):
    return sum([1 for t in terms if t in parameters])

# Test cases for check_required_one_of function

def test_check_required_one_of_all_present():
    assert check_required_one_of([["a", "b"], ["c"]], {"a": 1, "b": 2}) == []

def test_check_required_one_of_none_present():
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of([["x", "y"], ["z"]], {"a": 1, "b": 2})
    assert str(excinfo.value) == 'one of the following is required: x, y -> z'

def test_check_required_one_of_nested_terms():
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of([["nested1", "nested2"]], {"parent": {"nested1": 1}}, options_context=["parent"])
    assert str(excinfo.value) == 'one of the following is required: nested1, nested2 -> parent -> nested1'

def test_check_required_one_of_default_values():
    with pytest.raises(TypeError) as excinfo:
        check_required_one_of([["param1", "param2"], ["param3"]], {"param1": 1})
    assert str(excinfo.value) == 'one of the following is required: param1 -> param2, param3'

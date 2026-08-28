# Module: ansible.module_utils.common.validation
import pytest
from ansible.module_utils.common.validation import check_mutually_exclusive

# Example 1: Basic Usage
def test_check_mutually_exclusive_basic():
    terms = [["a", "b"], ["c", "d"]]
    parameters = {"a": 1, "b": 2, "c": 3, "d": 4}
    result = check_mutually_exclusive(terms, parameters)
    assert result == []

# Example 2: Mutual Exclusivity Issue
def test_check_mutually_exclusive_issue():
    terms = [["a", "b"], ["a", "c"]]
    parameters = {"a": 1, "b": 2, "c": 3}
    with pytest.raises(TypeError) as excinfo:
        check_mutually_exclusive(terms, parameters)
    assert str(excinfo.value) == 'parameters are mutually exclusive: a|b -> a|c'

# Example 3: Optional Context Specification
def test_check_mutually_exclusive_context():
    terms = [["x", "y"], ["z"]]
    parameters = {"x": 1, "y": 2, "z": 3}
    options_context = ["parent"]
    result = check_mutually_exclusive(terms, parameters, options_context=options_context)
    assert result == []

# Example 4: No Terms Provided
def test_check_mutually_exclusive_no_terms():
    terms = None
    parameters = {"a": 1, "b": 2}
    result = check_mutually_exclusive(terms, parameters)
    assert result == []

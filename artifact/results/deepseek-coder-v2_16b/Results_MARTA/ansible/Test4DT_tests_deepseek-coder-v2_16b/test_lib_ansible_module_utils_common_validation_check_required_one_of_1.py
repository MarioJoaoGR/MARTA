
import pytest
from ansible.module_utils.common.validation import check_required_one_of

def count_terms(terms, parameters):
    return sum([1 for term in terms if term in parameters])


def test_all_terms_present():
    terms = [["param1", "param2"], ["foo", "bar"]]
    parameters = {"param1": 1, "param2": 2, "foo": 3, "bar": 4}
    result = check_required_one_of(terms, parameters)
    assert result == []

def test_no_terms():
    terms = []
    parameters = {"param1": 1, "param2": 2}
    result = check_required_one_of(terms, parameters)
    assert result == []

def test_terms_as_tuples():
    terms = [("param1", "param2"), ("foo", "bar")]
    parameters = {"param1": 1, "param2": 2, "foo": 3, "bar": 4}
    result = check_required_one_of(terms, parameters)
    assert result == []
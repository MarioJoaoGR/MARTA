
import pytest
from ansible.module_utils.common.validation import count_terms

def test_count_terms_single_term():
    terms = "hello"
    parameters = {"hello": 1, "world": 2}
    result = count_terms(terms, parameters)
    assert result == 1

def test_count_terms_multiple_terms():
    terms = ["hello", "world"]
    parameters = {"hello": 1, "world": 2, "foo": 3}
    result = count_terms(terms, parameters)
    assert result == 2

def test_count_terms_no_terms():
    terms = ["hello", "foo"]
    parameters = {"bar": 4, "baz": 5}
    result = count_terms(terms, parameters)
    assert result == 0

def test_count_terms_single_term_as_list():
    terms = ["hello"]
    parameters = {"hello": 1, "world": 2}
    result = count_terms(terms, parameters)
    assert result == 1


import pytest
from ansible.module_utils.common.validation import count_terms

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Test 1: Count occurrences of a single term in a dictionary
def test_count_terms_single_term():
    terms = "hello"
    parameters = {"hello": 1, "world": 2}
    result = count_terms(terms, parameters)
    assert result == 1

# Test 2: Count occurrences of multiple terms in a dictionary
def test_count_terms_multiple_terms():
    terms = ["hello", "world"]
    parameters = {"hello": 1, "world": 2, "foo": 3}
    result = count_terms(terms, parameters)
    assert result == 2

# Test 3: Count occurrences of no terms in a dictionary (should return 0)
def test_count_terms_no_terms():
    terms = ["hello", "foo"]
    parameters = {"bar": 4, "baz": 5}
    result = count_terms(terms, parameters)
    assert result == 0

# Test 4: Count occurrences of a single term when provided as a list
def test_count_terms_single_term_as_list():
    terms = ["hello"]
    parameters = {"hello": 1, "world": 2}
    result = count_terms(terms, parameters)
    assert result == 1

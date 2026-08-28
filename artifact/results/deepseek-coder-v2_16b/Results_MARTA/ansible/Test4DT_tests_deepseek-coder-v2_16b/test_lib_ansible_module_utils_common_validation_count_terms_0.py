
import pytest
from ansible.module_utils.common.validation import count_terms

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Test case 1: Count occurrences of a single term in a dictionary
def test_count_terms_single_term():
    result = count_terms("hello", {"hello": 1, "world": 2})
    assert result == 1

# Test case 2: Count occurrences of multiple terms in a dictionary
def test_count_terms_multiple_terms():
    result = count_terms(["hello", "world"], {"hello": 1, "world": 2, "foo": 3})
    assert result == 2

# Test case 3: Count occurrences of no terms in a dictionary (should return 0)
def test_count_terms_no_terms():
    result = count_terms(["hello", "foo"], {"bar": 4, "baz": 5})
    assert result == 0

# Test case 4: Count occurrences of a single term when provided as a list
def test_count_terms_single_term_as_list():
    result = count_terms(["hello"], {"hello": 1, "world": 2})
    assert result == 1

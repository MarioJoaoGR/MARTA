
import pytest
from ansible.module_utils.common.validation import count_terms

# Test cases for the count_terms function

def test_count_terms_single_string():
    assert count_terms("a", {"a": 1, "b": 2}) == 1

def test_count_terms_multiple_terms_list():
    assert count_terms(["a", "b"], {"a": 1, "b": 2, "c": 3}) == 2

def test_count_terms_multiple_terms_set():
    assert count_terms({"a", "b"}, {"a": 1, "b": 2, "c": 3}) == 2

# Additional edge cases to consider:

def test_count_terms_empty_dictionary():
    assert count_terms("a", {}) == 0

@pytest.mark.xfail(raises=TypeError)
def test_count_terms_non_iterable_term():
    count_terms(1, {"a": 1})  # Expecting TypeError because 1 is not iterable

def test_count_terms_nonexistent_term():
    assert count_terms("c", {"a": 1, "b": 2}) == 0

# Test cases for the case where terms is a single string but passed as an iterable
def test_count_terms_single_string_as_iterable():
    assert count_terms(["a"], {"a": 1, "b": 2}) == 1

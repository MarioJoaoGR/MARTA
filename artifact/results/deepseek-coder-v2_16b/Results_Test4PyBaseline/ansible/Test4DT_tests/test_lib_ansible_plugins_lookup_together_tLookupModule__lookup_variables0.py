
import pytest
from ansible.plugins.lookup import together as lookup_module

# Assuming the function is imported correctly from the module

def test_transpose_basic():
    lm = lookup_module.LookupModule()
    terms = [[1, 2], [3, 4]]
    result = lm._lookup_variables(terms)
    assert result == [[1, 3], [2, 4]], f"Expected [[1, 3], [2, 4]], but got {result}"

def test_transpose_with_empty():
    lm = lookup_module.LookupModule()
    terms = [[1, 2], []]
    result = lm._lookup_variables(terms)
    assert result == [[1, None], [2, None]], f"Expected [[1, None], [2, None]], but got {result}"

def test_transpose_empty_list():
    lm = lookup_module.LookupModule()
    terms = []
    result = lm._lookup_variables(terms)
    assert result == [], f"Expected an empty list for an empty input, but got {result}"

def test_transpose_single_sublist():
    lm = lookup_module.LookupModule()
    terms = [[1, 2, 3]]
    result = lm._lookup_variables(terms)
    assert result == [[1], [2], [3]], f"Expected [[1], [2], [3]], but got {result}"

def test_transpose_multiple_sublists():
    lm = lookup_module.LookupModule()
    terms = [[1], [2, 3], [4, 5, 6]]
    result = lm._lookup_variables(terms)
    assert result == [[1, 2, 4], [None, 3, 5], [None, None, 6]], f"Expected [[1, 2, 4], [None, 3, 5], [None, None, 6]], but got {result}"

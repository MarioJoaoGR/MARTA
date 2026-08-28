
import pytest
from ansible.plugins.lookup.first_found import _split_on



def test_single_term():
    terms = 'apple'
    expected = ['apple']
    assert _split_on(terms) == expected, f"Expected {expected}, but got {_split_on(terms)}"

def test_multiple_terms():
    terms = 'apple,banana,orange'
    expected = ['apple', 'banana', 'orange']
    assert _split_on(terms) == expected, f"Expected {expected}, but got {_split_on(terms)}"

def test_multiple_terms_with_spaces():
    terms = 'apple banana orange'
    expected = ['apple', 'banana', 'orange']
    assert _split_on(terms) == expected, f"Expected {expected}, but got {_split_on(terms)}"

def test_nested_list():
    terms = ['apple', ['banana', 'orange']]
    expected = ['apple', 'banana', 'orange']
    assert _split_on(terms) == expected, f"Expected {expected}, but got {_split_on(terms)}"

import pytest
from lib.ansible.plugins.lookup import LookupModule
import random

# Test for valid input scenario
def test_valid_input():
    lookup_module = LookupModule()
    terms = ['apple', 'banana', 'cherry']
    result = lookup_module.run(terms)
    assert isinstance(result, list), "Expected a list but got something else"
    assert len(result) == 1, "Expected a single item in the list but got more or less"
    assert result[0] in terms, "The selected term is not in the provided list"

# Test for empty list scenario
def test_empty_list():
    lookup_module = LookupModule()
    terms = []
    result = lookup_module.run(terms)
    assert isinstance(result, list), "Expected a list but got something else"
    assert len(result) == 0, "Expected an empty list but it is not empty"

# Test for invalid input scenario
def test_invalid_input():
    lookup_module = LookupModule()
    terms = None
    with pytest.raises(TypeError):
        result = lookup_module.run(terms)

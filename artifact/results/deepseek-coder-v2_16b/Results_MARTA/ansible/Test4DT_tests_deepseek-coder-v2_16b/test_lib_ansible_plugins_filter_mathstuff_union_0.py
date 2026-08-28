
import pytest
from typing import Hashable
from ansible.plugins.filter.mathstuff import unique

# Fixture to provide a consistent environment for all tests
@pytest.fixture(scope="module")
def environment():
    return {'var': 'value'}

@pytest.fixture(scope="module")
def a():
    return [1, 2, 3]

@pytest.fixture(scope="module")
def b():
    return {3, 4, 5}

# Test for valid input scenario
def test_valid_input(environment, a, b):
    result = union(environment, a, b)
    assert isinstance(result, list), "Expected output to be a list"
    assert set(result) == {1, 2, 3, 4, 5}, "Union of lists should include all unique elements"

# Test for edge case scenario with None and empty lists/sets
def test_edge_case():
    environment = {}
    a = []
    b = None
    result = union(environment, a, b)
    assert isinstance(result, list), "Expected output to be a list"
    assert len(result) == 0, "Union of empty list and None should yield an empty list"

# Test for invalid input scenario
def test_invalid_input():
    environment = {}
    a = 'not a list or set'
    b = 123
    result = union(environment, a, b)
    assert isinstance(result, list), "Expected output to be a list"
    assert len(result) == 0, "Union of non-list/set types should yield an empty list"

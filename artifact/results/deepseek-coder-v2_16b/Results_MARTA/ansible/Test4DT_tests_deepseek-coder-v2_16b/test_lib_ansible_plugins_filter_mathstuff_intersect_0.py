
import pytest
from ansible.plugins.filter.mathstuff import intersect

def test_valid_case():
    environment = {'var': 'value'}
    a = ['apple', 'banana', 'Apple', 'cherry']
    b = ['banana', 'grape', 'Cherry']
    expected = ['banana']
    result = intersect(environment, a, b)
    assert set(result) == set(expected)

def test_edge_case():
    environment = {}
    a = []
    b = None
    expected = []
    result = intersect(environment, a, b)
    assert list(result) == expected

def test_invalid_input():
    environment = {'var': 'value'}
    a = 123
    b = [456]
    with pytest.raises(TypeError):
        intersect(environment, a, b)

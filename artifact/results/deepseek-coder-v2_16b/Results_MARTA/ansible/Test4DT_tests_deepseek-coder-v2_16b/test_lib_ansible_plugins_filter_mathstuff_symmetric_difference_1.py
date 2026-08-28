
import pytest
from ansible.plugins.filter.mathstuff import symmetric_difference, union, intersect

def test_valid_case():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = [3, 4, 5]
    result = symmetric_difference(environment, a, b)
    assert result == [1, 2, 4, 5], f"Expected [1, 2, 4, 5] but got {result}"

def test_edge_case():
    environment = {}
    a = None
    b = []
    with pytest.raises(TypeError):
        symmetric_difference(environment, a, b)

def test_error_case():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = ['a', 'b']
    with pytest.raises(TypeError):
        symmetric_difference(environment, a, b)

# Module: ansible.plugins.filter.mathstuff
import pytest
from ansible.plugins.filter.mathstuff import symmetric_difference

# Test cases for symmetric_difference function
def test_symmetric_difference_sets():
    environment = {'var': 'value'}
    a = {1, 2, 3}
    b = {2, 3, 4}
    result = symmetric_difference(environment, a, b)
    assert result == [1, 4]

def test_symmetric_difference_lists():
    environment = {'var': 'value'}
    a = ['a', 'b']
    b = ['b', 'c']
    result = symmetric_difference(environment, a, b)
    assert result == ['a', 'c']

def test_symmetric_difference_mixed():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = [2, 3, 4]
    result = symmetric_difference(environment, a, b)
    assert result == [1, 4]

def test_symmetric_difference_not_hashable():
    environment = {'var': 'value'}
    a = [1, 2, {3}]
    b = [2, 3, {4}]
    with pytest.raises(TypeError):
        symmetric_difference(environment, a, b)

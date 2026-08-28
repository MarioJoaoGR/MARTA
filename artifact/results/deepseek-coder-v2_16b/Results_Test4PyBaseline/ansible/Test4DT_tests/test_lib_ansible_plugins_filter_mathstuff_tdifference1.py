
import pytest
from ansible.plugins.filter import mathstuff

# Test cases for difference function
def test_difference_with_lists():
    environment = {'var': 'value'}
    result = mathstuff.difference(environment, [1, 2, 3], [2, 3, 4])
    assert set(result) == {1}

def test_difference_with_sets():
    environment = {'var': 'value'}
    result = mathstuff.difference(environment, {'apple', 'banana', 'cherry'}, {'banana', 'date'})
    assert set(result) == {'apple', 'cherry'}

def test_difference_with_mixed_types():
    environment = {'var': 'value'}
    result = mathstuff.difference(environment, [1, 2, 3], {2, 3, 4})
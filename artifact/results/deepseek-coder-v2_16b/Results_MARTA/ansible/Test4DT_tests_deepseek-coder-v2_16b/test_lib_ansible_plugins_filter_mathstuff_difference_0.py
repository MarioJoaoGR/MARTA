
import pytest
from ansible.plugins.filter.mathstuff import difference

def test_valid_input_lists():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = [2, 3, 4]
    expected_output = [1]
    assert difference(environment, a, b) == expected_output

def test_valid_input_sets():
    environment = {'var': 'value'}
    a = {1, 2, 3}
    b = {2, 3, 4}
    expected_output = [1]
    assert difference(environment, a, b) == expected_output

def test_invalid_input_non_hashable():
    environment = {'var': 'value'}
    a = ['a', 1]
    b = {'b': 2}
    expected_output = [{'a': 1}]
    assert difference(environment, a, b) == expected_output


import pytest
from ansible.plugins.filter import mathstuff

# Test cases for intersect function
def test_intersect_with_hashable_inputs():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = [2, 3, 4]
    expected_output = [2, 3]
    assert mathstuff.intersect(environment, a, b) == expected_output

def test_intersect_with_non_hashable_inputs():
    environment = {'var': 'value'}
    a = {'a': 1}
    b = {'b': 2}
    expected_output = []
    assert mathstuff.intersect(environment, a, b) == expected_output

def test_intersect_with_empty_inputs():
    environment = {'var': 'value'}
    a = []
    b = []
    expected_output = []
    assert mathstuff.intersect(environment, a, b) == expected_output

def test_intersect_with_one_empty_input():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = []
    expected_output = []
    assert mathstuff.intersect(environment, a, b) == expected_output

# Additional test cases for uncovered lines 93-94 and 96-97
def test_intersect_with_non_hashable_and_hashable_inputs():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = {3, 4}
    expected_output = [3]
    assert mathstuff.intersect(environment, a, b) == expected_output

def test_intersect_with_hashable_and_non_hashable_inputs():
    environment = {'var': 'value'}
    a = {1, 2, 3}
    b = [2, 3, 4]
    expected_output = [2, 3]
    assert mathstuff.intersect(environment, a, b) == expected_output

def test_intersect_with_non_hashable_and_non_hashable_inputs():
    environment = {'var': 'value'}
    a = {1: 'a', 2: 'b'}
    b = [3, 4]
    expected_output = []
    assert mathstuff.intersect(environment, a, b) == expected_output

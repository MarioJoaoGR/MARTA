
# Module: ansible.plugins.filter.mathstuff
from ansible.plugins.filter import mathstuff
import pytest

def test_union_with_non_hashable_inputs():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = [2, 3, 4]
    expected_result = {1, 2, 3, 4}
    
    result = mathstuff.union(environment, a, b)
    assert set(result) == expected_result

def test_union_with_non_hashable_inputs_different_order():
    environment = {'var': 'value'}
    a = [2, 3, 4]
    b = [1, 2, 3]
    expected_result = {1, 2, 3, 4}
    
    result = mathstuff.union(environment, a, b)
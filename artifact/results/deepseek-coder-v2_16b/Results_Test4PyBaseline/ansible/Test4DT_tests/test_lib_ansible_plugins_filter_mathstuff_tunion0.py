# Module: ansible.plugins.filter.mathstuff
# Import the function using its provided module name.
from ansible.plugins.filter import mathstuff

def test_union_with_hashable_inputs():
    environment = {'var': 'value'}
    a = {1, 2, 3}
    b = {2, 3, 4}
    expected_result = {1, 2, 3, 4}
    
    result = mathstuff.union(environment, a, b)
    assert result == expected_result

def test_union_with_non_hashable_inputs():
    environment = {'var': 'value'}
    a = [1, 2, 3]
    b = [2, 3, 4]
    expected_result = {1, 2, 3, 4}
    
    result = mathstuff.union(environment, a, b)
    assert result == expected_result

def test_union_with_mixed_hashable_and_non_hashable_inputs():
    environment = {'var': 'value'}
    a = {1, 2, 3}
    b = [2, 3, 4]
    expected_result = {1, 2, 3, 4}
    
    result = mathstuff.union(environment, a, b)
    assert result == expected_result


import pytest
from ansible.plugins.filter.mathstuff import intersect

def test_valid_case_1():
    environment = {'var': 'value'}
    a = ['apple', 'banana', 'Apple', 'cherry']
    b = ['banana', 'grape', 'Cherry']
    
    result = intersect(environment, a, b)
    assert result == ['banana']

def test_valid_case_2():
    environment = {'var': 'value'}
    a = [{'name': 'Alice'}, {'name': 'Bob'}]
    b = [{'name': 'Alice'}, {'age': 30}]
    
    result = intersect(environment, a, b)
    assert result == [{'name': 'Alice'}]

def test_error_case():
    environment = None
    a = None
    b = None
    
    with pytest.raises(TypeError):
        intersect(environment, a, b)

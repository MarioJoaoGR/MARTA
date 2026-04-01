
import pytest

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

def test_edge_cases():
    # Test with None as mapper
    with pytest.raises(TypeError):
        curried_map(None, [1, 2, 3])
    
    # Test with empty list
    assert curried_map(lambda x: x * 2, []) == []
    
    # Test with boundary values
    assert curried_map(lambda x: x + 1, [0]) == [1]
    assert curried_map(lambda x: x + 1, [-1]) == [0]
    assert curried_map(lambda x: x + 1, [99]) == [100]
    
    # Test with a simple mapper function
    def square(x):
        return x ** 2
    
    assert curried_map(square, [1, 2, 3, 4]) == [1, 4, 9, 16]
    
    # Test with a string mapper function
    def to_uppercase(s):
        return s.upper()
    
    assert curried_map(to_uppercase, ['hello', 'world']) == ['HELLO', 'WORLD']

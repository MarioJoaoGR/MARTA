# Module: pymonet.utils
import pytest
from pymonet.utils import curried_map

# Test cases for curried_map function

def test_curried_map_with_square():
    def square(x):
        return x ** 2
    
    result = curried_map(square, [1, 2, 3, 4])
    assert result == [1, 4, 9, 16]

def test_curried_map_with_to_uppercase():
    def to_uppercase(s):
        return s.upper()
    
    result = curried_map(to_uppercase, ['hello', 'world'])
    assert result == ['HELLO', 'WORLD']

def test_curried_map_with_double():
    def double(x):
        return x * 2
    
    result = curried_map(double, [1, 2, 3, 4])
    assert result == [2, 4, 6, 8]

def test_curried_map_with_identity():
    def identity(x):
        return x
    
    result = curried_map(identity, [1, 2, 3, 4])
    assert result == [1, 2, 3, 4]

def test_curried_map_with_empty_collection():
    def square(x):
        return x ** 2
    
    result = curried_map(square, [])
    assert result == []

def test_curried_map_with_none_mapper():
    with pytest.raises(TypeError):
        curried_map(None, [1, 2, 3, 4])

def test_curried_map_with_none_collection():
    def square(x):
        return x ** 2
    
    with pytest.raises(TypeError):
        curried_map(square, None)

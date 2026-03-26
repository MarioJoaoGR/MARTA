# Module: pymonet.utils
import pytest
from pymonet.utils import curried_map

# Test cases for the curried_map function

def test_curried_map_with_lambda():
    result = curried_map(lambda x: x * 2, [1, 2, 3])
    assert result == [2, 4, 6]

def test_curried_map_with_str_upper():
    result = curried_map(str.upper, ['hello', 'world'])
    assert result == ['HELLO', 'WORLD']

def test_curried_map_with_custom_function():
    def square(x):
        return x ** 2
    
    numbers = [1, 2, 3, 4]
    result = curried_map(square, numbers)
    assert result == [1, 4, 9, 16]

def test_curried_map_with_empty_collection():
    result = curried_map(lambda x: x * 2, [])
    assert result == []

def test_curried_map_with_none_mapper():
    with pytest.raises(TypeError):
        curried_map(None, [1, 2, 3])

def test_curried_map_with_none_collection():
    with pytest.raises(TypeError):
        curried_map(lambda x: x * 2, None)

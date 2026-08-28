
import pytest
from pymonet.utils import curried_map

# Test cases for the curried_map function

def test_curried_map_lambda():
    result = curried_map(lambda x: x * 2, [1, 2, 3])
    assert result == [2, 4, 6]

def test_curried_map_str_upper():
    result = curried_map(str.upper, ['hello', 'world'])
    assert result == ['HELLO', 'WORLD']

def test_curried_map_int():
    result = curried_map(int, ['1', '2', '3'])
    assert result == [1, 2, 3]

def test_curried_map_invalid_mapper():
    with pytest.raises(TypeError):
        curried_map("not a callable", [1, 2, 3])

def test_curried_map_empty_collection():
    result = curried_map(lambda x: x * 2, [])
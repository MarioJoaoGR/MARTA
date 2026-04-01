
import pytest

def square(x):
    return x ** 2

def curried_map(mapper, collection):
    return [mapper(item) for item in collection]

def test_valid_input():
    # Test case with a simple mapper function and a list of integers
    result = curried_map(square, [1, 2, 3, 4])
    assert result == [1, 4, 9, 16]
    
    # Test case with a different mapper function and a list of strings
    def to_uppercase(s):
        return s.upper()
    
    result = curried_map(to_uppercase, ['hello', 'world'])
    assert result == ['HELLO', 'WORLD']

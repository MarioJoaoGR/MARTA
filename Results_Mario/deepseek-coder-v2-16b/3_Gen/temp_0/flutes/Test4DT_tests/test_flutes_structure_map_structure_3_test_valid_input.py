
import pytest
from typing import Callable, Collection, TypeVar
from flutes.structure import map_structure

T = TypeVar('T')
R = TypeVar('R')

def test_valid_input():
    def square(x):
        return x ** 2
    
    # Test with list
    assert map_structure(square, [1, 2, 3]) == [1, 4, 9]
    
    # Test with tuple
    assert map_structure(square, (1, 2, 3)) == (1, 4, 9)
    
    # Test with dictionary
    assert map_structure(square, {'a': 1, 'b': 2}) == {'a': 1, 'b': 4}
    
    # Test with set
    assert map_structure(square, {1, 2, 3}) == {1, 4, 9}

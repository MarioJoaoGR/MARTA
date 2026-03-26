
import pytest
from flutes.structure import map_structure
from typing import Callable, Collection, TypeVar

T = TypeVar('T')
R = TypeVar('R')

def test_map_structure():
    # Define a simple function to use for mapping
    def square(x: int) -> int:
        return x ** 2

    # Test with a list
    assert map_structure(square, [1, 2, 3]) == [1, 4, 9]
    
    # Test with a tuple
    assert map_structure(square, (1, 2, 3)) == (1, 4, 9)
    
    # Test with a dictionary
    assert map_structure(square, {'a': 1, 'b': 2}) == {'a': 1, 'b': 4}
    
    # Test with a set
    assert map_structure(square, {1, 2, 3}) == {1, 4, 9}


import pytest
from typing import Callable, Collection, TypeVar
from collections import namedtuple

T = TypeVar('T')
R = TypeVar('R')

# Import the function from its module
from flutes.structure import map_structure

def test_map_structure_list():
    def square(x):
        return x ** 2
    
    numbers = [1, 2, 3, 4, 5]
    expected = [1, 4, 9, 16, 25]
    result = map_structure(square, numbers)
    assert result == expected

def test_map_structure_tuple():
    def square(x):
        return x ** 2
    
    numbers = (1, 2, 3, 4, 5)
    expected = [1, 4, 9, 16, 25]
    result = map_structure(square, numbers)
    assert list(result) == expected  # Simplified assertion

def test_map_structure_dict():
    def square(x):
        return x ** 2
    
    numbers = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    expected = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    result = map_structure(square, numbers)
    assert dict(result) == expected  # Simplified assertion

def test_map_structure_set():
    def square(x):
        return x ** 2
    
    numbers = {1, 2, 3, 4, 5}
    expected = {1, 4, 9, 16, 25}
    result = map_structure(square, numbers)
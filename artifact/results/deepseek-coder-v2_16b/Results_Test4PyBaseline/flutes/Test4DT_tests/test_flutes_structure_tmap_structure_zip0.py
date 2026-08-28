
import pytest
from typing import Callable, Sequence, Collection
from collections import namedtuple

# Import the function from its module
from flutes.structure import map_structure_zip

def test_map_structure_zip_basic():
    def add(a, b):
        return a + b
    
    result = map_structure_zip(add, [[1, 2], [3, 4]])
    assert result == [4, 6]

def test_map_structure_zip_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    
    def add(a, b):
        return a + b
    
    points = [Point(1, 2), Point(3, 4)]
    result = map_structure_zip(add, points)
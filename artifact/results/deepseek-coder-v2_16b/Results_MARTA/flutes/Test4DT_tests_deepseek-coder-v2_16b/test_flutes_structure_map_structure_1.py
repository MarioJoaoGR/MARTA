
import pytest
from flutes.structure import map_structure
from collections import namedtuple

# Define a transformation function for testing
def square(x):
    return x ** 2

# Test cases for map_structure with different types of input objects

def test_map_structure_list():
    nested_list = [1, 2, 3, 4, 5]
    transformed_list = map_structure(square, nested_list)
    assert list(transformed_list) == [1, 4, 9, 16, 25]

def test_map_structure_tuple():
    nested_tuple = (1, 2, 3, 4, 5)
    transformed_tuple = map_structure(square, nested_tuple)
    assert tuple(transformed_tuple) == (1, 4, 9, 16, 25)

def test_map_structure_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    nested_namedtuple = Point(1, 2)
    transformed_namedtuple = map_structure(square, nested_namedtuple)
    assert transformed_namedtuple == Point(x=1, y=4)

def test_map_structure_dict():
    nested_dict = {1: 2, 3: 4}
    transformed_dict = map_structure(square, nested_dict)
    assert dict(transformed_dict) == {1: 4, 3: 16}

def test_map_structure_set():
    nested_set = {1, 2, 3, 4, 5}
    transformed_set = map_structure(square, nested_set)
    assert set(transformed_set) == {1, 4, 9, 16, 25}

def test_map_structure_primitive():
    value = 3
    transformed_value = map_structure(square, value)
    assert transformed_value == 9

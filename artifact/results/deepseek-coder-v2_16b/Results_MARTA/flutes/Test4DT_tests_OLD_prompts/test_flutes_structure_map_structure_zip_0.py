
import pytest
from flutes.structure import map_structure_zip
from typing import Callable, Collection, Sequence

# Define a sample function to be used with map_structure_zip
def add(a, b):
    return a + b

# Test for valid input where all objects have identical structures
def test_valid_input():
    objs = [[1, 2], [3, 4]]
    result = map_structure_zip(add, objs)
    assert result == [4, 6]

# Test for valid input with OrderedDict
def test_valid_input_ordereddict():
    from collections import OrderedDict
    objs = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    result = map_structure_zip(lambda x, y: x * y, objs)
    assert result == {'a': 3, 'b': 8}

# Test for valid input with tuples
def test_valid_input_tuples():
    objs = [(1, 2), (3, 4)]
    result = map_structure_zip(lambda x, y: x + y, objs)
    assert result == (4, 6)

# Test for invalid input where structures cannot be mapped directly
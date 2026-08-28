
import pytest
from flutes.structure import map_structure_zip

def add(a, b):
    return a + b

# Test case for valid input where objects have identical structures
def test_map_structure_zip_valid():
    objs = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    result = map_structure_zip(add, objs)
    assert result == {'a': 4, 'b': 6}

# Test case for invalid input where objects do not have identical structures
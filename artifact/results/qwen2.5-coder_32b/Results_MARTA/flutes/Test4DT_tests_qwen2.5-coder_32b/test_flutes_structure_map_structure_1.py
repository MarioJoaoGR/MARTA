
import pytest
from flutes.structure import map_structure

def test_map_structure_basic():
    # Test basic functionality with a simple list
    result = map_structure(lambda x: x * 2, [1, 2, [3, 4]])
    assert result == [2, 4, [6, 8]], "List elements should be doubled"

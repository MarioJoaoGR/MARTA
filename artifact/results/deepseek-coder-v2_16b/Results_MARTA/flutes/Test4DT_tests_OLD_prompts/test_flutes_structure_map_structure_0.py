
import pytest
from typing import Callable, Collection, NamedTuple
from flutes.structure import map_structure

# Define the transformation function
def square(x):
    return x ** 2

# Define a namedtuple for testing
class Point(NamedTuple):
    x: int
    y: int

# Test cases for map_structure function
@pytest.mark.parametrize("obj, expected", [
    ([1, 2, 3], [1, 4, 9]),
    ((1, 2, 3), (1, 4, 9)),
    ({1: 2, 3: 4}, {1: 4, 3: 16}),
    (Point(x=1, y=2), Point(x=1, y=4))
])
def test_map_structure_basic(obj, expected):
    result = map_structure(square, obj)
    assert result == expected

# Test case for empty collection

import pytest
from typing import Callable, Collection

# Assuming map_structure is defined in a module named 'flutes.structure'
from flutes.structure import map_structure

def square(x):
    return x ** 2

test_data = [
    ([1, 2, 3], [1, 4, 9]),
    ((1, 2, 3), (1, 4, 9)),
    ({'a': 1, 'b': 2}, {'a': 1, 'b': 4}),
    ({1, 2, 3}, {1, 4, 9})
]

@pytest.mark.parametrize("input_obj, expected", test_data)
def test_valid_inputs(input_obj, expected):
    result = map_structure(square, input_obj)
    assert result == expected

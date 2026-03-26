
import pytest
from flutes.iterator import scanl

def add(x, y):
    return x + y

@pytest.mark.parametrize("iterable, expected", [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([5, -1, 2], [5, 4, 6]),
    ([0, 0, 0], [0, 0, 0]),
    ([10], [10]),
    ([-1, -2, -3, -4], [-1, -3, -6, -10])
])
def test_scanl_valid_inputs(iterable, expected):
    result = list(scanl(add, iterable))
    assert result == expected

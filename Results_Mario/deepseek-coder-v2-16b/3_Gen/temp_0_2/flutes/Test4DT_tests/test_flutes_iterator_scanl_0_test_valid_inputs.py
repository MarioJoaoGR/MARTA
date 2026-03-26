
import pytest
from flutes.iterator import scanl

# Define a simple add function for testing
def add(x, y):
    return x + y

# Test data
test_data = [
    (add, [5, -1, 2], 10, [10, 15, 14, 16])
]

@pytest.mark.parametrize("func, iterable, initial, expected", test_data)
def test_valid_inputs(func, iterable, initial, expected):
    result = list(scanl(func, iterable, initial))
    assert result == expected

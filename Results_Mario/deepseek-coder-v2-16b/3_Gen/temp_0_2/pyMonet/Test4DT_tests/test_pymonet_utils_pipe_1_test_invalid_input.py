
from pymonet.utils import pipe
import pytest

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

@pytest.mark.parametrize("value, expected", [
    (5, 12),          # Test with a valid input and expected output
    ("test", TypeError)  # Test with an invalid input type to trigger a TypeError
])
def test_invalid_input(value, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            pipe(value, add_one, multiply_by_two)
    else:
        assert pipe(value, add_one, multiply_by_two) == expected

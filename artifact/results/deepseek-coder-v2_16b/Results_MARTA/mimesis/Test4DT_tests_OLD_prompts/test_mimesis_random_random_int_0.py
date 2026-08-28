
import pytest
from unittest.mock import patch, MagicMock
import random

def random_int(a: int, b: int) -> int:
    """Generates a random integer between `a` and `b`, inclusive."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    if a > b:
        raise ValueError("First argument must be less than the second argument")
    return random.randint(a, b)

# Test valid input scenario
def test_valid_input():
    with patch('random.randint', return_value=3):
        assert random_int(1, 5) == 3

# Test edge cases scenario
def test_edge_cases():
    with pytest.raises(TypeError):
        random_int(None, None)
    with patch('random.randint', return_value=1):
        assert random_int(1, 1) == 1

# Test invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        random_int('a', 'b')

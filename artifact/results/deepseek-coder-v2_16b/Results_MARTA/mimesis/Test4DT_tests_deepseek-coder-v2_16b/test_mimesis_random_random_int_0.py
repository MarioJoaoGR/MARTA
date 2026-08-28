
import pytest
from unittest.mock import patch
import random

def random_int(a: int, b: int) -> int:
    """Generates a random integer between `a` and `b`, inclusive."""
    b = b - a
    return int(random.random() * b) + a

@pytest.fixture
def rng():
    random.seed(0)
    return random.Random()

# Test scenario 1: test_valid_input
def test_valid_input(rng):
    with patch('random.random', side_effect=[0.5]):
        assert random_int(1, 5) == 3

# Test scenario 2: test_edge_case
def test_edge_case(rng):
    with patch('random.random', side_effect=[0.0, 1.0]):
        assert random_int(1, 5) == 1 or random_int(1, 5) == 5

# Test scenario 3: test_invalid_input
def test_invalid_input():
    with pytest.raises(TypeError):
        random_int("a", "b")

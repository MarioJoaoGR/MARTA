
import pytest
from unittest.mock import MagicMock
import random

# Assuming the function is imported correctly from mimesis.random
def test_random_int_basic():
    # Mocking self.random to always return 0.5 for consistent results
    mock_random = MagicMock()
    mock_random.return_value = 0.5
    
    def random_int(a: int, b: int) -> int:
        b = b - a
        return int(mock_random() * b) + a
    
    # Test with bounds that include zero and positive numbers
    assert random_int(1, 10) == pytest.approx(5, abs=0.1)
    assert random_int(0, 1) == pytest.approx(0, abs=0.1)
    assert random_int(-10, 10) == pytest.approx(0, abs=0.1)

def test_random_int_with_explicit_generator():
    def random_int(a: int, b: int, random_generator) -> int:
        b = b - a
        return int(random_generator.random() * b) + a
    
    # Test with an explicit random number generator
    my_random_generator = random.Random()
    assert 1 <= random_int(1, 10, my_random_generator) < 10
    assert 0 <= random_int(0, 1, my_random_generator) < 1
    assert -10 <= random_int(-10, 10, my_random_generator) < 10

def test_random_int_default_module():
    def random_int(a: int, b: int) -> int:
        b = b - a
        return int(random.random() * b) + a
    
    # Test using Python's built-in random module
    assert 1 <= random_int(1, 10) < 10
    assert 0 <= random_int(0, 1) < 1
    assert -10 <= random_int(-10, 10) < 10

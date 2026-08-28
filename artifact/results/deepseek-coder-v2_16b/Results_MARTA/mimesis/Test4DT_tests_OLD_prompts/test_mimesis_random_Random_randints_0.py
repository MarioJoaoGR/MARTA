
import pytest
from mimesis.random import Random
from unittest.mock import patch

# Test 1: Generate 3 random integers between 1 and 100
def test_randints_valid():
    rand_gen = Random()
    with patch('mimesis.random.Random.random', return_value=0.5):
        result = rand_gen.randints(amount=3, a=1, b=100)
        assert len(result) == 3
        for num in result:
            assert isinstance(num, int)
            assert 1 <= num <= 100

# Test 2: Attempt to generate 0 random integers (should raise ValueError)
def test_randints_invalid():
    rand_gen = Random()
    with pytest.raises(ValueError):
        rand_gen.randints(amount=0, a=1, b=100)

# Test 3: Generate 5 random integers between 1 and 100
def test_randints_more():
    rand_gen = Random()
    with patch('mimesis.random.Random.random', side_effect=[0.1, 0.2, 0.3, 0.4, 0.5]):
        result = rand_gen.randints(amount=5, a=1, b=100)
        assert len(result) == 5
        for num in result:
            assert isinstance(num, int)
            assert 1 <= num <= 100

# Test 4: Generate random integers between -50 and 50
def test_randints_negative():
    rand_gen = Random()
    with patch('mimesis.random.Random.random', side_effect=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]):
        result = rand_gen.randints(amount=7, a=-50, b=50)
        assert len(result) == 7
        for num in result:
            assert isinstance(num, int)
            assert -50 <= num <= 50

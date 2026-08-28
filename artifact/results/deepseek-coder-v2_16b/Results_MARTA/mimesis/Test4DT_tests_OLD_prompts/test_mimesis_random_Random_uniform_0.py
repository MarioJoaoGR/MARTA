
import pytest
from unittest.mock import patch
from mimesis.random import Random as MimesisRandom

# Test for the uniform method of the Mimesis Random class
def test_mimesis_random_uniform():
    with patch('mimesis.random.Random.random', return_value=0.5):
        rand = MimesisRandom()
        result = rand.uniform(1, 2)
        assert pytest.approx(result, 0.000000000000001) == 1.5

# Test for the uniform method with different precision
def test_mimesis_random_uniform_precision():
    with patch('mimesis.random.Random.random', return_value=0.5):
        rand = MimesisRandom()
        result = rand.uniform(1, 2, precision=3)
        assert pytest.approx(result, 0.001) == 1.5

# Test for the uniform method with different values of 'a' and 'b'
def test_mimesis_random_uniform_different_values():
    with patch('mimesis.random.Random.random', return_value=0.5):
        rand = MimesisRandom()
        result = rand.uniform(1, 3)
        assert pytest.approx(result, 0.000000000000001) == 2.0

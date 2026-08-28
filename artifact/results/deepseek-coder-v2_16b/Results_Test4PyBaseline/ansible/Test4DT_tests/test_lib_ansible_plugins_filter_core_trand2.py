
import pytest
from random import SystemRandom, Random
from ansible.plugins.filter.core import rand
from ansible.errors import AnsibleFilterError

# Test generating a random integer within a specified range with default start and step values
def test_rand_integer_range_default():
    r = SystemRandom()
    result = rand(None, 10)
    assert isinstance(result, int), "Expected an integer"
    assert 0 <= result < 10, "Result should be in the range [0, 10)"

# Test selecting a random element from a list
def test_rand_list():
    r = SystemRandom()
    result = rand(None, [1, 2, 3, 4, 5])
    assert result in [1, 2, 3, 4, 5], "Result should be one of the elements in the list"

# Test generating a random integer with custom start and step values
def test_rand_custom_start_step():
    r = SystemRandom()
    result = rand(None, 20, start=0, step=2)
    assert isinstance(result, int), "Expected an integer"
    assert 0 <= result < 20, "Result should be in the range [0, 20)"
    assert result % 2 == 0, "Result should be an even number"

# Test generating a random integer using a specific seed for reproducibility
def test_rand_seed():
    r = Random()
    r.seed(42)
    result1 = rand(None, 100, seed=42)
    
    # Reset the seed and generate another number to ensure reproducibility
    r.seed(42)
    result2 = rand(None, 100, seed=42)
    
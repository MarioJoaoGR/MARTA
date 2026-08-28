
import pytest
from pymonet.utils import compose

# Test valid case where composition of functions results in the correct value

# Test edge case where the composition results in an incorrect value
def test_invalid_case():
    def add_one(x): return x + 1
    def multiply_by_two(x): return x * 2
    
    result = compose(5, add_one, multiply_by_two)
    assert result != 10  # This should fail if the assertion is incorrect
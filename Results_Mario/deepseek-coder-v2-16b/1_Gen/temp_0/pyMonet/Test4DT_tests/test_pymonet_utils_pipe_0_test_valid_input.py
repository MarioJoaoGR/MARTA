
import pytest
from pymonet.utils import pipe

def test_valid_input():
    def add_one(x):
        return x + 1
    
    def multiply_by_two(x):
        return x * 2
    
    # Test with a single function
    assert pipe(5, add_one) == 6
    
    # Test with multiple functions
    assert pipe(5, add_one, multiply_by_two) == 12
    
    # Test with no functions (should return the value itself)
    assert pipe(5) == 5

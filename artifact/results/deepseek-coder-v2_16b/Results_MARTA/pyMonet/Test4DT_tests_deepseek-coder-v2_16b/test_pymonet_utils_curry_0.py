
import pytest
from pymonet.utils import curry

# Test valid input where x is a callable function
def test_valid_input():
    def add(a, b):
        return a + b
    
    curried_add = curry(add)
    assert curried_add(1)(2) == 3

# Test specifying the number of arguments
def test_specify_args_count():
    def add(a, b):
        return a + b
    
    curried_add = curry(add, args_count=2)
    assert curried_add(1)(2) == 3

# Test invalid input where x is None
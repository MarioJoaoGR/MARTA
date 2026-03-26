
import pytest
from pymonet.utils import curry

def test_valid_inputs():
    # Define a simple function to be curried
    def add(a, b):
        return a + b
    
    # Currying the function without specifying args_count
    curried_add = curry(add)
    
    # Test currying with one argument
    assert curried_add(1)(2) == 3
    
    # Test currying directly with both arguments
    curried_add_with_args_count = curry(add, args_count=2)
    assert curried_add_with_args_count(1)(2) == 3

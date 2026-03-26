
import pytest
from pymonet.utils import curry

def test_valid_inputs():
    def add(a, b):
        return a + b
    
    curried_add = curry(add)
    assert curried_add(1)(2) == 3
    
    curried_add_with_count = curry(add, args_count=2)
    assert curried_add_with_count(1, 2) == 3

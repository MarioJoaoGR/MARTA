# Module: pymonet.utils
import pytest
from typing import Callable, List, Tuple

# Import the function from its module
from pymonet.utils import cond

def is_even(n): 
    return n % 2 == 0

def double(n): 
    return n * 2

def triple(n): 
    return n * 3

# Test cases for the `cond` function
@pytest.mark.parametrize("condition_list, args, expected", [
    ([(is_even, double), (lambda x: x > 5, triple)], (4,), 8),
    ([(is_even, double), (lambda x: x > 5, triple)], (7,), 21),
])
def test_cond(condition_list, args, expected):
    result = cond(condition_list)(*args)
    assert result == expected

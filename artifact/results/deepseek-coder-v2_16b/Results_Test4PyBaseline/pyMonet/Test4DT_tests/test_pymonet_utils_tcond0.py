
import pytest
from typing import Callable, List, Tuple
from pymonet.utils import cond

# Example test cases for the `cond` function

def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def triple(n):
    return n * 3

@pytest.mark.parametrize("args, expected", [
    ((4,), 8),       # Test with an even number, should use the double function
    ((7,), 21),      # Test with a number greater than 5, should use the triple function
])
def test_cond_basic(args, expected):
    cond_func = cond([(is_even, double), (lambda x: x > 5, triple)])
    assert cond_func(*args) == expected

@pytest.mark.parametrize("args, expected", [
    ((4,), 8),       # Test with an even number, should use the double function
    ((-1,), 2),      # Test with a negative number, should use the add_one function
    ((3,), 9),       # Test with a multiple of 3, should use the triple function
])
def test_cond_different_conditions(args, expected):
    cond_func = cond([(is_even, double), (lambda x: x > 5, triple), (lambda x: x % 3 == 0, lambda x: x * 3)])
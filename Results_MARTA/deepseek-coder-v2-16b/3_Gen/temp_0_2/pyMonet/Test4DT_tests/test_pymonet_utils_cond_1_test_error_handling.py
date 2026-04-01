
import pytest
from typing import Callable, List, Tuple
from pymonet.utils import cond

def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def triple(n):
    return n * 3

@pytest.mark.parametrize("args, expected", [
    (4, 8),   # is_even returns True for 4, so it should use the double function
    (7, 21),  # lambda x: x > 5 returns True for 7, so it should use the triple function
])
def test_cond(args, expected):
    cond_func = cond([(is_even, double), (lambda x: x > 5, triple)])
    assert cond_func(args) == expected

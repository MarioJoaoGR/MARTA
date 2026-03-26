
import pytest
from typing import Callable, List, Tuple
from pymonet.utils import cond

# Assuming you have some condition and execute functions defined elsewhere
def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def triple(n):
    return n * 3

@pytest.mark.parametrize("condition_list, args, expected", [
    ([(is_even, double), (lambda n: n > 5, triple)], (4,), 8),
    ([(is_even, double), (lambda n: n > 5, triple)], (7,), 21),
])
def test_cond(condition_list, args, expected):
    cond_func = cond(condition_list)
    assert cond_func(*args) == expected

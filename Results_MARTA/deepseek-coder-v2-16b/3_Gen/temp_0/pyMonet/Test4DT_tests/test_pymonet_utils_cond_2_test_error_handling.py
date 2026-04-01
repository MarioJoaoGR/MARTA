
import pytest
from pymonet.utils import cond

def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def triple(n):
    return n * 3

@pytest.mark.parametrize("args, expected", [
    (4, 8),       # Test with even number
    (7, 21),      # Test with number greater than 5
    (3, None)     # Test without a matching condition
])
def test_cond(args, expected):
    cond_func = cond([
        (is_even, double),
        (lambda n: n > 5, triple)
    ])
    assert cond_func(args) == expected

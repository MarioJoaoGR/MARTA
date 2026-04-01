
import pytest
from pymonet.utils import cond

def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

def triple(n):
    return n * 3

@pytest.fixture
def c():
    return cond([(is_even, double), (lambda x: x > 5, triple)])

def test_valid_input(c):
    assert c(4) == 8  # is_even returns True for 4, so it should use the double function
    assert c(7) == 21  # lambda x: x > 5 returns True for 7, so it should use the triple function
    assert c(3) == None  # Neither condition is met for 3, so it should return the default value or raise an error if not handled

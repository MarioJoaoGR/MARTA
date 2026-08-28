
import pytest
from pymonet.utils import cond


def test_cond_with_multiple_conditions():
    def is_even(n):
        return n % 2 == 0
    
    def double(n):
        return n * 2
    
    cond_func = cond([
        (is_even, double),
        (lambda n: n > 5, lambda n: n * 3),
        (lambda n: n < -10, lambda n: -n)
    ])
    
    assert cond_func(4) == 8
    assert cond_func(7) == 21
    assert cond_func(-12) == -12

def test_cond_with_multiple_conditions():
    def is_multiple_of_three(n):
        return n % 3 == 0
    
    def triple(n):
        return n * 3
    
    cond_func = cond([
        (lambda n: n % 2 == 0, lambda n: n * 2),
        (is_multiple_of_three, triple),
        (lambda n: n > 10, lambda n: n + 5)
    ])
    
    assert cond_func(9) == 27
    assert cond_func(8) == 16
    assert cond_func(15) == 45
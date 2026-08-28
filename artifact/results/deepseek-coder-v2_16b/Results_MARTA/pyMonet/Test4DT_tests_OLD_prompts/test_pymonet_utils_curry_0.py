
import pytest
from pymonet.utils import curry

def test_curry_basic():
    def add(a, b):
        return a + b
    
    curried_add = curry(add)
    assert curried_add(1)(2) == 3

def test_curry_specified_args_count():
    def add(a, b):
        return a + b
    
    curried_add = curry(add, args_count=2)
    assert curried_add(1)(2) == 3

def test_curry_more_than_two_args():
    def multiply(a, b, c):
        return a * b * c
    
    curried_multiply = curry(multiply)
    assert curried_multiply(2)(3)(4) == 24


import pytest
from pymonet.utils import curry


def test_curry_partial_application():
    def multiply(a, b):
        return a * b
    
    curried_multiply = curry(multiply, 2)
    assert curried_multiply(3)(6) == 18

def test_curry_with_more_arguments():
    def subtract(a, b, c):
        return a - b - c
    
    curried_subtract = curry(subtract, 3)
    assert curried_subtract(5)(2)(3) == 0
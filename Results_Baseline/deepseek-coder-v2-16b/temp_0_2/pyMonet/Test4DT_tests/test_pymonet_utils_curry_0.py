
import pytest
from pymonet.utils import curry

# Test cases for the curry function

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

def test_curry_lambda():
    curried_lambda = curry(lambda x, y: x + y)
    assert curried_lambda(1)(2) == 3

def test_curry_multiple_args():
    def multiply_and_add(a, b, c):
        return (a * b) + c
    
    curried_multiply_and_add = curry(multiply_and_add)
    assert curried_multiply_and_add(2)(3)(4) == 10

def test_curry_method():
    class Calculator:
        def add(self, a, b):
            return a + b
    
    calc = Calculator()
    curried_add = curry(calc.add)
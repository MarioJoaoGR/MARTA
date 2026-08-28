
import pytest
from pymonet.utils import curry

# Helper functions to create simple curried functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

# Test cases for curry function
def test_curry_without_args_count():
    curried_add = curry(add)
    assert curried_add(1)(2) == 3

def test_curry_with_specified_args_count():
    curried_multiply = curry(multiply, args_count=2)
    assert curried_multiply(3)(4) == 12

def test_curry_lambda():
    curried_lambda = curry(lambda x, y: x + y)
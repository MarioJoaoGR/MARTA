
import pytest
from functools import reduce
from pymonet.utils import pipe

# Helper functions for testing
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def test_pipe_basic():
    result = pipe(5, add_one, multiply_by_two)
    assert result == 12

def test_pipe_lambda():
    result = pipe(3, lambda x: x + 2, lambda x: x * 3)
    assert result == 15

def test_pipe_chaining():
    def add_five(x):
        return x + 5

    def subtract_three(x):
        return x - 3

    result = pipe(7, add_one, multiply_by_two, add_five, subtract_three)
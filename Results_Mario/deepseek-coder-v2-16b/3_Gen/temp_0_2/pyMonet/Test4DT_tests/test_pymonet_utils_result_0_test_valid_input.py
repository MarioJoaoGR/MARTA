
import pytest

def is_even(n):
    return n % 2 == 0

def square(n):
    return n * n

condition_list = [(is_even, square)]

def result(*args):
    for (condition_function, execute_function) in condition_list:
        if condition_function(*args):
            return execute_function(*args)

def test_valid_input():
    assert result(4) == 16
    assert result(2) == 4

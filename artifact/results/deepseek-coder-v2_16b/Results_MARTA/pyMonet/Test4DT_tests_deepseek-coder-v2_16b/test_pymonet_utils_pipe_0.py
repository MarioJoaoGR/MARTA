
import pytest
from functools import reduce

# Assuming add_one and multiply_by_two are defined as per the provided examples
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def pipe(value, *functions):
    """
    Perform left-to-right function composition.

    :param value: argument of first applied function
    :type value: Any
    :param functions: list of functions to applied from left-to-right
    :type functions: List[Function]
    :returns: result of all functions
    :rtype: Any
    """
    return reduce(lambda current_value, function: function(current_value), functions, value)

# Test cases
def test_valid_case_single_function():
    def add_one(x):
        return x + 1
    result = pipe(5, add_one)
    assert result == 6

def test_valid_case_multiple_functions():
    def multiply_by_two(x):
        return x * 2
    def subtract_three(x):
        return x - 3
    result = pipe(10, multiply_by_two, subtract_three)
    assert result == 17

def test_valid_case_lambda_and_predefined():
    result = pipe(20, lambda x: x + 5, add_one)
    assert result == 26

def test_edge_case_none_input():
    with pytest.raises(TypeError):
        result = pipe(None, add_one)

def test_edge_case_empty_functions():
    result = pipe(5)
    assert result == 5

def test_error_case_invalid_function():
    def add_one(x):
        return x + 1
    with pytest.raises(TypeError):
        result = pipe(5, 'not_a_function', add_one)

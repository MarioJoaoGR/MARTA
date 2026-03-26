
import pytest
from functools import reduce

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
    return reduce(
        lambda current_value, function: function(current_value),
        functions,
        value
    )

def test_valid_input():
    def add_one(x): return x + 1
    def multiply_by_two(x): return x * 2
    
    assert pipe(5, add_one, multiply_by_two) == 12
    assert pipe(3, add_one, multiply_by_two) == 8
    assert pipe(0, add_one, multiply_by_two) == 2
    assert pipe(7, add_one, multiply_by_two) == 16

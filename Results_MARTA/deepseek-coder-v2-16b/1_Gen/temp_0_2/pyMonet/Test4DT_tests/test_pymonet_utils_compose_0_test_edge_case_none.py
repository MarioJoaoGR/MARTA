
import pytest
from functools import reduce

def compose(value, *functions):
    """
    Perform right-to-left function composition.

    :param value: argument of first applied function
    :type value: Any
    :param functions: list of functions to applied from right-to-left
    :type functions: List[Function]
    :returns: result of all functions
    :rtype: Any
    """
    return reduce(
        lambda current_value, function: function(current_value),
        functions[::-1],
        value
    )

def test_edge_case_none():
    def add_one(x): return x + 1 if x is not None else None
    def multiply_by_two(x): return x * 2 if x is not None else None
    
    # Test with initial value None
    assert compose(None, add_one, multiply_by_two) is None

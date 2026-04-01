
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

def test_invalid_input():
    with pytest.raises(TypeError):
        pipe("not a function", 1)


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

def test_invalid_input():
    with pytest.raises(TypeError):
        compose(5, "not a function", lambda x: x + 1)

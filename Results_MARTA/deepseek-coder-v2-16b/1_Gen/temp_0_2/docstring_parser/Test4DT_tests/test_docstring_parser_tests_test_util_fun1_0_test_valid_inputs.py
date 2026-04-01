
import pytest

def fun1(arg_a, arg_b, arg_c, arg_d):
    """
    Perform a check on the provided arguments to ensure they are all present and not None.
    
    Args:
        arg_a (any): The first argument to be checked for presence.
        arg_b (any): The second argument to be checked for presence.
        arg_c (any): The third argument to be checked for presence.
        arg_d (any): The fourth argument to be checked for presence.
    
    Raises:
        AssertionError: If any of the arguments are not provided, an assertion error is raised.
    
    Examples:
        >>> fun1(True, 123, "string", [1, 2, 3])
        This will pass as all four arguments are present and not None.
        
        >>> fun1(None, 123, "string", [1, 2, 3])
        This will raise an AssertionError because arg_a is None.
    
    """
    assert arg_a and arg_b and arg_c and arg_d

def test_valid_inputs():
    fun1(True, 123, "string", [1, 2, 3])
    with pytest.raises(AssertionError):
        fun1(None, 123, "string", [1, 2, 3])

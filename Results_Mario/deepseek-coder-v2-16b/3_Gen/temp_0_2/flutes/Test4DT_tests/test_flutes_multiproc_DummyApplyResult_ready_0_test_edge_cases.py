
import pytest
from flutes.multiproc import DummyApplyResult

def dummy_apply_result(value):
    """
    Creates a `DummyApplyResult` instance with the given value.

    This function initializes an instance of `DummyApplyResult` with the provided value. The `DummyApplyResult` class is assumed to be defined elsewhere in the codebase, and it should have at least one method called `__init__`.

    Parameters:
        value (T): The value to be stored in the `DummyApplyResult` instance. This parameter must be of type T, where T can be any valid Python type.

    Returns:
        DummyApplyResult[T]: An instance of `DummyApplyResult` with the specified value.

    Example:
        To create a `DummyApplyResult` instance with an integer value of 42, you would call the function as follows:
        
        >>> result = dummy_apply_result(42)
        >>> print(result._value)  # Output will be 42

        Similarly, to create one with a string value "hello", you can do:
        
        >>> result = dummy_apply_result("hello")
        >>> print(result._value)  # Output will be "hello"
    """
    return DummyApplyResult(value)

def test_edge_cases():
    # Test edge cases for the dummy apply result
    assert dummy_apply_result(None).ready() is True
    assert dummy_apply_result("string").ready() is True
    assert dummy_apply_result(42).ready() is True

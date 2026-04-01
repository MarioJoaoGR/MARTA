
from pymonet.either import Either, Left, Right

class Either:
    """
    The Either type represents values with two possibilities: A value of type Either[A, B] is either Left[A] or Right[B].
    
    Parameters:
        value (T): The value to be stored in the Either. This can be of any type `T`.
        
    Examples:
        >>> left_value = Either(Left("error message"))  # Creating a Left instance with an error message
        >>> right_value = Either(Right(42))            # Creating a Right instance with the value 42
        
        In this example, `left_value` is of type Left["error message"] and contains an error message.
        Similarly, `right_value` is of type Right[int] and contains the integer value 42.
    
    Returns:
        None: The function does not return a value directly but initializes an instance with the provided value.
        
    Usage:
        You can use Either to handle cases where you want to represent values that could be one of two types, providing flexibility in handling different outcomes.
    
    Transform Validation to Either.

    This function converts a `Validation` instance into an `Either` monad. If the `Validation` has no errors (i.e., it is successful), it returns a `Right` with the previous value. Otherwise, it returns a `Left` containing the list of errors.

    :returns: Right[A] | Left[E] where A is the type of the validation's value and E is the type of the validation's errors.
    :rtype: Union[Right[A], Left[E]]
    """
    def __init__(self, value: T) -> None:
        self.value = value

    def is_right(self):
        return isinstance(self.value, Right)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Either):
            return False
        return (isinstance(self.value, type(other.value)) and self.value == other.value and self.is_right() == other.is_right())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either___eq___0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_edge_cases.py:4:0: E0102: class already defined line 2 (function-redefined)
pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___0_test_edge_cases.py:31:30: E0602: Undefined variable 'T' (undefined-variable)


"""
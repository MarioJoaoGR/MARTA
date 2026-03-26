
from pymonet.either import Either, Left, Right
from pymonet.lazy import Lazy

class Either:
    """
    The Either type represents values with two possibilities: A value of type Either[A, B] is either Left[A] or Right[B].
    
    Parameters:
        value (T): The value to be stored in the Either. It can be of any type and will be encapsulated within an instance of Either.
        
    Examples:
        >>> left_value = Either(Left("error message"))  # Creating a Left variant with an error message
        >>> right_value = Either(Right(42))  # Creating a Right variant with the value 42
        
    Methods:
        to_lazy(): Transforms the Either to a Lazy monad, where the function returned by the lazy evaluation will retrieve the value stored in the Either. This is useful for handling values that may not be present or for deferring computation until it is actually needed.
    
    Returns:
        Lazy[Function() -> T]: A Lazy monad encapsulating a function that returns the value of the Either when called.
    """
    def __init__(self, value: T) -> None:
        self.value = value

    def to_lazy(self):
        """
        Transform Either to Try.

        :returns: Lazy monad with function returning previous value
        :rtype: Lazy[Function() -> A]
        """
        from pymonet.lazy import Lazy

        return Lazy(lambda: self.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_to_lazy_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Either_to_lazy_0_test_valid_input.py:5:0: E0102: class already defined line 2 (function-redefined)
pyMonet/Test4DT_tests/test_pymonet_either_Either_to_lazy_0_test_valid_input.py:22:30: E0602: Undefined variable 'T' (undefined-variable)


"""
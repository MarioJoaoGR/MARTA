
class Maybe:
    """
    Represents a container that may or may not have a value, encapsulating the concept of nullability.
    
    Attributes:
        is_nothing (bool): Indicates whether the Maybe contains no value.
        value (T): The contained value if `is_nothing` is False.
        
    Methods:
        __init__(self, value: T, is_nothing: bool) -> None: Initializes a new instance of Maybe.
            - Parameters:
                value (T): The value to be stored in the Maybe container.
                is_nothing (bool): A boolean indicating whether the container should be empty or contain a value.
        __eq__(self, other: object) -> bool: Compares two Maybe instances for equality.
            - Parameters:
                other (object): The instance to compare with.
            - Returns:
                bool: True if both instances are of type Maybe and have the same `is_nothing` status and value; otherwise False.
    
    Examples:
        >>> maybe1 = Maybe(value=42, is_nothing=False)  # A Maybe container with a value of 42
        >>> maybe2 = Maybe(value=None, is_nothing=True)  # A Maybe container with no value
        >>> print(maybe1.is_nothing, maybe1.value)  # Output: False 42
        >>> print(maybe2.is_nothing, maybe2.value)  # Output: True None
        >>> another_maybe = Maybe(value=42, is_nothing=False)
        >>> print(maybe1 == another_maybe)  # Output: True (because both have the same value and are not nothing)
    """
    def __init__(self, value: T, is_nothing: bool) -> None:
        if not isinstance(is_nothing, bool):
            raise TypeError("is_nothing must be a boolean")
        self.is_nothing = is_nothing
        if not is_nothing:
            self.value = value

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Maybe) and \
            self.is_nothing == other.is_nothing and \
            (self.is_nothing or self.value == other.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe___eq___1_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe___eq___1_test_invalid_inputs.py:29:30: E0602: Undefined variable 'T' (undefined-variable)


"""
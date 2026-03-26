
class Either:
    """
    The Either type represents values with two possibilities: A value of type Either[A, B] is either Left[A] or Right[B], but not both in the same time.
    
    Attributes:
        value (T): The value contained within the Either object.
        
    Methods:
        is_right(): Checks if the Either contains a Right value and returns True if it does, otherwise returns False.
    
    Examples:
        >>> either = Either(10)  # Creating an instance of Either with a value of 10
        >>> print(either.is_right())  # Output will be False since the value is not in a Right container
        
        >>> right_either = Either("Hello")  # Creating an instance of Either with a string value "Hello"
        >>> print(right_either.is_right())  # Output will be True since the value is in a Right container
    """
    def __init__(self, value: T) -> None:
        self.value = value
    
    def is_right(self):
        return isinstance(self.value, Right)
```

Now let's write the test case to check if `is_right` works correctly:

```python
from pymonet.either import Either, Right

def test_valid_input():
    # Test when the Either contains a Right value
    either = Either(Right("Hello"))
    assert either.is_right() is True

    # Test when the Either contains a Left value
    either = Either(Left("error message"))
    assert either.is_right() is False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_is_right_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Either_is_right_0_test_valid_input.py:26:8: E0001: Parsing failed: 'unterminated string literal (detected at line 26) (Test4DT_tests.test_pymonet_either_Either_is_right_0_test_valid_input, line 26)' (syntax-error)


"""
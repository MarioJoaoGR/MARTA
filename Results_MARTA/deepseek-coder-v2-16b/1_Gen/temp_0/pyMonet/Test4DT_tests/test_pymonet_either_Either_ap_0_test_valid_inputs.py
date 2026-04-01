
import pytest
from pymonet.either import Either, Left, Right

def test_valid_inputs():
    # Test cases for valid inputs
    left_value = Left("error message")
    right_value = Right(42)
    
    # Create a Left instance with a lambda function
    left_function = Left(lambda x: x + 1)
    
    # Applying the function inside the Left structure to self (which is not applicable here)
    result_left_to_left = left_value.ap(left_function)
    assert isinstance(result_left_to_left, Left)
    assert result_left_to_left.value == "error message"  # The function is not applicable to the value in Left

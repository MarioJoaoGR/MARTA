
from pymonet.either import Right, Left
import pytest

def test_Right_bind_with_error():
    right_instance = Right(42)  # Create an instance of Right with value 42
    result = right_instance.bind(lambda x: x * 2)  # Apply a lambda function that doubles the value
    assert result == 84  # Check if the result is as expected

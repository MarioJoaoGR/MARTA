
from pymonet.either import Right  # Assuming this is the correct module path
import pytest

def test_valid_input():
    right_instance = Right(42)  # Create a Right instance with value 42
    mapped_value = right_instance.bind(lambda x: x * 2)  # Apply the mapper function (doubling the value)
    assert mapped_value == 84  # Check if the result is as expected

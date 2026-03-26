
from pymonet.either import Left
import pytest

def test_valid_input():
    left_instance = Left(value=42)  # Create an instance of Left with a value
    result = left_instance.bind(lambda x: x + 1)  # Bind the lambda function to the value
    assert isinstance(result, Left)  # Ensure that the result is still a Left instance
    assert result.value == 42  # The value should remain unchanged

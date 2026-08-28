
import pytest
from pymonet.either import Left

# Test that checks if is_right method of Left returns False
def test_left_is_not_right():
    left_instance = Left("error message")
    assert not left_instance.is_right(), "Expected is_right to return False for a Left instance"

# Test that checks the initialization with an error message
def test_left_initialization_with_error_message():
    left_instance = Left("error message")
    assert left_instance.value == "error message", "Expected value to be 'error message' for a Left instance"

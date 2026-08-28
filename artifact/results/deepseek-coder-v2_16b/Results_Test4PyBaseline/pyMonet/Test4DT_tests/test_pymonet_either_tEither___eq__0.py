
import pytest
from pymonet.either import Either

# Test cases for the Either class initialization
def test_init():
    # Create a Left instance with a string value
    left_value = Either("error message")
    assert not left_value.is_right(), "Expected is_right() to be False for Left instances"
    assert left_value.value == "error message", f"Expected value to be 'error message', but got {left_value.value}"

    # Create a Right instance with an integer value
    right_value = Either(15)
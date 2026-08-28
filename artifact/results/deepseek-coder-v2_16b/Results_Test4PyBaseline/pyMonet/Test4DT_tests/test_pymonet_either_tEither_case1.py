
import pytest
from pymonet.either import Either

# Test cases for the Either class and its methods

def test_create_left_instance():
    left_value = Either("error message")  # Creates a Left instance with value "error message"
    assert not left_value.is_right(), "Expected is_right() to be False when creating a Left instance"
    result = left_value.case(lambda x: "Error handling {}".format(x), lambda x: "Successfully handled {}".format(x))
    assert result == "Error handling error message", f"Expected 'Error handling error message' but got {result}"

def test_create_right_instance():
    right_value = Either(15)  # Creates a Right instance with value 15
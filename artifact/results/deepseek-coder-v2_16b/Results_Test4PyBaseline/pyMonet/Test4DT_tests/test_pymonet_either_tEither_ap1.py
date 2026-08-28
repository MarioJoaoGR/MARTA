
import pytest
from pymonet.either import Either, Right, Left

# Test cases for the Either class
def test_either_creation():
    left_value = Either(10)  # Creates a Left instance with value 10
    assert not left_value.is_right(), "Expected is_right() to be False"
    
    right_value = Either("hello")  # Creates a Right instance with value "hello"
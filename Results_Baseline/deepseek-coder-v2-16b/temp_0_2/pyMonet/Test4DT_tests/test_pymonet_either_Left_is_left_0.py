
import pytest
from pymonet.either import Left, Right, Either

# Test initialization of Left instance
def test_left_initialization():
    left_value = Left("error message")
    assert left_value.is_left() == True
    assert left_value.is_right() == False

# Test mapping the contained value in Left
def test_left_map():
    left_value = Left("error message")
    mapped_left = left_value.map(lambda x: f"Error: {x}")
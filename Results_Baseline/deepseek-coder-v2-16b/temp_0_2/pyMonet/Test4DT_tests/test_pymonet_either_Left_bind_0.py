
# Module: pymonet.either
import pytest
from pymonet.either import Left  # Assuming the module is named correctly as per the documentation

# Test initialization of a Left instance with an error message
def test_left_initialization():
    left_value = Left("error message")
    assert left_value.value == "error message"

# Test using the map method on a Left instance
def test_map_method():
    left_value = Left("error message")
    mapped_left = left_value.map(lambda x: f"Error: {x}")

import pytest
from unittest.mock import patch
from pymonet.either import Left, Right

# Test for valid input scenario
def test_valid_input():
    left_instance = Left("error message")
    assert left_instance.is_left() is True

# Test for edge case scenario
def test_edge_case():
    left_instance = Left(None)
    assert left_instance.is_left() is True

# Test for invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        Left()

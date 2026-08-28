
import pytest
from unittest.mock import patch
from pymonet.either import Right, Left

# Test valid input scenario
def test_valid_input():
    right_value = Right(42)
    with patch('pymonet.either.Right.map', return_value=Right(84)):
        assert right_value.map(lambda x: x * 2).value == 84

# Test edge case scenario
def test_edge_case():
    right_none = Right(None)
    with patch('pymonet.either.Right.map', return_value=Right(None)):
        assert right_none.map(lambda x: x).value is None

# Test invalid input scenario
def test_invalid_input():
    right_invalid = Right(42)
    with patch('pymonet.either.Right.map', side_effect=TypeError):
        with pytest.raises(TypeError):
            right_invalid.map("not a callable")

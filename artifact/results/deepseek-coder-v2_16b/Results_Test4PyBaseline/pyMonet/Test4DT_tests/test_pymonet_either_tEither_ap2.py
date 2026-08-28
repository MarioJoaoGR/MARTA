
import pytest
from pymonet.either import Either, Right, Left

# Test cases for the ap method in Either class
def test_ap_with_right():
    """Test ap with a Right instance containing a callable function."""
    right = Right(lambda x: x + 1)
    result = right.ap(Right(5))
    assert isinstance(result, Right), "Expected Right"

import pytest
from pymonet.either import Either, Left, Right

# Test valid input where Either is not left and has a valid value

# Test edge case where Either is left and has an error message
def test_edge_case():
    either = Either(Left("some left value"))
    result = either.case(lambda x: "Error handling", lambda x: f"Success with {x}")
    assert result == "Error handling"
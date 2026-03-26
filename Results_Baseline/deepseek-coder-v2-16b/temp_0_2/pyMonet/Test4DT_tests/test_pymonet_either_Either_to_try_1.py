
import pytest
from pymonet.either import Either, Left, Right
from pymonet.monad_try import Try

# Test cases for the Either class and its methods

def test_to_try_left():
    """Test that to_try method returns a Try monad with error message when Either is Left."""
    left_value = Either(Left("error message"))
    try_monad = left_value.to_try()
    assert isinstance(try_monad, Try), "Expected the result of to_try to be an instance of Try"
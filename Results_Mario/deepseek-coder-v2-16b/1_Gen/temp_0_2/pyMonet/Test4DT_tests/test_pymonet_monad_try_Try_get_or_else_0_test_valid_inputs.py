
from pymonet.monad_try import Try
import pytest

def test_valid_inputs():
    # Test with a successful Try instance
    success = Try(10, True)
    assert success.get_or_else(0) == 10

    # Test with a failed Try instance
    failure = Try(None, False)
    assert failure.get_or_else("World") == "World"

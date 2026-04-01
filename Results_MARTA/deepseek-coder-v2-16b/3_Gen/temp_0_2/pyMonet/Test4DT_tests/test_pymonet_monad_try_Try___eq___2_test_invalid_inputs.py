
from pymonet.monad_try import Try
import pytest

def test_invalid_inputs():
    # Test equality with a non-Try object
    try1 = Try("test", True)
    assert not (try1 == "not a Try object")  # This should fail since it's not a Try instance

    # Test equality with another Try object with different values
    try2 = Try("different test", False)
    assert not (try1 == try2)  # This should fail since the values are different

    # Test equality with another Try object with the same values but is_success set to True
    try3 = Try("test", True)
    assert try1 == try3  # This should pass since both have the same value and is_success is True

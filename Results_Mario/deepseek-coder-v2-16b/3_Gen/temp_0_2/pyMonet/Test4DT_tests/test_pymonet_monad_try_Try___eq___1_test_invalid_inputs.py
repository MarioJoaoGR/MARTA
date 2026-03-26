
from pymonet.monad_try import Try
import pytest

def test_invalid_inputs():
    # Test with None value and False is_success
    try_object = Try(None, False)
    assert isinstance(try_object, Try), "Expected instance of Try"
    assert not try_object.is_success, "Expected is_success to be False"
    assert try_object.value is None, "Expected value to be None"

    # Test with a string value and True is_success
    try_object = Try("test", True)
    assert isinstance(try_object, Try), "Expected instance of Try"
    assert try_object.is_success, "Expected is_success to be True"
    assert try_object.value == "test", "Expected value to be 'test'"

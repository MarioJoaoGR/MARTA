
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    try_success = Try(42, True)  # Creates an instance where value is 42 and operation was successful.
    assert isinstance(try_success, Try)
    assert try_success.value == 42
    assert try_success.is_success is True

def test_invalid_input():
    with pytest.raises(TypeError):
        Try().on_fail(lambda x: print("Failure:", x))

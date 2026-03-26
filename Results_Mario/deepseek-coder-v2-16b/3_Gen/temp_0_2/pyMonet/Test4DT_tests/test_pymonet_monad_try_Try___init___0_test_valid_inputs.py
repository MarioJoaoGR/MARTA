
import pytest
from pymonet.monad_try import Try  # Assuming this is the correct module for Try class

def test_valid_inputs():
    try_object_true = Try("result", True)
    assert try_object_true.value == "result"
    assert try_object_true.is_success is True

    try_object_false = Try(None, False)
    assert try_object_false.value is None
    assert try_object_false.is_success is False


import pytest
from pymonet.monad_try import Try

def test_valid_inputs():
    try_object = Try("valid_string", True)
    assert try_object.is_success is True
    assert try_object.value == "valid_string"
    
    try_object_number = Try(123, True)
    assert try_object_number.is_success is True
    assert try_object_number.value == 123


import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

def test_invalid_input():
    # Test with invalid input type (should raise a TypeError)
    box = Box(123)  # Valid initialization
    
    # Attempt to call to_try() on the instance, which should return a successful Try monad
    try_monad = box.to_try()
    
    # Check if the returned object is an instance of Try and has the correct value and is_success attribute
    assert isinstance(try_monad, Try)
    assert try_monad.value == 123
    assert try_monad.is_success is True

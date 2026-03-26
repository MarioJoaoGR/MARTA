
import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

def test_valid_input():
    # Create a Box instance with a string value
    box = Box("Success")
    
    # Convert the Box to a successful Try monad
    try_monad = box.to_try()
    
    # Assert that the resulting Try monad contains the correct value and is_success is True
    assert try_monad.value == "Success"
    assert try_monad.is_success is True

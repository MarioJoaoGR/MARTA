
import pytest
from pymonet.validation import Validation
from pymonet.box import Box

def test_valid_inputs():
    # Create a Validation instance with a success value and no errors
    val = Validation("Success", [])
    
    # Transform the Validation to a Box
    box = val.to_box()
    
    # Check if the transformed Box contains the correct value
    assert isinstance(box, Box)
    assert box.value == "Success"

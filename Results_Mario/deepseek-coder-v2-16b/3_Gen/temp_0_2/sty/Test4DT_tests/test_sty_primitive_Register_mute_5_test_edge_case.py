
# Import necessary modules from the sty.primitive package
from unittest.mock import patch
from sty.primitive import Register, Renderfuncs, Style
import pytest

def test_mute():
    # Create an instance of Register
    reg = Register()
    
    # Ensure that the register is not muted initially
    assert not reg.is_muted
    
    # Call the mute method to mute the register
    reg.mute()
    
    # Check if the register is now muted
    assert reg.is_muted
    
    # Verify that all Style attributes are also muted by checking one example
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, Style):
            with pytest.raises(AttributeError):  # Assuming mute sets the attribute to None or similar behavior
                assert not hasattr(reg, attr_name)

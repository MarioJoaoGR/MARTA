
import pytest
from sty.primitive import Register, Style

def test_valid_input():
    # Create a new instance of Register
    register = Register()
    
    # Check that initially, the register is not muted
    assert not register.is_muted
    
    # Mute the register (this would typically be done outside this function)
    register.is_muted = True
    
    # Call unmute method to reset the register
    register.unmute()
    
    # Check that the register is now not muted
    assert not register.is_muted

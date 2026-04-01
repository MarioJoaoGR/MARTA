
# Import necessary modules and classes from the sty.primitive package
from sty.primitive import Register
import pytest

def test_unmute():
    # Create an instance of the Register class
    register = Register()
    
    # Initially, the register should be unmuted (is_muted should be False)
    assert not register.is_muted
    
    # Mute the register by setting is_muted to True
    register.is_muted = True
    assert register.is_muted
    
    # Call the unmute method to reset the muted state
    register.unmute()
    
    # After calling unmute, is_muted should be False again
    assert not register.is_muted

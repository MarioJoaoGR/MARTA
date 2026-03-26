
from sty import Style, Register
import pytest

def test_unmute():
    register = Register()
    assert not register.is_muted
    
    # Mute the register by setting is_muted to True (assuming there's a way to do this in the code)
    register.is_muted = True
    assert register.is_muted
    
    # Call unmute method
    register.unmute()
    assert not register.is_muted

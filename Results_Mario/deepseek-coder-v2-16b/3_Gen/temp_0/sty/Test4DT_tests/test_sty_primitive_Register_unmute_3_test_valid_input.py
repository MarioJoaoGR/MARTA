
from sty import Style, Register
import pytest

def test_valid_input():
    register = Register()
    assert not register.is_muted
    
    # Mute the register
    register.is_muted = True
    assert register.is_muted
    
    # Unmute the register
    register.unmute()
    assert not register.is_muted

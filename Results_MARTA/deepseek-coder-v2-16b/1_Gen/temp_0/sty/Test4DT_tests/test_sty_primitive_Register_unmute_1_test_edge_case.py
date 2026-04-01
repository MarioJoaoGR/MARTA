
import pytest
from sty.primitive import Register

def test_unmute():
    register = Register()
    assert not register.is_muted  # Initially, the register should not be muted
    
    register.is_muted = True  # Simulate muting the register
    assert register.is_muted  # Verify that it is indeed muted
    
    register.unmute()  # Unmute the register
    assert not register.is_muted  # Check if unmuting worked by verifying the state

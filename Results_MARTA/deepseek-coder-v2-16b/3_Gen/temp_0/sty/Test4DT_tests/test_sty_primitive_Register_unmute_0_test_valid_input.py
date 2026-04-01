
import pytest
from sty import Register

def test_unmute():
    register = Register()
    assert not register.is_muted  # Initially, the register should not be muted

    register.is_muted = True  # Simulate a mute state
    register.unmute()  # Call unmute method to reset the muted state

    assert not register.is_muted  # After unmuting, the register should not be muted

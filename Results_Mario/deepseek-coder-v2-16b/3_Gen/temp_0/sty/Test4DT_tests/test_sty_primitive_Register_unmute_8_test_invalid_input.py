
import pytest
from sty import Register

def test_unmute():
    register = Register()
    assert not register.is_muted  # Initially, the register should not be muted

    register.is_muted = True  # Simulate a muted state by directly setting the attribute
    register.unmute()  # Call the unmute method to reset the muted state

    assert not register.is_muted  # After calling unmute, the register should no longer be muted

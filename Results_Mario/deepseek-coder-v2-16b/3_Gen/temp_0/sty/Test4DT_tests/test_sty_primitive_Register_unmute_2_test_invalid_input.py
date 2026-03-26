
from sty import Register
import pytest

def test_unmute():
    register = Register()
    assert not register.is_muted  # Initially, the register should be unmuted
    
    register.unmute()  # Call the unmute method
    assert not register.is_muted  # After calling unmute, it should still be unmuted

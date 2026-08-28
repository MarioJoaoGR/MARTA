
import pytest
from sty.primitive import Register

def test_unmute():
    register = Register()
    assert not register.is_muted, "Initial state should be unmuted"
    
    register.unmute()
    assert not register.is_muted, "Unmuting should set is_muted to False"

def test_invalid_input():
    with pytest.raises(TypeError):
        Register("unexpected argument")

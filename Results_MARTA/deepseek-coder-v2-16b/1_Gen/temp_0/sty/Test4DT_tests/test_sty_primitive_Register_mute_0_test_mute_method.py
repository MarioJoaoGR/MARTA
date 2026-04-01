
import pytest
from sty import Register

def test_mute_method():
    reg = Register()
    
    # Initially, the register should not be muted
    assert not reg.is_muted
    
    # After calling mute(), the register should be muted
    reg.mute()
    assert reg.is_muted

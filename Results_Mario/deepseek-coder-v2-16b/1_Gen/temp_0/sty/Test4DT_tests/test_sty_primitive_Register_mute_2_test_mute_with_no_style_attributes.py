
import pytest
from sty.primitive import Register, Style

def test_mute_with_no_style_attributes():
    reg = Register()
    assert not reg.is_muted  # Ensure the register is not muted initially
    
    reg.mute()  # Mute the register
    assert reg.is_muted  # Ensure the register is muted after calling mute method

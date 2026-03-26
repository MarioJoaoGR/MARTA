
import pytest
from sty.primitive import Register

# Test initialization of the Register class
def test_register_initialization():
    reg = Register()
    assert hasattr(reg, 'renderfuncs') and isinstance(reg.renderfuncs, dict)
    assert hasattr(reg, 'is_muted') and not reg.is_muted
    assert hasattr(reg, 'eightbit_call') and callable(reg.eightbit_call)
    assert hasattr(reg, 'rgb_call') and callable(reg.rgb_call)

# Test muting the register
def test_register_mute():
    reg = Register()
    assert not reg.is_muted
    reg.mute()
    assert reg.is_muted

# Test unmuting the register
def test_register_unmute():
    reg = Register()
    reg.mute()
    assert reg.is_muted
    reg.unmute()
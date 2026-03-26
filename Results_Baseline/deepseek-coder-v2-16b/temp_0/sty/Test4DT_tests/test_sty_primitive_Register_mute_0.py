
import pytest
from sty.primitive import Register

# Test creating an instance of Register
def test_create_register():
    reg = Register()
    assert hasattr(reg, 'renderfuncs')
    assert isinstance(reg.renderfuncs, dict)
    assert hasattr(reg, 'is_muted')
    assert isinstance(reg.is_muted, bool)
    assert hasattr(reg, 'eightbit_call')
    assert callable(reg.eightbit_call)
    assert hasattr(reg, 'rgb_call')
    assert callable(reg.rgb_call)

# Test muting the register
def test_mute():
    reg = Register()
    reg.mute()
    assert reg.is_muted is True

# Test unmuting the register
def test_unmute():
    reg = Register()
    reg.mute()
    reg.unmute()
    assert reg.is_muted is False

# Test exporting the register as a dictionary
def test_as_dict():
    reg = Register()
    dict_repr = reg.as_dict()
    assert isinstance(dict_repr, dict)
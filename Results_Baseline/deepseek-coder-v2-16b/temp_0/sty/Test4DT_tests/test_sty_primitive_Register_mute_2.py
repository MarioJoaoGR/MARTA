
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

# Test muting method sets is_muted to True
def test_mute_method():
    reg = Register()
    reg.mute()
    assert reg.is_muted == True

# Test that other attributes are not affected by the mute method
def test_other_attributes_not_affected():
    reg = Register()
    initial_attr = getattr(reg, dir(reg)[0])  # Get an initial attribute to compare later
    reg.mute()
    assert getattr(reg, dir(reg)[0]) == initial_attr  # Ensure the attribute hasn't changed

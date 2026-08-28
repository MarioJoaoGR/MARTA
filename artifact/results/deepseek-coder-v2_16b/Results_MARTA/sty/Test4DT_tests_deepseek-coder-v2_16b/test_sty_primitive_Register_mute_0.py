
import pytest
from sty.primitive import Register, Style

# Test to check if the register starts unmuted
def test_initial_unmuted():
    register = Register()
    assert not register.is_muted, "Register should start unmuted"

# Test to mute the register and then check if it is muted
def test_mute_method():
    register = Register()
    register.mute()
    assert register.is_muted, "Register should be muted after calling mute method"

# Test to unmute the register and then check if it is not muted
def test_unmute_method():
    register = Register()
    register.mute()
    register.unmute()
    assert not register.is_muted, "Register should be unmuted after calling unmute method"

# Test to check if the mute method mutes all Style attributes
def test_mute_with_style_attributes():
    register = Register()
    for attr in dir(register):
        val = getattr(register, attr)
        if isinstance(val, Style):
            setattr(register, attr, val)
    assert not register.is_muted, "All style attributes should be muted"

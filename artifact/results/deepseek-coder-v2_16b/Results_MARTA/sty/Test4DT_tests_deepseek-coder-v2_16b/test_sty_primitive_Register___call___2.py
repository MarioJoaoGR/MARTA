
import pytest
from sty.primitive import Register

# Test to check if the register starts unmuted
def test_initial_unmuted():
    register = Register()
    assert not register.is_muted, "Register should start unmuted"

# Test to mute the register and then check if it is muted
def test_mute_method():
    register = Register()
    register.mute()
    assert register.is_muted, "Register should be muted after calling mute()"

# Test to unmute the register and then check if it is unmuted
def test_unmute_method():
    register = Register()
    register.mute()
    register.unmute()
    assert not register.is_muted, "Register should be unmuted after calling unmute()"

# Test to handle invalid input and raise TypeError
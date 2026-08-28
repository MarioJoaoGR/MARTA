
import pytest
from sty.primitive import Register

# Test to check if the register starts unmuted
def test_initial_unmuted():
    custom_register = Register()
    assert not custom_register.is_muted, "Register should start unmuted"

# Test to mute the register and then check if it is muted
def test_mute_method():
    custom_register = Register()
    custom_register.mute()
    assert custom_register.is_muted, "Register should be muted after calling mute()"

# Test to unmute the register and then check if it is not muted
def test_unmute_method():
    custom_register = Register()
    custom_register.mute()
    custom_register.unmute()
    assert not custom_register.is_muted, "Register should be unmuted after calling unmute()"

# Test to handle valid 8-bit color input correctly

# Test to handle edge case of None input

# Test to handle edge case of empty list input

# Test for error handling with invalid input type
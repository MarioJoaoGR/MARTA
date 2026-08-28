
import pytest
from sty.primitive import Register

# Test to check if the register starts unmuted
def test_initial_unmuted():
    reg = Register()
    assert not reg.is_muted, "Register should start unmuted"

# Test to check valid inputs return expected output
def test_valid_mute():
    reg = Register()
    reg.mute()
    assert reg.is_muted, "Expected the register to be muted after calling mute()"

# Test to check invalid inputs raise TypeError

# Test to check edge cases raise AttributeError
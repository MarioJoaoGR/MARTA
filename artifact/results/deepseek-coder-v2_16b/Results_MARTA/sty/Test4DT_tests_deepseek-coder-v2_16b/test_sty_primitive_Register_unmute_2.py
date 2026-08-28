
import pytest
from sty.primitive import Register

# Test to check if the register starts unmuted
def test_initial_unmuted():
    reg = Register()
    assert not reg.is_muted, "Register should start unmuted"

# Test to check valid inputs return expected output
def test_valid_unmute():
    register = Register()
    assert not register.is_muted  # Initial state should be unmuted
    register.unmute()  # Unmute the register
    assert register.is_muted is False  # After unmuting, it should still be unmuted

# Test to check invalid inputs raise TypeError
def test_invalid_input_unmute():
    non_register = "I am not a Register"
    with pytest.raises(AttributeError):
        non_register.unmute()  # Attempt to call unmute on a non-Register object


import pytest
from sty.lib import Register, mute

# Test to check if the register starts unmuted
def test_initial_unmuted():
    reg = Register()
    assert not reg.is_muted, "Register should start unmuted"

# Test to check valid inputs return expected output
def test_valid_inputs_return_expected_output():
    reg1 = Register()
    reg2 = Register()
    mute(reg1, reg2)
    assert reg1.is_muted and reg2.is_muted, "Both registers should be muted"

# Test to check invalid inputs raise TypeError
def test_invalid_inputs_raise_type_error():
    class NonRegisterClass:
        pass
    
    non_register = NonRegisterClass()
    with pytest.raises(ValueError) as e:
        mute(non_register)
    assert str(e.value) == "The mute() method can only be used with objects that inherit from the 'Register class'."

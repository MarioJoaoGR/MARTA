
import pytest
from sty.lib import unmute, Register

class NonRegister:
    def unmute(self):
        pass


def test_unmute_single_register():
    reg1 = Register()
    reg1.mute()
    assert reg1.is_muted  # Corrected assertion to check if muted before unmuting
    unmute(reg1)
    assert not reg1.is_muted


def test_unmute_multiple_registers():
    reg1 = Register()
    reg2 = Register()
    reg1.mute()
    reg2.mute()
    assert reg1.is_muted and reg2.is_muted  # Corrected assertion to check if muted before unmuting
    unmute(reg1, reg2)
    assert not reg1.is_muted
    assert not reg2.is_muted


def test_unmute_already_unmuted_registers():
    reg1 = Register()
    reg2 = Register()
    unmute(reg1, reg2)  # No need to mute as they are already unmuted by default
    assert not reg1.is_muted
    assert not reg2.is_muted


def test_unmute_with_non_register_object():
    reg1 = Register()
    non_reg = NonRegister()
    with pytest.raises(ValueError) as e_info:
        unmute(reg1, non_reg)
    assert str(e_info.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."


def test_unmute_with_no_objects():
    unmute()  # Should not raise any error


def test_unmute_with_mixed_valid_and_invalid_objects():
    reg1 = Register()
    non_reg = NonRegister()
    with pytest.raises(ValueError) as e_info:
        unmute(reg1, non_reg)
    assert str(e_info.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."

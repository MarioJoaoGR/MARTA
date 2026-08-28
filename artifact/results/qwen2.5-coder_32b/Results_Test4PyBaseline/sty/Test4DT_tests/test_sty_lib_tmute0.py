# Module: sty.lib
import pytest
from sty.lib import mute, Register

class MockRegister(Register):
    def __init__(self):
        self.muted = False

    def mute(self):
        self.muted = True

class NonRegister:
    def mute(self):
        pass

def test_mute_single_register():
    reg1 = MockRegister()
    mute(reg1)
    assert reg1.muted is True, "The register should be muted after calling mute."

def test_mute_multiple_registers():
    reg1 = MockRegister()
    reg2 = MockRegister()
    mute(reg1, reg2)
    assert reg1.muted is True, "reg1 should be muted after calling mute."
    assert reg2.muted is True, "reg2 should be muted after calling mute."

def test_mute_subclass_of_register():
    class SubRegister(Register):
        def __init__(self):
            super().__init__()
            self.muted = False

        def mute(self):
            self.muted = True

    sub_reg1 = SubRegister()
    mute(sub_reg1)
    assert sub_reg1.muted is True, "Subclass of Register should be muted after calling mute."

def test_mute_custom_register():
    class CustomRegister(Register):
        def __init__(self):
            super().__init__()
            self.muted = False

        def mute(self):
            self.muted = True

    custom_reg1 = CustomRegister()
    mute(custom_reg1)
    assert custom_reg1.muted is True, "Custom subclass of Register should be muted after calling mute."

def test_mute_non_register_object():
    non_reg = NonRegister()
    with pytest.raises(ValueError) as excinfo:
        mute(non_reg)
    assert str(excinfo.value) == "The mute() method can only be used with objects that inherit from the 'Register class'.", "Should raise ValueError for non-Register object."

def test_mute_mixed_objects():
    reg1 = MockRegister()
    non_reg = NonRegister()
    with pytest.raises(ValueError) as excinfo:
        mute(reg1, non_reg)
    assert str(excinfo.value) == "The mute() method can only be used with objects that inherit from the 'Register class'.", "Should raise ValueError when one of the objects is not a Register."

def test_mute_no_objects():
    mute()  # Should not raise any error if no objects are provided

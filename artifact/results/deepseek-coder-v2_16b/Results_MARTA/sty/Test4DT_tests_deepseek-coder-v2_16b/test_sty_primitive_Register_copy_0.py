
import pytest
from copy import deepcopy
from sty.primitive import Register

# Test for creating an instance of Register
def test_register_instance():
    reg = Register()
    assert isinstance(reg, Register), "Instance should be a Register"
    assert not reg.is_muted, "Default is_muted should be False"

# Test for muting and unmuting the register
def test_mute_unmute():
    reg = Register()
    reg.mute()
    assert reg.is_muted, "After muting, is_muted should be True"
    reg.unmute()
    assert not reg.is_muted, "After unmuting, is_muted should be False"

# Test for setting a custom RGB call function

# Test for exporting the register as a dictionary

# Test for creating a deep copy of the register
def test_copy():
    reg = Register()
    copied_reg = reg.copy()
    assert isinstance(copied_reg, Register), "Copied instance should be a Register"
    assert not copied_reg.is_muted, "Copied register's is_muted should be False"
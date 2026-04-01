
import pytest
from copy import deepcopy
from sty.primitive import Register

def test_sty_primitive_Register_copy():
    # Create an instance of Register
    reg = Register()
    
    # Make a copy of the register
    copied_reg = reg.copy()
    
    # Check if the copied register is equal to the original (deepcopy should create a new object)
    assert reg is not copied_reg
    assert isinstance(copied_reg, Register)
    
    # Check if attributes are the same except for the copy method which will be different in deepcopied objects
    assert reg.renderfuncs == copied_reg.renderfuncs
    assert reg.is_muted == copied_reg.is_muted
    assert reg.eightbit_call == copied_reg.eightbit_call
    assert reg.rgb_call == copied_reg.rgb_call

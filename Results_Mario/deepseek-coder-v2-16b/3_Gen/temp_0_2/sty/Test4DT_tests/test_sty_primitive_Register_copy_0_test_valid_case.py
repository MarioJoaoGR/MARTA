
import pytest
from copy import deepcopy
from sty.primitive import Register

def test_valid_case():
    # Create an instance of Register
    reg = Register()
    
    # Make a copy of the register
    copied_reg = reg.copy()
    
    # Check if the copy is equal to the original (deepcopy should create a new object)
    assert reg != copied_reg
    assert isinstance(copied_reg, Register)
    
    # Check if the attributes are the same initially
    assert reg.renderfuncs == copied_reg.renderfuncs
    assert reg.is_muted == copied_reg.is_muted
    assert reg.eightbit_call == copied_reg.eightbit_call
    assert reg.rgb_call == copied_reg.rgb_call
    
    # Modify the original register and check if it affects the copy
    reg.is_muted = True
    assert reg.is_muted != copied_reg.is_muted
    
    # Make sure modifying the original does not affect the copy
    assert reg.renderfuncs == copied_reg.renderfuncs
    assert reg.eightbit_call == copied_reg.eightbit_call
    assert reg.rgb_call == copied_reg.rgb_call

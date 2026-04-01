
import pytest
from copy import deepcopy
from sty.primitive import Register

def test_edge_case():
    # Create an instance of Register
    reg = Register()
    
    # Make a copy of the register
    copied_reg = reg.copy()
    
    # Check if the copied register is not muted and has no custom render functions
    assert not copied_reg.is_muted
    assert len(copied_reg.renderfuncs) == 0
    
    # Check if the lambda functions are deep-copied correctly
    original_lambda = reg.eightbit_call
    copied_lambda = copied_reg.eightbit_call
    assert original_lambda("test") == "test"
    assert copied_lambda("test") == "test"
    
    # Modify the original register and check if it doesn't affect the copy
    reg.is_muted = True
    reg.renderfuncs['custom'] = lambda x: f"Custom {x}"
    
    assert not copied_reg.is_muted
    assert len(copied_reg.renderfuncs) == 0

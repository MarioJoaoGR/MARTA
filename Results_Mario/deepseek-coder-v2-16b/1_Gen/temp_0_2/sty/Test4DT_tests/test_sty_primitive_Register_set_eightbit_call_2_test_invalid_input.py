
import pytest
from sty import Register
from typing import Type

class CustomRenderType:
    pass  # Dummy implementation to simulate a custom render type

def test_set_eightbit_call():
    register = Register()
    
    # Define a dummy function for the custom render type
    def dummy_func(x):
        return x
    
    # Set up the custom render type in the renderfuncs dictionary
    register.renderfuncs[CustomRenderType] = dummy_func
    
    # Call set_eightbit_call with the CustomRenderType
    register.set_eightbit_call(CustomRenderType)
    
    # Check if the eightbit_call attribute has been updated correctly
    assert register.eightbit_call == dummy_func


import pytest
from copy import deepcopy
from sty.primitive import Register

def test_valid_input():
    custom_register = Register()
    copied_register = custom_register.copy()
    
    # Check if the original and copied objects are not the same instance
    assert id(custom_register) != id(copied_register)
    
    # Check if the copied object has the same attributes as the original
    assert custom_register.__dict__ == copied_register.__dict__

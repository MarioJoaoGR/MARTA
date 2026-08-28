
import pytest
from copy import deepcopy
from sty.primitive import Register

def test_copy_happy_path():
    my_register = Register()
    copied_register = my_register.copy()
    
    assert copied_register.renderfuncs == {}
    assert copied_register.is_muted is False

def test_copy_with_custom_values():
    my_register = Register()
    my_register.is_muted = True
    my_register.eightbit_call = lambda x: x + 10
    my_register.rgb_call = lambda r, g, b: (r+10, g+10, b+10)
    
    copied_register = my_register.copy()
    
    assert copied_register.is_muted is True
    assert copied_register.eightbit_call(5) == 15
    assert copied_register.rgb_call(10, 20, 30) == (20, 30, 40)

def test_copy_with_empty_renderfuncs():
    my_register = Register()
    my_register.renderfuncs = {}
    
    copied_register = my_register.copy()
    
    assert copied_register.renderfuncs == {}

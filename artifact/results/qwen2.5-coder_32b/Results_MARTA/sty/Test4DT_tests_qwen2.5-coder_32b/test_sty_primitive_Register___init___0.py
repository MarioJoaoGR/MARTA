
import pytest
from sty.primitive import Register



def test_eightbit_call_with_valid_function():
    my_register = Register()
    my_register.eightbit_call = lambda x: x + 10
    
    assert my_register.eightbit_call(42) == 52

def test_rgb_call_with_valid_function():
    my_register = Register()
    my_register.rgb_call = lambda r, g, b: (r+10, g+10, b+10)
    
    assert my_register.rgb_call(102, 49, 42) == (112, 59, 52)

def test_is_muted_initial_value():
    my_register = Register()
    
    assert my_register.is_muted is False

def test_set_is_muted_to_true():
    my_register = Register()
    my_register.is_muted = True
    
    assert my_register.is_muted is True

def test_set_is_muted_to_false():
    my_register = Register()
    my_register.is_muted = True
    my_register.is_muted = False
    
    assert my_register.is_muted is False

def test_renderfuncs_initial_value():
    my_register = Register()
    
    assert my_register.renderfuncs == {}
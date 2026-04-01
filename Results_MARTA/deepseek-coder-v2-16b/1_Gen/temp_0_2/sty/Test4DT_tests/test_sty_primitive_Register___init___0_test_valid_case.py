
import pytest
from sty import Register  # Assuming 'sty' is the module and 'Register' is its class, adjust accordingly if different names are used

def test_register_init():
    register = Register()
    
    assert isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert register.renderfuncs == {}, "Expected an empty dictionary for renderfuncs"
    
    assert isinstance(register.is_muted, bool), "Expected is_muted to be a boolean"
    assert register.is_muted is False, "Expected is_muted to be False by default"
    
    assert callable(register.eightbit_call), "Expected eightbit_call to be a callable (lambda function)"
    assert register.eightbit_call(10) == 10, "Expected eightbit_call to return its argument unchanged"
    
    assert callable(register.rgb_call), "Expected rgb_call to be a callable (lambda function)"
    r, g, b = 25, 30, 40
    assert register.rgb_call(r, g, b) == (r, g, b), "Expected rgb_call to return the RGB values unchanged"

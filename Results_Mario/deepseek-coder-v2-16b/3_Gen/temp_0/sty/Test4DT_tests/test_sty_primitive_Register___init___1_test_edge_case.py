
import pytest
from sty import Register  # Assuming 'sty' is the module and 'Register' is its class, adjust accordingly if different names or structure

def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not register.is_muted, "Expected is_muted to be False"
    assert callable(register.eightbit_call), "Expected eightbit_call to be a callable"
    assert callable(register.rgb_call), "Expected rgb_call to be a callable"

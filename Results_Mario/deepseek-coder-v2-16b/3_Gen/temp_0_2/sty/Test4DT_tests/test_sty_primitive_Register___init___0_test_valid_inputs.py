
import pytest
from sty import Register  # Assuming 'sty' is the correct module path and 'Register' is the class within that module

def test_valid_inputs():
    register = Register()
    assert isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert register.is_muted == False, "Expected is_muted to be False"
    assert callable(register.eightbit_call), "Expected eightbit_call to be a callable"
    assert callable(register.rgb_call), "Expected rgb_call to be a callable"

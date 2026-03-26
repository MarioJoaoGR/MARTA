
import pytest
from sty.primitive import Register

# Test initialization of the Register class
def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not register.is_muted, "Expected is_muted to be False"
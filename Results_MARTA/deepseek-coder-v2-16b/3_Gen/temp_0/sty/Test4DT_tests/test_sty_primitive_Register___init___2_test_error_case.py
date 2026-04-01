
import pytest
from sty import Register  # Assuming 'sty' is the module and 'Register' is its class, adjust accordingly if different names or structure

def test_register_initialization():
    register = Register()
    assert register.renderfuncs == {}
    assert not register.is_muted
    assert register.eightbit_call(10) == 10
    assert register.rgb_call(255, 0, 0) == (255, 0, 0)

# Run this test with Pytest: pytest -v your_script_name.py


# Module: sty.primitive
# test_register.py
from sty.primitive import Register
import pytest
from typing import Tuple  # Added this import for the 'Tuple' variable type hint

@pytest.fixture
def register():
    return Register()

def test_default_attributes(register):
    assert isinstance(register.renderfuncs, dict)
    assert not register.is_muted
    assert callable(register.eightbit_call)
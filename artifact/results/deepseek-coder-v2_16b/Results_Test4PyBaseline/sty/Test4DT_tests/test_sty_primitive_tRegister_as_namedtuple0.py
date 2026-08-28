
# Module: sty.primitive
# test_register.py
from sty.primitive import Register
import pytest
from collections import namedtuple

@pytest.fixture
def register():
    return Register()

def test_initialization(register):
    assert isinstance(register.renderfuncs, dict)
    assert not register.is_muted
    assert callable(register.eightbit_call)
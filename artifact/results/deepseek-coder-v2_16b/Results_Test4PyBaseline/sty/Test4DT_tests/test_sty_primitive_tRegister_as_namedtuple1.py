
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

# New test case to cover line 199 and 200 of the as_namedtuple method
def test_as_namedtuple_conversion(register):
    # Assuming that 'register' has a method or property called 'as_dict' which returns a dictionary representation of the color register.
    d = register.as_dict()
    
    # Create a namedtuple from the keys and values of the dictionary
    expected_namedtuple = namedtuple("StyleRegister", list(d.keys()))(*list(d.values()))
    
    # Convert the register to a namedtuple using as_namedtuple method
    actual_namedtuple = register.as_namedtuple()
    
    # Assert that the actual and expected namedtuples are equal
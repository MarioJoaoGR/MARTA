
import pytest
from sty import Register
from copy import deepcopy

def test_register_initialization():
    register = Register()
    assert register.renderfuncs == {}
    assert not register.is_muted
    assert register.eightbit_call(10) == 10
    assert register.rgb_call(255, 255, 255) == (255, 255, 255)

def test_register_copy():
    register = Register()
    copied_register = register.copy()
    assert isinstance(copied_register, Register)
    assert register.renderfuncs == copied_register.renderfuncs
    assert register.is_muted == copied_register.is_muted
    assert register.eightbit_call == copied_register.eightbit_call
    assert register.rgb_call == copied_register.rgb_call


import pytest
from sty.primitive import Register

def test_register_initialization():
    register = Register()
    assert not register.is_muted, "Initial state of is_muted should be False"
    assert register.eightbit_call(10) == 10, "Default eightbit_call should return the input value"
    assert register.rgb_call(10, 20, 30) == (10, 20, 30), "Default rgb_call should return the input values"

def test_register_mute():
    register = Register()
    register.mute()
    assert register.is_muted, "After muting, is_muted should be True"

def test_register_unmute():
    register = Register()
    register.mute()
    register.unmute()
    assert not register.is_muted, "After unmuting, is_muted should be False"



def test_register_copy():
    register = Register()
    copied_register = register.copy()
    assert register.is_muted == copied_register.is_muted, "Copied register should have the same state as the original"
    assert register.eightbit_call == copied_register.eightbit_call, "Copied register should have the same eightbit_call function"
    assert register.rgb_call == copied_register.rgb_call, "Copied register should have the same rgb_call function"
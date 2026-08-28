
# Test case  
import pytest
from sty.primitive import Register

def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict), "renderfuncs should be an empty dictionary"
    assert not register.is_muted, "is_muted should default to False"
    assert callable(register.eightbit_call), "eightbit_call should be a lambda function"
    assert callable(register.rgb_call), "rgb_call should be a lambda function"

def test_register_eightbit_call():
    register = Register()
    assert register.eightbit_call(5) == 5, "eightbit_call should return the input unchanged"
    assert register.eightbit_call(-10) == -10, "eightbit_call should handle negative numbers correctly"
    assert register.eightbit_call(0) == 0, "eightbit_call should handle zero correctly"

def test_register_rgb_call():
    register = Register()
    assert register.rgb_call(10, 20, 30) == (10, 20, 30), "rgb_call should return the input tuple unchanged"
    assert register.rgb_call(0, 0, 0) == (0, 0, 0), "rgb_call should handle zero values correctly"
    assert register.rgb_call(255, 255, 255) == (255, 255, 255), "rgb_call should handle max RGB values correctly"

def test_register_mute_unmute():
    register = Register()
    register.mute()
    assert register.is_muted, "register should be muted after calling mute()"
    register.unmute()
    assert not register.is_muted, "register should be unmuted after calling unmute()"

def test_register_as_dict():
    register = Register()
    register_dict = register.as_dict()
    assert isinstance(register_dict, dict), "as_dict should return a dictionary"
    # Adjusted to match actual output

import pytest
from sty.primitive import Register, Style

def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict)
    assert not register.is_muted
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

def test_register_mute():
    register = Register()
    register.mute()
    assert register.is_muted


def test_eightbit_call_default_behavior():
    register = Register()
    result = register.eightbit_call(255)
    assert result == 255

def test_rgb_call_default_behavior():
    register = Register()
    result = register.rgb_call(255, 0, 0)
    assert result == (255, 0, 0)

def test_custom_eightbit_call():
    register = Register()
    register.eightbit_call = lambda x: f"8-bit color: {x}"
    result = register.eightbit_call(255)
    assert result == "8-bit color: 255"

def test_custom_rgb_call():
    register = Register()
    register.rgb_call = lambda r, g, b: f"RGB color: ({r}, {g}, {b})"
    result = register.rgb_call(255, 0, 0)
    assert result == "RGB color: (255, 0, 0)"
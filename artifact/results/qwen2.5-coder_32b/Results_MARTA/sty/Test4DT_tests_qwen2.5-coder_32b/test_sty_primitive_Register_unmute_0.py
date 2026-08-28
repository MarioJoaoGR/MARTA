
import pytest
from sty.primitive import Register, Style


def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict)
    assert not register.is_muted
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

def test_register_unmute_resets_is_muted_flag():
    register = Register()
    register.is_muted = True
    register.unmute()
    assert not register.is_muted

def test_register_eightbit_call_default_behavior():
    register = Register()
    result = register.eightbit_call(42)
    assert result == 42

def test_register_rgb_call_default_behavior():
    register = Register()
    result = register.rgb_call(102, 49, 42)
    assert result == (102, 49, 42)

def test_register_unmute_with_no_style_attribute():
    register = Register()
    register.unmute()
    assert not hasattr(register, 'my_style')
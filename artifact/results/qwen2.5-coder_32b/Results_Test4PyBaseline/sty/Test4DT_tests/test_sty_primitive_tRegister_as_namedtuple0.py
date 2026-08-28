
# Test case  
import pytest
from sty.primitive import Register
from collections import namedtuple

def test_register_initialization():
    reg = Register()
    assert isinstance(reg.renderfuncs, dict)
    assert not reg.is_muted
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)

def test_eightbit_call_default_behavior():
    reg = Register()
    assert reg.eightbit_call(5) == 5

def test_rgb_call_default_behavior():
    reg = Register()
    assert reg.rgb_call(10, 20, 30) == (10, 20, 30)

def test_overriding_eightbit_call():
    reg = Register()
    reg.eightbit_call = lambda x: x + 10
    assert reg.eightbit_call(5) == 15

def test_overriding_rgb_call():
    reg = Register()
    reg.rgb_call = lambda r, g, b: (r * 2, g * 2, b * 2)
    assert reg.rgb_call(10, 20, 30) == (20, 40, 60)

def test_as_namedtuple():
    reg = Register()
    reg.color1 = "red"
    reg._private_attr = "should not be included"
    style_register = reg.as_namedtuple()
    StyleRegister = namedtuple("StyleRegister", ["color1"])
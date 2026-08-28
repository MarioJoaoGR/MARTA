# Module: sty.primitive
import pytest
from sty.primitive import Register

def test_register_initialization():
    reg = Register()
    assert isinstance(reg.renderfuncs, dict)
    assert not reg.is_muted
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)

def test_register_eightbit_call_default_behavior():
    reg = Register()
    assert reg.eightbit_call(42) == 42

def test_register_rgb_call_default_behavior():
    reg = Register()
    assert reg.rgb_call(102, 49, 42) == (102, 49, 42)

def test_register_call_with_8bit_color_code():
    reg = Register()
    assert reg(42) == 42

def test_register_call_with_rgb_values():
    reg = Register()
    assert reg(102, 49, 42) == (102, 49, 42)

def test_register_call_with_named_attribute():
    reg = Register()
    reg.red = "red_color_code"
    assert reg('red') == "red_color_code"

def test_register_call_when_muted():
    reg = Register()
    reg.is_muted = True
    assert reg(42) == ""
    assert reg('red') == ""

def test_register_override_eightbit_call():
    reg = Register()
    reg.eightbit_call = lambda x: f"\033[38;5;{x}m"
    assert reg(42) == "\033[38;5;42m"

def test_register_override_rgb_call():
    reg = Register()
    reg.rgb_call = lambda r, g, b: f"\033[38;2;{r};{g};{b}m"
    assert reg(102, 49, 42) == "\033[38;2;102;49;42m"

def test_register_call_with_invalid_arguments():
    reg = Register()
    assert reg() == ""
    assert reg(42, 42) == ""
    assert reg("red", "blue") == ""

def test_register_mute_unmute_methods():
    reg = Register()
    reg.mute()
    assert reg.is_muted
    reg.unmute()
    assert not reg.is_muted

# Assuming mute and unmute methods are defined as follows:
# def mute(self):
#     self.is_muted = True
#
# def unmute(self):
#     self.is_muted = False

# Module: sty.primitive
import pytest
from sty.primitive import Register

def test_register_initialization():
    register = Register()
    assert isinstance(register.renderfuncs, dict) and not register.renderfuncs, "renderfuncs should be an empty dictionary"
    assert not register.is_muted, "is_muted should be False by default"
    assert callable(register.eightbit_call), "eightbit_call should be a callable"
    assert callable(register.rgb_call), "rgb_call should be a callable"

def test_register_eightbit_call_default():
    register = Register()
    assert register.eightbit_call(5) == 5, "Default eightbit_call should return the input unchanged"

def test_register_rgb_call_default():
    register = Register()
    assert register.rgb_call(10, 20, 30) == (10, 20, 30), "Default rgb_call should return a tuple of the inputs"

def test_register_unmute():
    register = Register()
    register.is_muted = True
    register.unmute()
    assert not register.is_muted, "unmute should set is_muted to False"

# Assuming Style and RenderType are defined elsewhere in your codebase
# from sty import Style, RenderType

# def test_register_unmute_with_style_attributes():
#     # This test would require the Style class to be defined and used within Register
#     register = Register()
#     style_instance = Style(RenderType.EIGHTBIT, 123)
#     setattr(register, 'some_style', style_instance)
#     register.is_muted = True
#     register.unmute()
#     assert getattr(register, 'some_style') == style_instance, "unmute should reset Style attributes correctly"

def test_register_custom_eightbit_call():
    register = Register()
    custom_eightbit_render = lambda x: f"\033[38;5;{x}m"
    register.eightbit_call = custom_eightbit_render
    assert register.eightbit_call(42) == "\033[38;5;42m", "Custom eightbit_call should return the expected ANSI escape sequence"

def test_register_custom_rgb_call():
    register = Register()
    custom_rgb_render = lambda r, g, b: f"\033[38;2;{r};{g};{b}m"
    register.rgb_call = custom_rgb_render
    assert register.rgb_call(102, 49, 42) == "\033[38;2;102;49;42m", "Custom rgb_call should return the expected ANSI escape sequence"

# Additional tests can be added based on other methods and attributes of the Register class

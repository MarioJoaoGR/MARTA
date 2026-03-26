
# Module: sty.primitive
import pytest
from sty.primitive import Register

# Test initialization of the Register class
def test_register_initialization():
    reg = Register()
    assert isinstance(reg.renderfuncs, dict)
    assert not reg.is_muted
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)

# Test creating a custom render function in the register
def test_custom_render_function():
    reg = Register()
    reg.renderfuncs['custom'] = lambda x: f"Custom {x}"
    assert 'custom' in reg.renderfuncs
    assert reg.renderfuncs['custom']("function") == "Custom function"

# Test muting and unmuting the register
def test_mute_unmute():
    reg = Register()
    assert not reg.is_muted
    reg.mute()
    assert reg.is_muted
    reg.unmute()
    assert not reg.is_muted

# Test exporting the register as a dictionary
def test_as_dict():
    reg = Register()
    dict_repr = reg.as_dict()
    expected_keys = {'renderfuncs', 'is_muted', 'eightbit_call', 'rgb_call'}
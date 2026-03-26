# Module: sty.primitive
import pytest
from sty import Register
from copy import deepcopy

# Test creating an instance of the Register class
def test_create_register():
    reg = Register()
    assert isinstance(reg, Register), "The object should be an instance of the Register class"
    assert reg.renderfuncs == {}, "Render functions dictionary should be empty initially"
    assert not reg.is_muted, "Register should not be muted initially"
    assert reg.eightbit_call(123) == 123, "Eightbit call should return the input value"
    assert reg.rgb_call(255, 0, 0) == (255, 0, 0), "RGB call should return the specified RGB values"

# Test muting and unmuting the register
def test_mute_unmute():
    reg = Register()
    assert not reg.is_muted, "Register should start as not muted"
    
    reg.mute()
    assert reg.is_muted, "Register should be muted after calling mute()"
    
    reg.unmute()
    assert not reg.is_muted, "Register should be unmuted after calling unmute()"

# Test adding and accessing render functions
def test_add_access_renderfuncs():
    reg = Register()
    reg.renderfuncs['text'] = lambda x: f"Rendered {x}"
    assert 'text' in reg.renderfuncs, "Render function should be added to the dictionary"
    assert reg.renderfuncs['text']("example") == "Rendered example", "The render function should return the expected string"

# Test using lambda functions
def test_lambda_functions():
    reg = Register()
    assert reg.eightbit_call(123) == 123, "Eightbit call should return the input value"
    assert reg.rgb_call(255, 0, 0) == (255, 0, 0), "RGB call should return the specified RGB values"

# Test copying a register
def test_copy():
    reg = Register()
    copied_reg = reg.copy()
    assert isinstance(copied_reg, Register), "The copy should be an instance of the Register class"
    assert copied_reg is not reg, "The copy should be a deepcopy and not reference the original object"

if __name__ == "__main__":
    pytest.main()

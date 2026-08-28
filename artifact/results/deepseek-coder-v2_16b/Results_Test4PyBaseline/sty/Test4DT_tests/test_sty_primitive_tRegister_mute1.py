
import pytest
from sty.primitive import Register, Style

# Test the initialization of the Register class
def test_register_initialization():
    reg = Register()
    assert not reg.is_muted
    assert isinstance(reg.renderfuncs, dict)
    assert reg.renderfuncs == {}
    assert callable(reg.eightbit_call)
    assert callable(reg.rgb_call)

# Test the mute method of the Register class
def test_mute():
    reg = Register()
    reg.mute()
    assert reg.is_muted

# Test that muting a register also mutes any Style attributes
def test_muting_styles():
    class StyleMock:
        pass
    
    reg = Register()
    style_mock = StyleMock()
    setattr(reg, 'some_style_attribute', style_mock)
    

import pytest
from sty.primitive import Register

# Test initialization of the Register class
def test_register_initialization():
    reg = Register()
    assert reg.renderfuncs == {}
    assert not reg.is_muted
    assert reg.eightbit_call(1) == 1
    assert reg.rgb_call(255, 0, 0) == (255, 0, 0)

# Test muting the register
def test_register_mute():
    reg = Register()
    reg.is_muted = True  # This should be a method call to mute the register
    assert reg.is_muted

# Test unmuting the register
def test_register_unmute():
    reg = Register()
    reg.is_muted = True
    reg.unmute()
    assert not reg.is_muted

# Test that only attributes of type Style are reset when unmuting
class CustomClass:
    pass

def test_register_unmute_only_resets_style_attributes():
    class Style:
        pass
    
    reg = Register()
    custom_attr = CustomClass()
    setattr(reg, 'custom_attr', custom_attr)
    assert isinstance(getattr(reg, 'custom_attr'), CustomClass)
    
    reg.is_muted = True
    reg.unmute()
    assert not isinstance(getattr(reg, 'custom_attr'), Style)

# Test unmuting with multiple style attributes
def test_register_unmute_multiple_style_attributes():
    class Style:
        pass
    
    reg = Register()
    setattr(reg, 'style1', Style())
    setattr(reg, 'style2', Style())
    reg.is_muted = True
    reg.unmute()
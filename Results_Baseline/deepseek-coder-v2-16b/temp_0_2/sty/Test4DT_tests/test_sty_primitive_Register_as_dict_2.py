
import pytest
from sty import Register

# Test creating a custom register instance
def test_create_custom_register():
    custom_register = Register()
    assert hasattr(custom_register, 'renderfuncs')
    assert hasattr(custom_register, 'is_muted')
    assert hasattr(custom_register, 'eightbit_call')
    assert hasattr(custom_register, 'rgb_call')
    assert custom_register.renderfuncs == {}
    assert not custom_register.is_muted
    assert callable(custom_register.eightbit_call)
    assert callable(custom_register.rgb_call)

# Test muting the register
def test_mute():
    custom_register = Register()
    custom_register.mute()
    assert custom_register.is_muted

# Test unmuting the register
def test_unmute():
    custom_register = Register()
    custom_register.mute()
    custom_register.unmute()
    assert not custom_register.is_muted

# Test exporting as a dictionary with no attributes
def test_as_dict_no_attributes():
    custom_register = Register()
    dict_repr = custom_register.as_dict()
    expected_keys = ['renderfuncs', 'is_muted', 'eightbit_call', 'rgb_call']
    assert isinstance(dict_repr, dict)
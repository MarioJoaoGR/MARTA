
import pytest
from sty import Register

# Test case for creating a custom register instance
def test_create_custom_register():
    custom_register = Register()
    assert hasattr(custom_register, 'renderfuncs')
    assert isinstance(custom_register.renderfuncs, dict)
    assert not custom_register.renderfuncs  # Ensure it's initially empty
    assert hasattr(custom_register, 'is_muted')
    assert not custom_register.is_muted
    assert hasattr(custom_register, 'eightbit_call')
    assert callable(custom_register.eightbit_call)
    assert hasattr(custom_register, 'rgb_call')
    assert callable(custom_register.rgb_call)

# Test case for muting the register
def test_mute_register():
    custom_register = Register()
    custom_register.is_muted = True
    assert custom_register.is_muted

# Test case for adding a new rendering function to the renderfuncs dictionary
def test_add_render_function():
    custom_register = Register()
    def some_function(x):
        return x * 2
    custom_register.renderfuncs['new_func'] = some_function
    assert 'new_func' in custom_register.renderfuncs
    assert callable(custom_register.renderfuncs['new_func'])

# Test case for exporting the register as a dictionary
def test_export_as_dict():
    register = Register()
    reg_dict = register.as_dict()
    assert isinstance(reg_dict, dict)

# Module: sty.primitive
import pytest
from sty import Register, Renderfuncs, Type, RenderType

# Test creating a custom register and defining a custom render function
def test_create_custom_register():
    custom_register = Register()
    
    def custom_render(x):
        return f"Custom {x}"
    
    # Assign the custom render function to a specific key in renderfuncs
    custom_register.renderfuncs['custom'] = custom_render
    
    # Call the custom render function and check the output
    assert custom_register.renderfuncs['custom']("function") == "Custom function"

# Test setting a specific RenderType for RGB calls
def test_set_rgb_call():
    class CustomRenderType:
        def __call__(self, *args):
            return args
    
    custom_register = Register()
    custom_register.set_rgb_call(CustomRenderType())
    
    # Call the RGB call and check the output
    assert custom_register.rgb_call(10, 42, 255) == (10, 42, 255)

# Test muting and unmuting a register
def test_mute_unmute():
    register = Register()
    
    # Mute the register
    register.mute()
    assert register.is_muted is True
    
    # Unmute the register
    register.unmute()
    assert register.is_muted is False

# Test exporting data from a register as a dictionary and namedtuple
def test_export_data():
    register = Register()
    
    # Export data as a dictionary
    data_dict = register.as_dict()
    assert isinstance(data_dict, dict)
    
    # Export data as a namedtuple
    data_namedtuple = register.as_namedtuple()
    assert isinstance(data_namedtuple, tuple)

# Test copying a register
def test_copy():
    original_register = Register()
    copied_register = original_register.copy()
    
    # Check that the copied register is not the same object as the original
    assert copied_register is not original_register

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_set_rgb_call_0
sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_0.py:4:0: E0611: No name 'Renderfuncs' in module 'sty' (no-name-in-module)
sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_0.py:4:0: E0611: No name 'Type' in module 'sty' (no-name-in-module)

"""
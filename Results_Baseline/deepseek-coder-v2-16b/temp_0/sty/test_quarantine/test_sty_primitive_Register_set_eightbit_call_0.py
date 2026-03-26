
# Module: sty.primitive
import pytest
from sty import Register, Type, RenderType, Callable, Style, bg, fg

# Test creating a custom register instance
def test_create_custom_register():
    custom_register = Register()
    assert hasattr(custom_register, 'renderfuncs')
    assert hasattr(custom_register, 'is_muted')
    assert hasattr(custom_register, 'eightbit_call')
    assert hasattr(custom_register, 'rgb_call')

# Test setting an eight-bit call with a custom render type
def test_set_eightbit_call():
    class CustomRenderType:
        def __call__(self, *args):
            return "Custom Rendered"
    
    custom_register = Register()
    custom_register.renderfuncs['custom'] = lambda x: f"Custom {x}"
    assert callable(custom_register.eightbit_call)
    assert custom_register.eightbit_call("test") == "Custom test"
    
    # Set a new eight-bit call with CustomRenderType
    custom_register.set_eightbit_call(CustomRenderType())
    assert custom_register.eightbit_call("test") == "Custom Rendered"

# Test setting an RGB color call
def test_rgb_color_call():
    custom_register = Register()
    rgb_result = custom_register.rgb_call(255, 0, 0)
    assert rgb_result == (255, 0, 0)

# Test setting a muted state
def test_set_muted():
    custom_register = Register()
    assert not custom_register.is_muted
    custom_register.is_muted = True
    assert custom_register.is_muted

# Test copying a register instance
def test_copy_register():
    custom_register = Register()
    copied_register = custom_register.copy()
    assert isinstance(copied_register, Register)
    assert copied_register is not custom_register

# Test using the Style class with custom registers
def test_style_class_with_custom_registers():
    style = Style(bg.red)
    assert callable(style.renderfuncs['bg'].eightbit_call)
    assert style.renderfuncs['bg'].eightbit_call(144) == "Custom Rendered"

# Test using the fg and bg classes for color manipulation
def test_fg_and_bg_classes():
    custom_register = Register()
    print(f"{custom_register.fg(144)}Text With Custom Color{custom_register.rs}")
    assert callable(custom_register.eightbit_call)
    assert custom_register.eightbit_call("test") == "Custom test"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_set_eightbit_call_0
sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0.py:4:0: E0611: No name 'Type' in module 'sty' (no-name-in-module)
sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0.py:4:0: E0611: No name 'Callable' in module 'sty' (no-name-in-module)
sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0.py:52:20: E1101: Instance of 'Style' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0.py:53:11: E1101: Instance of 'Style' has no 'renderfuncs' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0.py:58:13: E1101: Instance of 'Register' has no 'fg' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0.py:58:60: E1101: Instance of 'Register' has no 'rs' member (no-member)

"""
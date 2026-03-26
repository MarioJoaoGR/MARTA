
# Module: sty.primitive
# test_sty_primitive.py
from sty.primitive import Register

def test_register_initialization():
    reg = Register()
    assert hasattr(reg, 'renderfuncs') and isinstance(reg.renderfuncs, dict), "Expected renderfuncs to be a dictionary"
    assert not reg.is_muted, "Expected is_muted to be False initially"
    assert callable(reg.eightbit_call) and reg.eightbit_call('test') == 'test', "Expected eightbit_call to be a lambda function that returns its input"
    assert callable(reg.rgb_call) and reg.rgb_call(255, 0, 0) == (255, 0, 0), "Expected rgb_call to be a lambda function that returns its input as RGB values"

def test_register_call_method():
    reg = Register()
    assert reg.__call__() == "", "Expected empty string for default muted state"
    
    # Test with an 8-bit color code
    def test_eightbit_call(value):
        return f"\033[38;5;{value}m"

    class CustomRegister(Register):
        def eightbit_call(self, value: int) -> str:
            return test_eightbit_call(value)

    custom_reg = CustomRegister()
    assert custom_reg.__call__(42) == "\033[38;5;42m", "Expected eightbit_call to return ANSI escape code for 8-bit color"
    
    # Test with a string attribute lookup
    class CustomRegisterWithAttr(Register):
        def __init__(self):
            super().__init__()
            self.colors = {'red': "\033[31m"}
        
        def get_color(self, color_name: str) -> str:
            return self.colors.get(color_name, "")
    
    custom_reg_with_attr = CustomRegisterWithAttr()
    assert custom_reg_with_attr.__call__('red') == "\033[31m", "Expected attribute lookup to return ANSI escape code for color"
    
    # Test with an RGB call
    class CustomRegisterRGB(Register):
        def rgb_call(self, r: int, g: int, b: int) -> str:
            return f"\033[38;2;{r};{g};{b}m"
    
    custom_reg_rgb = CustomRegisterRGB()
    assert custom_reg_rgb.__call__(255, 0, 0) == "\033[38;2;255;0;0m", "Expected rgb_call to return ANSI escape code for RGB color"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register___call___1
sty/Test4DT_tests/test_sty_primitive_Register___call___1.py:22:8: E0202: An attribute defined in sty.primitive line 72 hides this method (method-hidden)
sty/Test4DT_tests/test_sty_primitive_Register___call___1.py:42:8: E0202: An attribute defined in sty.primitive line 73 hides this method (method-hidden)

"""
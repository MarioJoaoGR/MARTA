
import pytest
from sty import Style, fg, bg, ef, rs

class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are created from this class. You can use it to create your own custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions for various formats.
        is_muted (bool): Indicates whether the register is muted, meaning its formatting is disabled.
        eightbit_call (lambda): A lambda function to handle 8-bit color values.
        rgb_call (lambda): A lambda function to handle RGB color values.
    
    Methods:
        mute(): Sometimes it is useful to disable the formatting for a register-object. You can do so by invoking this method. When muted, all attributes that are instances of Style will be set to their default values.
    
    Example:
        reg = Register()
        # Create a custom register and use its methods as needed.
        
        # To mute the register:
        reg.mute()
    """
    def __init__(self):
        self.renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def mute(self) -> None:
        """
        Sometimes it is useful to disable the formatting for a register-object. You can
        do so by invoking this method.
        """
        self.is_muted = True

        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, Style):
                setattr(self, attr_name, val.default)

def test_mute_method():
    reg = Register()
    
    # Before muting, check the default values of fg, bg, ef, and rs
    assert reg.fg == fg.default
    assert reg.bg == bg.default
    assert reg.ef == ef.default
    assert reg.rs == rs.default
    
    # Mute the register
    reg.mute()
    
    # After muting, check that all Style attributes are reset to their default values
    assert reg.fg == fg.default
    assert reg.bg == bg.default
    assert reg.ef == ef.default
    assert reg.rs == rs.default

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_mute_0_test_mute_method
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:47:11: E1101: Instance of 'Register' has no 'fg' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:47:21: E1101: Instance of 'FgRegister' has no 'default' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:48:11: E1101: Instance of 'Register' has no 'bg' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:48:21: E1101: Instance of 'BgRegister' has no 'default' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:49:11: E1101: Instance of 'Register' has no 'ef' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:49:21: E1101: Instance of 'EfRegister' has no 'default' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:50:11: E1101: Instance of 'Register' has no 'rs' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:50:21: E1101: Instance of 'RsRegister' has no 'default' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:56:11: E1101: Instance of 'Register' has no 'fg' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:56:21: E1101: Instance of 'FgRegister' has no 'default' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:57:11: E1101: Instance of 'Register' has no 'bg' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:57:21: E1101: Instance of 'BgRegister' has no 'default' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:58:11: E1101: Instance of 'Register' has no 'ef' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:58:21: E1101: Instance of 'EfRegister' has no 'default' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:59:11: E1101: Instance of 'Register' has no 'rs' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:59:21: E1101: Instance of 'RsRegister' has no 'default' member (no-member)


"""
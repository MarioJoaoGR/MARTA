
import pytest
from sty import primitive

class Register:
    """
    The base Register class from which default registers such as fg, bg, ef, and rs are created. This class can be used to create custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions for the register.
        is_muted (bool): Indicates whether the register is muted.
        eightbit_call (lambda): A lambda function that takes one argument and returns it.
        rgb_call (lambda): A lambda function that takes three arguments (red, green, blue) and returns a tuple of these values.
    
    Examples:
        To create a custom register, you can instantiate the Register class::
        
            custom_register = Register()
            
        You can then use this custom register for various purposes in your application.
    """
    def __init__(self):
        self.renderfuncs: Renderfuncs = {}
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
                setattr(self, attr_name, val)

# Test case for mute method with no input
def test_mute_no_input():
    reg = Register()
    assert not reg.is_muted
    reg.mute()
    assert reg.is_muted

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_mute_5_test_edge_case
sty/Test4DT_tests/test_sty_primitive_Register_mute_5_test_edge_case.py:23:26: E0602: Undefined variable 'Renderfuncs' (undefined-variable)
sty/Test4DT_tests/test_sty_primitive_Register_mute_5_test_edge_case.py:37:31: E0602: Undefined variable 'Style' (undefined-variable)


"""
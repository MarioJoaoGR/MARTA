
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

# Assuming the `Style` class is defined somewhere in the module 'sty.primitive'
class Style:
    pass

Renderfuncs = dict

def test_error_case():
    reg = Register()
    
    # Test raising ValueError for invalid inputs
    with pytest.raises(ValueError):
        reg.mute("invalid input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_mute_1_test_error_case
sty/Test4DT_tests/test_sty_primitive_Register_mute_1_test_error_case.py:51:8: E1121: Too many positional arguments for method call (too-many-function-args)


"""

import pytest
from sty import primitive as sp

class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are created from this class. You can use it to create your own custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions.
        is_muted (bool): Indicates whether the register is muted.
        eightbit_call (lambda): A lambda function for handling 8-bit color calls.
        rgb_call (lambda): A lambda function for handling RGB color calls.
    
    Methods:
        unmute(): Use this method to unmute a previously muted register object.
    
    Example:
        To create a custom register, you can instantiate the Register class and call its methods as needed. For example:
        
        ```python
        custom_register = Register()
        custom_register.unmute()  # This will unmute the register.
        ```
    
    """
    def __init__(self):
        self.renderfuncs: Renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def unmute(self) -> None:
        """
        Use this method to unmute a previously muted register object.
        """
        self.is_muted = False

        for attr_name in dir(self):
            val = getattr(self, attr_name)
            if isinstance(val, sp.Style):
                setattr(self, attr_name, val)

def test_valid_input():
    custom_register = Register()
    assert not custom_register.is_muted  # Initially, the register should be unmuted
    
    custom_register.unmute()  # Call the unmute method to mute the register
    assert not custom_register.is_muted  # After unmuting, the register should still be unmuted

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_unmute_0_test_valid_input
sty/Test4DT_tests/test_sty_primitive_Register_unmute_0_test_valid_input.py:28:26: E0602: Undefined variable 'Renderfuncs' (undefined-variable)


"""
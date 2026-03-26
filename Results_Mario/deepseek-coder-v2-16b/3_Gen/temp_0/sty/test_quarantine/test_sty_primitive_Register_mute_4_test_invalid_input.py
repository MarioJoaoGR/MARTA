
import pytest
from sty import primitive as Style

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
                setattr(self, attr_name, val)

def test_invalid_input():
    reg = Register()
    
    # Test mute method with invalid input (should not raise an error)
    reg.mute()
    assert reg.is_muted is True
    
    # Ensure other attributes are not affected by the mute method
    for attr_name in dir(reg):
        if attr_name != 'is_muted':
            val = getattr(reg, attr_name)
            assert isinstance(val, Style) or callable(val), f"Attribute {attr_name} is not set to its default value."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_mute_4_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        reg = Register()
    
        # Test mute method with invalid input (should not raise an error)
>       reg.mute()

sty/Test4DT_tests/test_sty_primitive_Register_mute_4_test_invalid_input.py:47: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_sty_primitive_Register_mute_4_test_invalid_input.Register object at 0x105a46320>

    def mute(self) -> None:
        """
        Sometimes it is useful to disable the formatting for a register-object. You can
        do so by invoking this method.
        """
        self.is_muted = True
    
        for attr_name in dir(self):
            val = getattr(self, attr_name)
>           if isinstance(val, Style):
E           TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

sty/Test4DT_tests/test_sty_primitive_Register_mute_4_test_invalid_input.py:40: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_mute_4_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""
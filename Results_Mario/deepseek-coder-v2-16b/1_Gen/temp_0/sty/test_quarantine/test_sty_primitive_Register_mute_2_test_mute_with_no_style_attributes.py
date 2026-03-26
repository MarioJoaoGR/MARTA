
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

def test_mute_with_no_style_attributes():
    reg = Register()
    assert not reg.is_muted  # Ensure the register is not muted initially
    
    reg.mute()  # Mute the register
    assert reg.is_muted  # Check if the register is now muted
    
    # Verify that no style attributes are reset to their default values
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, Style):
            assert val == getattr(Style, attr_name)  # Ensure the attribute is not changed

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

sty/Test4DT_tests/test_sty_primitive_Register_mute_2_test_mute_with_no_style_attributes.py F [100%]

=================================== FAILURES ===================================
______________________ test_mute_with_no_style_attributes ______________________

    def test_mute_with_no_style_attributes():
        reg = Register()
        assert not reg.is_muted  # Ensure the register is not muted initially
    
>       reg.mute()  # Mute the register

sty/Test4DT_tests/test_sty_primitive_Register_mute_2_test_mute_with_no_style_attributes.py:47: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_sty_primitive_Register_mute_2_test_mute_with_no_style_attributes.Register object at 0x103b216c0>

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

sty/Test4DT_tests/test_sty_primitive_Register_mute_2_test_mute_with_no_style_attributes.py:40: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_mute_2_test_mute_with_no_style_attributes.py::test_mute_with_no_style_attributes
============================== 1 failed in 0.02s ===============================

"""

import pytest
from sty import primitive as Style

class Register:
    """
    The base Register class from which default registers such as fg, bg, ef, and rs are created. This class can be used to create custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions.
        is_muted (bool): Indicates whether the register is muted.
        eightbit_call (lambda): A lambda function for handling 8-bit color values.
        rgb_call (lambda): A lambda function for handling RGB color values.
    
    Methods:
        unmute(): Use this method to unmute a previously muted register object. When called, it will reset the muted attributes to their original state by iterating over all attributes and setting them back if they are instances of Style.
    
    Example:
        To create a custom register, you can instantiate the Register class::
        
            custom_register = Register()
            # Now you can use custom_register for your specific needs.
            
        To unmute a previously muted register, call the `unmute` method::
        
            custom_register.unmute()
    
    The `unmute` method is designed to reverse the muting process of the Register class, allowing it to regain its original functionality by resetting any attributes that were set to muted states back to their default or overridden values. This ensures that the register object operates as intended without any unintended restrictions.
    """
    def __init__(self):
        self.renderfuncs = {}
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
            if isinstance(val, Style):
                setattr(self, attr_name, val)

def test_edge_case():
    custom_register = Register()
    assert not custom_register.is_muted  # Ensure the register is initially unmuted
    
    custom_register.unmute()  # Attempt to unmute an already unmuted register
    assert not custom_register.is_muted  # Ensure the register remains unmuted after attempting to unmute it again

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

sty/Test4DT_tests/test_sty_primitive_Register_unmute_7_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        custom_register = Register()
        assert not custom_register.is_muted  # Ensure the register is initially unmuted
    
>       custom_register.unmute()  # Attempt to unmute an already unmuted register

sty/Test4DT_tests/test_sty_primitive_Register_unmute_7_test_edge_case.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_sty_primitive_Register_unmute_7_test_edge_case.Register object at 0x104146ef0>

    def unmute(self) -> None:
        """
        Use this method to unmute a previously muted register object.
        """
        self.is_muted = False
    
        for attr_name in dir(self):
            val = getattr(self, attr_name)
>           if isinstance(val, Style):
E           TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

sty/Test4DT_tests/test_sty_primitive_Register_unmute_7_test_edge_case.py:44: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_unmute_7_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""
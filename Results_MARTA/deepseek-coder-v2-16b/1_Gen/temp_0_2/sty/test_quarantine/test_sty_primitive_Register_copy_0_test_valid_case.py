
from sty.primitive import Renderfuncs  # Correctly importing from 'sty.primitive'
import pytest
from copy import deepcopy

class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are created from this class. You can use it to create your own custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions.
        is_muted (bool): Indicates whether the register is muted.
        eightbit_call (lambda): A lambda function for handling 8-bit color values.
        rgb_call (lambda): A lambda function for handling RGB color values.
    
    Methods:
        copy(): Make a deepcopy of a register-object.
        
        Returns:
            Register: A deepcopy of the current register object.
    
    Example:
        To create a custom register, you can instantiate the Register class and customize its attributes as needed. For example:
        
        ```python
        custom_register = Register()
        custom_register.is_muted = True
        custom_register.rgb_call = lambda r, g, b: (r + 10, g + 10, b + 10)
        ```
    """
    def __init__(self):
        self.renderfuncs: Renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def copy(self) -> "Register":
        """
        Make a deepcopy of a register-object.
        
        Returns:
            Register: A deepcopy of the current register object.
        """
        return deepcopy(self)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================
"""

import pytest
from sty.lib import unmute

# Define a simple base class for testing
class Register:
    def __init__(self):
        self.is_muted = False
    
    def unmute(self):
        self.is_muted = True

class AnotherRegisterSubclass(Register):
    pass

# Test cases for the unmute function
def test_unmute_multiple_objects():
    obj1 = Register()
    obj2 = AnotherRegisterSubclass()
    unmute(obj1, obj2)
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

sty/Test4DT_tests/test_sty_lib_unmute_0.py F                             [100%]

=================================== FAILURES ===================================
_________________________ test_unmute_multiple_objects _________________________

    def test_unmute_multiple_objects():
        obj1 = Register()
        obj2 = AnotherRegisterSubclass()
>       unmute(obj1, obj2)

sty/Test4DT_tests/test_sty_lib_unmute_0.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

objects = (<Test4DT_tests.test_sty_lib_unmute_0.Register object at 0x106502590>, <Test4DT_tests.test_sty_lib_unmute_0.AnotherRegisterSubclass object at 0x106516350>)
err = ValueError("The unmute() method can only be used with objects that inherit from the 'Register class'.")
obj = <Test4DT_tests.test_sty_lib_unmute_0.Register object at 0x106502590>

    def unmute(*objects: Register) -> None:
        """
        Use this function to unmute multiple register-objects at once.
    
        :param objects: Pass multiple register-objects to the function.
        """
        err = ValueError(
            "The unmute() method can only be used with objects that inherit "
            "from the 'Register class'."
        )
        for obj in objects:
            if not isinstance(obj, Register):
>               raise err
E               ValueError: The unmute() method can only be used with objects that inherit from the 'Register class'.

sty/sty/lib.py:36: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_lib_unmute_0.py::test_unmute_multiple_objects
============================== 1 failed in 0.01s ===============================

"""
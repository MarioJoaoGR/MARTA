
import pytest
from collections import namedtuple
from sty.primitive import Register

def test_valid_inputs():
    custom_register = Register()
    style_register = custom_register.as_namedtuple()
    
    assert isinstance(style_register, namedtuple), f"Expected a namedtuple but got {type(style_register)}"

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

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        custom_register = Register()
        style_register = custom_register.as_namedtuple()
    
>       assert isinstance(style_register, namedtuple), f"Expected a namedtuple but got {type(style_register)}"
E       TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_valid_inputs.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.02s ===============================
"""
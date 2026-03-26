
import pytest
from sty.primitive import Register
from collections import namedtuple

def test_edge_case():
    # Create an instance of Register with all attributes set to None or empty values
    register = Register()
    
    # Call the as_namedtuple method
    style_register = register.as_namedtuple()
    
    # Define expected namedtuple fields and their default values
    expected_fields = {
        'renderfuncs': {},
        'is_muted': False,
        'eightbit_call': lambda x: x,
        'rgb_call': lambda r, g, b: (r, g, b)
    }
    
    # Create the expected namedtuple from the fields dictionary
    ExpectedStyleRegister = namedtuple("StyleRegister", expected_fields.keys())(**expected_fields)
    
    # Assert that the returned namedtuple matches the expected one
    assert style_register == ExpectedStyleRegister

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

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create an instance of Register with all attributes set to None or empty values
        register = Register()
    
        # Call the as_namedtuple method
        style_register = register.as_namedtuple()
    
        # Define expected namedtuple fields and their default values
        expected_fields = {
            'renderfuncs': {},
            'is_muted': False,
            'eightbit_call': lambda x: x,
            'rgb_call': lambda r, g, b: (r, g, b)
        }
    
        # Create the expected namedtuple from the fields dictionary
        ExpectedStyleRegister = namedtuple("StyleRegister", expected_fields.keys())(**expected_fields)
    
        # Assert that the returned namedtuple matches the expected one
>       assert style_register == ExpectedStyleRegister
E       assert StyleRegister() == StyleRegister... 0x104054ca0>)
E         
E         Right contains 4 more items, first extra item: {}
E         Use -v to get more diff

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_edge_case.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================

"""
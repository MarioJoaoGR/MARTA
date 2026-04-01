
import pytest
from sty.primitive import Register
from collections import namedtuple

def test_valid_inputs():
    register = Register()
    
    # Test that as_dict method returns a dictionary without private attributes
    result = register.as_dict()
    assert isinstance(result, dict)
    for key in result:
        assert not key.startswith("_")
        assert isinstance(getattr(register, key), str)
    
    # Test that as_namedtuple method returns a namedtuple with correct field names
    nt = register.as_namedtuple()
    assert isinstance(nt, tuple)  # Check if it's a tuple first
    assert all(isinstance(getattr(nt, key), str) for key in dir(register) if not key.startswith("_"))

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

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        register = Register()
    
        # Test that as_dict method returns a dictionary without private attributes
        result = register.as_dict()
        assert isinstance(result, dict)
        for key in result:
            assert not key.startswith("_")
            assert isinstance(getattr(register, key), str)
    
        # Test that as_namedtuple method returns a namedtuple with correct field names
        nt = register.as_namedtuple()
        assert isinstance(nt, tuple)  # Check if it's a tuple first
>       assert all(isinstance(getattr(nt, key), str) for key in dir(register) if not key.startswith("_"))

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_2_test_valid_inputs.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x1024da650>

>   assert all(isinstance(getattr(nt, key), str) for key in dir(register) if not key.startswith("_"))
E   AttributeError: 'StyleRegister' object has no attribute 'as_dict'. Did you mean: '_asdict'?

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_2_test_valid_inputs.py:19: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.03s ===============================
"""
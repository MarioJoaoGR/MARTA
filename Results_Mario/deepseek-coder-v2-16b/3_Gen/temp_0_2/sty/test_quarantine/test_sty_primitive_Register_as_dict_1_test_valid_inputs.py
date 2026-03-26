
import pytest
from sty.primitive import Register

def test_valid_inputs():
    register = Register()
    # Call the as_dict method and check if it returns a dictionary
    result = register.as_dict()
    
    # Check that the returned object is indeed a dictionary
    assert isinstance(result, dict)
    
    # Check specific keys in the dictionary for their string representations
    assert "is_muted" in result

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

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        register = Register()
        # Call the as_dict method and check if it returns a dictionary
        result = register.as_dict()
    
        # Check that the returned object is indeed a dictionary
        assert isinstance(result, dict)
    
        # Check specific keys in the dictionary for their string representations
>       assert "is_muted" in result
E       AssertionError: assert 'is_muted' in {}

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_valid_inputs.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.03s ===============================
"""

import pytest
from dataclasses_json.utils import _isinstance_safe

def test_valid_inputs():
    # Test case 1: Check if an object is an instance of a given type
    assert _isinstance_safe([1, 2, 3], list) == True
    
    # Test case 2: Check if an object is an instance of another type
    assert _isinstance_safe(42, int) == True
    
    # Test case 3: Check if an object is not an instance of a given type
    assert _isinstance_safe("hello", int) == False
    
    # Test case 4: Check if an object is an instance of any one of multiple types
    assert _isinstance_safe(None, (int, str)) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test case 1: Check if an object is an instance of a given type
        assert _isinstance_safe([1, 2, 3], list) == True
    
        # Test case 2: Check if an object is an instance of another type
        assert _isinstance_safe(42, int) == True
    
        # Test case 3: Check if an object is not an instance of a given type
        assert _isinstance_safe("hello", int) == False
    
        # Test case 4: Check if an object is an instance of any one of multiple types
>       assert _isinstance_safe(None, (int, str)) == True
E       AssertionError: assert False == True
E        +  where False = _isinstance_safe(None, (<class 'int'>, <class 'str'>))

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_inputs.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.03s ===============================
"""
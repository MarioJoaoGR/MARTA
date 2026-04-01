
import pytest
from dataclasses_json.utils import _is_new_type

def test_valid_class():
    class MyClass: pass
    
    # Check if MyClass is a new-style class or function
    assert _is_new_type(MyClass) == True, "Expected MyClass to be identified as a new-style class"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_1_test_valid_class.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_class _______________________________

    def test_valid_class():
        class MyClass: pass
    
        # Check if MyClass is a new-style class or function
>       assert _is_new_type(MyClass) == True, "Expected MyClass to be identified as a new-style class"
E       AssertionError: Expected MyClass to be identified as a new-style class
E       assert False == True
E        +  where False = _is_new_type(<class 'Test4DT_tests.test_dataclasses_json_utils__is_new_type_1_test_valid_class.test_valid_class.<locals>.MyClass'>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_1_test_valid_class.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_1_test_valid_class.py::test_valid_class
============================== 1 failed in 0.03s ===============================
"""
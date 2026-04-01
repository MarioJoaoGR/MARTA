
import pytest
from dataclasses_json.utils import _is_new_type

def test_valid_case_class():
    class MyClass: pass
    
    # Check if the function correctly identifies a new-style class
    assert _is_new_type(MyClass) is True, "Expected _is_new_type to return True for a new-style class"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_case_class.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_case_class _____________________________

    def test_valid_case_class():
        class MyClass: pass
    
        # Check if the function correctly identifies a new-style class
>       assert _is_new_type(MyClass) is True, "Expected _is_new_type to return True for a new-style class"
E       AssertionError: Expected _is_new_type to return True for a new-style class
E       assert False is True
E        +  where False = _is_new_type(<class 'Test4DT_tests.test_dataclasses_json_utils__is_new_type_0_test_valid_case_class.test_valid_case_class.<locals>.MyClass'>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_case_class.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_case_class.py::test_valid_case_class
============================== 1 failed in 0.03s ===============================
"""
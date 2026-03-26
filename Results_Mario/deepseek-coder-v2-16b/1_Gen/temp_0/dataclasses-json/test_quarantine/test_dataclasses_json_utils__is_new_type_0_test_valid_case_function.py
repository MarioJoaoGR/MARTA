
import inspect
from dataclasses_json.utils import _is_new_type

def test_valid_case_function():
    # Test a valid new-style class
    class MyClass: pass
    assert _is_new_type(MyClass) == True

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_case_function.py F [100%]

=================================== FAILURES ===================================
___________________________ test_valid_case_function ___________________________

    def test_valid_case_function():
        # Test a valid new-style class
        class MyClass: pass
>       assert _is_new_type(MyClass) == True
E       AssertionError: assert False == True
E        +  where False = _is_new_type(<class 'Test4DT_tests.test_dataclasses_json_utils__is_new_type_0_test_valid_case_function.test_valid_case_function.<locals>.MyClass'>)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_case_function.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_case_function.py::test_valid_case_function
============================== 1 failed in 0.03s ===============================

"""
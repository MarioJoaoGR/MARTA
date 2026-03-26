
from dataclasses_json.utils import _isinstance_safe

def test_valid_input():
    # Test cases where the object is an instance of the provided type or tuple of types
    assert _isinstance_safe(42, int) == True
    assert _isinstance_safe("hello", str) == True
    assert _isinstance_safe(3.14, (int, float)) == True
    assert _isinstance_safe([], (list, tuple)) == False

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test cases where the object is an instance of the provided type or tuple of types
        assert _isinstance_safe(42, int) == True
        assert _isinstance_safe("hello", str) == True
        assert _isinstance_safe(3.14, (int, float)) == True
>       assert _isinstance_safe([], (list, tuple)) == False
E       AssertionError: assert True == False
E        +  where True = _isinstance_safe([], (<class 'list'>, <class 'tuple'>))

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""
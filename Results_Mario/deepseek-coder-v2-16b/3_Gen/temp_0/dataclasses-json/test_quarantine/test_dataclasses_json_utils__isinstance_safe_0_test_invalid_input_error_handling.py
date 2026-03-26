
import pytest
from dataclasses_json.utils import _isinstance_safe

def test_invalid_input_error_handling():
    with pytest.raises(TypeError):
        assert _isinstance_safe([1, 2, 3], [list, tuple])

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        with pytest.raises(TypeError):
>           assert _isinstance_safe([1, 2, 3], [list, tuple])
E           AssertionError: assert False
E            +  where False = _isinstance_safe([1, 2, 3], [<class 'list'>, <class 'tuple'>])

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_invalid_input_error_handling.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__isinstance_safe_0_test_invalid_input_error_handling.py::test_invalid_input_error_handling
============================== 1 failed in 0.03s ===============================
"""
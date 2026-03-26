
import pytest
from dataclasses_json.utils import _is_new_type
import inspect

def test_invalid_input():
    with pytest.raises(TypeError):
        assert _is_new_type(123)  # Providing an invalid input type to trigger TypeError

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           assert _is_new_type(123)  # Providing an invalid input type to trigger TypeError
E           assert False
E            +  where False = _is_new_type(123)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_invalid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""

import pytest
from dataclasses_json.utils import _hasargs

def test_invalid_input():
    with pytest.raises(TypeError):
        assert _hasargs(int, "arg1", "arg2")  # int does not have __args__ attribute

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           assert _hasargs(int, "arg1", "arg2")  # int does not have __args__ attribute
E           AssertionError: assert False
E            +  where False = _hasargs(int, 'arg1', 'arg2')

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_invalid_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""
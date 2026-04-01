
import pytest
from dataclasses_json.utils import _handle_undefined_parameters_safe, _undefined_parameter_action_safe

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test case for invalid usage input
        _handle_undefined_parameters_safe(cls=None, kvs={}, usage="invalid")

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_invalid_inputs.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__handle_undefined_parameters_safe_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""
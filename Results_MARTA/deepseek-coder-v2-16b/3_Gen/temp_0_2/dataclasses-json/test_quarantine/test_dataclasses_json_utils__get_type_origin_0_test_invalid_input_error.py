
import pytest
from dataclasses_json.utils import _get_type_origin, _NO_TYPE_ORIGIN
import sys

def test_invalid_input_error():
    # Test with an invalid type that should raise a TypeError
    with pytest.raises(TypeError):
        _get_type_origin(None)  # Passing None as an invalid type

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_invalid_input_error.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_error ___________________________

    def test_invalid_input_error():
        # Test with an invalid type that should raise a TypeError
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_invalid_input_error.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_invalid_input_error.py::test_invalid_input_error
============================== 1 failed in 0.03s ===============================
"""
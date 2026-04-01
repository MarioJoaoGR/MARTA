
import pytest
from dataclasses_json.utils import _is_nonstr_collection

def test_error_handling_invalid_type():
    # Test with an invalid type (not a Type)
    with pytest.raises(TypeError):
        _is_nonstr_collection("invalid_type")

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_nonstr_collection_5_test_error_handling_invalid_type.py F [100%]

=================================== FAILURES ===================================
_______________________ test_error_handling_invalid_type _______________________

    def test_error_handling_invalid_type():
        # Test with an invalid type (not a Type)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_nonstr_collection_5_test_error_handling_invalid_type.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_nonstr_collection_5_test_error_handling_invalid_type.py::test_error_handling_invalid_type
============================== 1 failed in 0.03s ===============================
"""
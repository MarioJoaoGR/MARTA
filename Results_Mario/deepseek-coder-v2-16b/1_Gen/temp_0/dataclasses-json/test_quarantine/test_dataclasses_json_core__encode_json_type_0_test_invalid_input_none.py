
import pytest
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder

def test_invalid_input_none():
    # Test that the function raises a TypeError when given None as input
    with pytest.raises(TypeError):
        _encode_json_type(None)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_invalid_input_none.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        # Test that the function raises a TypeError when given None as input
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_invalid_input_none.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_invalid_input_none.py::test_invalid_input_none
============================== 1 failed in 0.04s ===============================

"""
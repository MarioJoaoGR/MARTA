
import pytest
from dataclasses_json.utils import _hasargs

def test_invalid_type():
    with pytest.raises(TypeError):
        _hasargs(int, 'a')  # This should raise TypeError because 'a' is not an int

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_3_test_invalid_type.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_type _______________________________

    def test_invalid_type():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_3_test_invalid_type.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_3_test_invalid_type.py::test_invalid_type
============================== 1 failed in 0.03s ===============================
"""
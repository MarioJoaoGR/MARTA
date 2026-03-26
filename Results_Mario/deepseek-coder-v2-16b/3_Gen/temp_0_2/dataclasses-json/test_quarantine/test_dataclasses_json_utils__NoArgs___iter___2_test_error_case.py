
import pytest
from dataclasses_json.utils import _NoArgs

def test_error_case():
    no_args = _NoArgs()
    with pytest.raises(ValueError):
        for item in no_args:
            pass  # This will force iteration to ensure the error is raised

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__NoArgs___iter___2_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        no_args = _NoArgs()
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__NoArgs___iter___2_test_error_case.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__NoArgs___iter___2_test_error_case.py::test_error_case
============================== 1 failed in 0.03s ===============================
"""

import pytest
from isort.api import _config, DEFAULT_CONFIG, Config

def test_invalid_empty_path():
    with pytest.raises(ValueError):
        _config()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_api__config_1_test_invalid_empty_path.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_empty_path ____________________________

    def test_invalid_empty_path():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort_api__config_1_test_invalid_empty_path.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__config_1_test_invalid_empty_path.py::test_invalid_empty_path
============================== 1 failed in 0.12s ===============================
"""
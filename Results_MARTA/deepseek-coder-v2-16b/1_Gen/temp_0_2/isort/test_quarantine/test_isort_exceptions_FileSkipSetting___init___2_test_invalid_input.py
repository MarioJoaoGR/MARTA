
import pytest
from isort.exceptions import FileSkipSetting

def test_invalid_input():
    with pytest.raises(FileSkipSetting) as exc_info:
        try:
            raise FileSkipSetting("example/file.py")
        except FileSkipSetting as e:
            pass
    assert str(exc_info.value) == "example/file.py was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

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

isort/Test4DT_tests/test_isort_exceptions_FileSkipSetting___init___2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(FileSkipSetting) as exc_info:
E       Failed: DID NOT RAISE <class 'isort.exceptions.FileSkipSetting'>

isort/Test4DT_tests/test_isort_exceptions_FileSkipSetting___init___2_test_invalid_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_FileSkipSetting___init___2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""
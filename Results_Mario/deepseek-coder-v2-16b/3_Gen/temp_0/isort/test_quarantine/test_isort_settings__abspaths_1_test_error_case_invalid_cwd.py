
import pytest
import os
from isort.settings import _abspaths

@pytest.mark.parametrize("invalid_cwd", [
    "nonexistent/directory",  # Non-existent directory
    "/invalid/absolute/path"   # Absolute path to an invalid location
])
def test_error_case_invalid_cwd(invalid_cwd):
    with pytest.raises(FileNotFoundError):
        _abspaths(invalid_cwd, ["file1.txt"])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_settings__abspaths_1_test_error_case_invalid_cwd.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________ test_error_case_invalid_cwd[nonexistent/directory] ______________

invalid_cwd = 'nonexistent/directory'

    @pytest.mark.parametrize("invalid_cwd", [
        "nonexistent/directory",  # Non-existent directory
        "/invalid/absolute/path"   # Absolute path to an invalid location
    ])
    def test_error_case_invalid_cwd(invalid_cwd):
>       with pytest.raises(FileNotFoundError):
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_settings__abspaths_1_test_error_case_invalid_cwd.py:11: Failed
_____________ test_error_case_invalid_cwd[/invalid/absolute/path] ______________

invalid_cwd = '/invalid/absolute/path'

    @pytest.mark.parametrize("invalid_cwd", [
        "nonexistent/directory",  # Non-existent directory
        "/invalid/absolute/path"   # Absolute path to an invalid location
    ])
    def test_error_case_invalid_cwd(invalid_cwd):
>       with pytest.raises(FileNotFoundError):
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_settings__abspaths_1_test_error_case_invalid_cwd.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_1_test_error_case_invalid_cwd.py::test_error_case_invalid_cwd[nonexistent/directory]
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_1_test_error_case_invalid_cwd.py::test_error_case_invalid_cwd[/invalid/absolute/path]
============================== 2 failed in 0.11s ===============================
"""

import os
from typing import Iterable

def _abspaths(cwd: str, values: Iterable[str]) -> set[str]:
    paths = {
        (
            os.path.join(cwd, value)
            if not value.startswith(os.path.sep) and value.endswith(os.path.sep)
            else value
        )
        for value in values
    }
    return paths

import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        _abspaths("home/user", None)  # Test with invalid iterable type

    with pytest.raises(ValueError):
        _abspaths("home/user", ["folder1/", "file2.txt", ""])  # Test with empty string in values

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

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            _abspaths("home/user", None)  # Test with invalid iterable type
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_invalid_input.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""
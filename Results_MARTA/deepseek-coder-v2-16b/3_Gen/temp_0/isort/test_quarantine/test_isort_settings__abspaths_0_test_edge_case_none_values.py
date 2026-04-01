
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

def test_edge_case_none_values():
    assert _abspaths("home/user", None) == set()

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

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_edge_case_none_values.py F [100%]

=================================== FAILURES ===================================
__________________________ test_edge_case_none_values __________________________

    def test_edge_case_none_values():
>       assert _abspaths("home/user", None) == set()

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_edge_case_none_values.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cwd = 'home/user', values = None

    def _abspaths(cwd: str, values: Iterable[str]) -> set[str]:
>       paths = {
            (
                os.path.join(cwd, value)
                if not value.startswith(os.path.sep) and value.endswith(os.path.sep)
                else value
            )
            for value in values
        }
E       TypeError: 'NoneType' object is not iterable

isort/Test4DT_tests/test_isort_settings__abspaths_0_test_edge_case_none_values.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0_test_edge_case_none_values.py::test_edge_case_none_values
============================== 1 failed in 0.08s ===============================
"""
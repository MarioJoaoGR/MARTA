
import os
from contextlib import contextmanager
from unittest.mock import patch

@contextmanager
def chdir(path: str):
    """Context manager for changing directory and restoring the previous working directory after exit."""
    curdir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(curdir)

def test_chdir():
    with patch('os.getcwd', return_value='/original/path'):
        with patch('os.chdir') as mock_chdir:
            with chdir('/new/directory') as cm:
                assert os.getcwd() == '/new/directory'

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

isort/Test4DT_tests/test_isort_deprecated_finders_chdir_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_chdir __________________________________

    def test_chdir():
        with patch('os.getcwd', return_value='/original/path'):
            with patch('os.chdir') as mock_chdir:
                with chdir('/new/directory') as cm:
>                   assert os.getcwd() == '/new/directory'
E                   AssertionError: assert '/original/path' == '/new/directory'
E                     
E                     - /new/directory
E                     + /original/path

isort/Test4DT_tests/test_isort_deprecated_finders_chdir_0_test_edge_case_none.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_chdir_0_test_edge_case_none.py::test_chdir
============================== 1 failed in 0.08s ===============================
"""

import os
from contextlib import contextmanager
from isort.deprecated.finders import chdir
import pytest

@contextmanager
def temp_chdir(path):
    """Context manager to change directory temporarily."""
    original_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original_cwd)

def test_none_input():
    with temp_chdir('/tmp'):
        assert os.getcwd() == '/tmp'
    # After the context block, the original working directory should be restored
    assert os.getcwd() == os.path.expanduser('~')

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

isort/Test4DT_tests/test_isort_deprecated_finders_chdir_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with temp_chdir('/tmp'):
            assert os.getcwd() == '/tmp'
        # After the context block, the original working directory should be restored
>       assert os.getcwd() == os.path.expanduser('~')
E       AssertionError: assert '/projects/F2...IACDCF2/mario' == '/home/joaovitorino'
E         
E         - /home/joaovitorino
E         + /projects/F202407648IACDCF2/mario

isort/Test4DT_tests/test_isort_deprecated_finders_chdir_1_test_none_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_chdir_1_test_none_input.py::test_none_input
============================== 1 failed in 0.10s ===============================
"""

import os
from contextlib import contextmanager
from isort.deprecated.finders import chdir

@contextmanager
def temp_chdir(path: str):
    """Context manager for changing directory and restoring the previous working directory after exit."""
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

def test_none_input():
    with temp_chdir('/tmp'):
        assert os.getcwd() == '/tmp'
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
>           assert os.getcwd() == os.path.expanduser('~')
E           AssertionError: assert '/tmp' == '/home/joaovitorino'
E             
E             - /home/joaovitorino
E             + /tmp

isort/Test4DT_tests/test_isort_deprecated_finders_chdir_1_test_none_input.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_chdir_1_test_none_input.py::test_none_input
============================== 1 failed in 0.10s ===============================
"""
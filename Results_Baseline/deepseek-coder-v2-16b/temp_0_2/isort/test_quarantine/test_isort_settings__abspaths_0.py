
import os
from typing import Iterable
import pytest

# Import the function from its module
from isort.settings import _abspaths

def test_abspaths_relative_with_cwd():
    result = _abspaths("home/user", ["folder1/", "file.txt"])
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

isort/Test4DT_tests/test_isort_settings__abspaths_0.py F.                [100%]

=================================== FAILURES ===================================
_______________________ test_abspaths_relative_with_cwd ________________________

    def test_abspaths_relative_with_cwd():
        result = _abspaths("home/user", ["folder1/", "file.txt"])
>       assert set(result) == {'home/user/folder1/', 'home/user/file.txt'}
E       AssertionError: assert {'file.txt', ...ser/folder1/'} == {'home/user/f...ser/folder1/'}
E         
E         Extra items in the left set:
E         'file.txt'
E         Extra items in the right set:
E         'home/user/file.txt'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__abspaths_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__abspaths_0.py::test_abspaths_relative_with_cwd
========================= 1 failed, 1 passed in 0.11s ==========================
"""

import os
import sys
import pytest
from isort.utils import exists_case_sensitive

@pytest.mark.parametrize("path, expected", [
    ("C:\\path\\to\\file", True),
    ("C:\\path\\to\\File", False),
    ("/usr/local/bin/script.py", True),
])
def test_valid_input(path, expected):
    assert exists_case_sensitive(path) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_utils_exists_case_sensitive_3_test_valid_input.py F [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
__________________ test_valid_input[C:\\path\\to\\file-True] ___________________

path = 'C:\\path\\to\\file', expected = True

    @pytest.mark.parametrize("path, expected", [
        ("C:\\path\\to\\file", True),
        ("C:\\path\\to\\File", False),
        ("/usr/local/bin/script.py", True),
    ])
    def test_valid_input(path, expected):
>       assert exists_case_sensitive(path) == expected
E       AssertionError: assert False == True
E        +  where False = exists_case_sensitive('C:\\path\\to\\file')

isort/Test4DT_tests/test_isort_utils_exists_case_sensitive_3_test_valid_input.py:13: AssertionError
_______________ test_valid_input[/usr/local/bin/script.py-True] ________________

path = '/usr/local/bin/script.py', expected = True

    @pytest.mark.parametrize("path, expected", [
        ("C:\\path\\to\\file", True),
        ("C:\\path\\to\\File", False),
        ("/usr/local/bin/script.py", True),
    ])
    def test_valid_input(path, expected):
>       assert exists_case_sensitive(path) == expected
E       AssertionError: assert False == True
E        +  where False = exists_case_sensitive('/usr/local/bin/script.py')

isort/Test4DT_tests/test_isort_utils_exists_case_sensitive_3_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_utils_exists_case_sensitive_3_test_valid_input.py::test_valid_input[C:\\path\\to\\file-True]
FAILED isort/Test4DT_tests/test_isort_utils_exists_case_sensitive_3_test_valid_input.py::test_valid_input[/usr/local/bin/script.py-True]
========================= 2 failed, 1 passed in 0.12s ==========================
"""
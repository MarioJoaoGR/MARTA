
import pytest
from isort.comments import add_to_line

def test_empty_original_string():
    assert add_to_line(['This is comment 1', 'This is comment 2'], original_string='', removed=False) == ''

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

isort/Test4DT_tests/test_isort_comments_add_to_line_1_test_empty_original_string.py F [100%]

=================================== FAILURES ===================================
__________________________ test_empty_original_string __________________________

    def test_empty_original_string():
>       assert add_to_line(['This is comment 1', 'This is comment 2'], original_string='', removed=False) == ''
E       AssertionError: assert ' This is com... is comment 2' == ''
E         
E         +  This is comment 1; This is comment 2

isort/Test4DT_tests/test_isort_comments_add_to_line_1_test_empty_original_string.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_comments_add_to_line_1_test_empty_original_string.py::test_empty_original_string
============================== 1 failed in 0.10s ===============================
"""
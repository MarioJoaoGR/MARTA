
import pytest
from isort.comments import add_to_line

def test_empty_list():
    assert add_to_line(None, "original string", removed=False) == "original string"
    assert add_to_line([], "original string", removed=False) == "original string"
    assert add_to_line(['comment1'], "original string", removed=False) == "original string  # comment1"

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

isort/Test4DT_tests/test_isort_comments_add_to_line_0_test_empty_list.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_empty_list ________________________________

    def test_empty_list():
        assert add_to_line(None, "original string", removed=False) == "original string"
        assert add_to_line([], "original string", removed=False) == "original string"
>       assert add_to_line(['comment1'], "original string", removed=False) == "original string  # comment1"
E       AssertionError: assert 'original string comment1' == 'original string  # comment1'
E         
E         - original string  # comment1
E         ?                ---
E         + original string comment1

isort/Test4DT_tests/test_isort_comments_add_to_line_0_test_empty_list.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_comments_add_to_line_0_test_empty_list.py::test_empty_list
============================== 1 failed in 0.10s ===============================
"""
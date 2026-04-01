
import pytest
from isort.format import remove_whitespace

def test_valid_input_with_separator():
    assert remove_whitespace("Hello, World!") == "Hello,World!"
    assert remove_whitespace("This is a test.", line_separator=".") == "Thisisatest."

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

isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_valid_input_with_separator.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_with_separator ________________________

    def test_valid_input_with_separator():
        assert remove_whitespace("Hello, World!") == "Hello,World!"
>       assert remove_whitespace("This is a test.", line_separator=".") == "Thisisatest."
E       AssertionError: assert 'Thisisatest' == 'Thisisatest.'
E         
E         - Thisisatest.
E         ?            -
E         + Thisisatest

isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_valid_input_with_separator.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_valid_input_with_separator.py::test_valid_input_with_separator
============================== 1 failed in 0.11s ===============================
"""
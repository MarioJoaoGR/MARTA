
import pytest
from isort.output import _normalize_empty_lines

def test_error_case_non_string_elements():
    with pytest.raises(TypeError):
        _normalize_empty_lines(['line1', '', 123, ''])

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

isort/Test4DT_tests/test_isort_output__normalize_empty_lines_1_test_error_case_non_string_elements.py F [100%]

=================================== FAILURES ===================================
_____________________ test_error_case_non_string_elements ______________________

    def test_error_case_non_string_elements():
        with pytest.raises(TypeError):
>           _normalize_empty_lines(['line1', '', 123, ''])

isort/Test4DT_tests/test_isort_output__normalize_empty_lines_1_test_error_case_non_string_elements.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

lines = ['line1', '', 123]

    def _normalize_empty_lines(lines: list[str]) -> list[str]:
>       while lines and lines[-1].strip() == "":
E       AttributeError: 'int' object has no attribute 'strip'

isort/isort/output.py:651: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_output__normalize_empty_lines_1_test_error_case_non_string_elements.py::test_error_case_non_string_elements
============================== 1 failed in 0.12s ===============================
"""
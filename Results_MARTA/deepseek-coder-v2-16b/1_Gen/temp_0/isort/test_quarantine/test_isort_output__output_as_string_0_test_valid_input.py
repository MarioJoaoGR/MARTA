
import pytest
from isort.output import _output_as_string, _normalize_empty_lines

def test_valid_input():
    # Test with normal input
    assert _output_as_string(["line1", "line2"], "\n") == 'line1\nline2\n'
    
    # Test with empty lines at the end
    assert _output_as_string(["line1", "", "", "line2"], " ") == 'line1  line2 '

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

isort/Test4DT_tests/test_isort_output__output_as_string_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Test with normal input
        assert _output_as_string(["line1", "line2"], "\n") == 'line1\nline2\n'
    
        # Test with empty lines at the end
>       assert _output_as_string(["line1", "", "", "line2"], " ") == 'line1  line2 '
E       AssertionError: assert 'line1   line2 ' == 'line1  line2 '
E         
E         - line1  line2 
E         + line1   line2 
E         ?        +

isort/Test4DT_tests/test_isort_output__output_as_string_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_output__output_as_string_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""
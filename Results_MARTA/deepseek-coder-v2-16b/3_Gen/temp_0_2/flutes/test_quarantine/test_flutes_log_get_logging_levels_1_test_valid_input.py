
import pytest
from flutes.log import get_logging_levels  # Assuming this is the correct module and function

def test_valid_input():
    levels = get_logging_levels()
    assert isinstance(levels, list), "The result should be a list"
    assert all(isinstance(level, str) for level in levels), "All items in the list should be strings"
    expected_levels = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']
    assert set(levels) == set(expected_levels), f"Expected {expected_levels}, but got {levels}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        levels = get_logging_levels()
        assert isinstance(levels, list), "The result should be a list"
        assert all(isinstance(level, str) for level in levels), "All items in the list should be strings"
        expected_levels = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']
>       assert set(levels) == set(expected_levels), f"Expected {expected_levels}, but got {levels}"
E       AssertionError: Expected ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], but got ['success', 'warning', 'error', 'info', 'quiet']
E       assert {'error', 'in...s', 'warning'} == {'CRITICAL', ...O', 'WARNING'}
E         
E         Extra items in the left set:
E         'warning'
E         'quiet'
E         'success'
E         'error'
E         'info'...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_1_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_logging_levels_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""
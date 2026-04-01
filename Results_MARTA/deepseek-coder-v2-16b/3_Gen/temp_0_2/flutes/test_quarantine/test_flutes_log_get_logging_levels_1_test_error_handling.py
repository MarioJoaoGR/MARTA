
import pytest
from flutes.log import get_logging_levels  # Assuming this module contains the function

@pytest.mark.parametrize("expected_levels", [
    (['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']),
])
def test_error_handling(expected_levels):
    levels = get_logging_levels()
    assert set(levels) == set(expected_levels), f"Expected {set(expected_levels)}, but got {set(levels)}"

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

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_1_test_error_handling.py F [100%]

=================================== FAILURES ===================================
____________________ test_error_handling[expected_levels0] _____________________

expected_levels = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']

    @pytest.mark.parametrize("expected_levels", [
        (['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']),
    ])
    def test_error_handling(expected_levels):
        levels = get_logging_levels()
>       assert set(levels) == set(expected_levels), f"Expected {set(expected_levels)}, but got {set(levels)}"
E       AssertionError: Expected {'WARNING', 'ERROR', 'CRITICAL', 'INFO', 'DEBUG'}, but got {'success', 'quiet', 'warning', 'error', 'info'}
E       assert {'error', 'in...s', 'warning'} == {'CRITICAL', ...O', 'WARNING'}
E         
E         Extra items in the left set:
E         'success'
E         'quiet'
E         'warning'
E         'error'
E         'info'...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_1_test_error_handling.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_logging_levels_1_test_error_handling.py::test_error_handling[expected_levels0]
============================== 1 failed in 0.10s ===============================
"""
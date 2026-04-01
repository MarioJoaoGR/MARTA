
import pytest
from flutes.log import get_logging_levels, LoggingLevel

@pytest.mark.valid_input
def test_valid_input():
    levels = get_logging_levels()
    expected_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    assert sorted(levels) == sorted(expected_levels)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    @pytest.mark.valid_input
    def test_valid_input():
        levels = get_logging_levels()
        expected_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
>       assert sorted(levels) == sorted(expected_levels)
E       AssertionError: assert ['error', 'in...s', 'warning'] == ['CRITICAL', ...O', 'WARNING']
E         
E         At index 0 diff: 'error' != 'CRITICAL'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py:9: AssertionError
=============================== warnings summary ===============================
flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py:5
  /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py:5: PytestUnknownMarkWarning: Unknown pytest.mark.valid_input - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.valid_input

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py::test_valid_input
========================= 1 failed, 1 warning in 0.09s =========================

"""
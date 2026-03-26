
import pytest
from flutes.log import get_logging_levels  # Assuming the module is named 'flutes.log'

@pytest.mark.parametrize("expected", [['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']])
def test_valid_input(expected):
    assert get_logging_levels() == expected

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

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input[expected0] __________________________

expected = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']

    @pytest.mark.parametrize("expected", [['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']])
    def test_valid_input(expected):
>       assert get_logging_levels() == expected
E       AssertionError: assert ['success', '...nfo', 'quiet'] == ['CRITICAL', ...NFO', 'DEBUG']
E         
E         At index 0 diff: 'success' != 'CRITICAL'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_get_logging_levels_0_test_valid_input.py::test_valid_input[expected0]
============================== 1 failed in 0.08s ===============================
"""

import pytest
from unittest.mock import patch
from codetiming._timer import Timer, TimerError

def test_start():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.start()

def test_start_with_name():
    timer = Timer(name="test")
    with patch('builtins.print') as mock_logger:
        timer.logger = mock_logger
        timer.initial_text = "Timer {name} started"
        
        timer.start()
        assert timer._start_time is not None, "Start time should be set when the timer starts."
        mock_logger.assert_called_with("Timer test started")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_3_test_edge_cases.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
__________________________________ test_start __________________________________

    def test_start():
        timer = Timer()
>       with pytest.raises(TimerError):
E       Failed: DID NOT RAISE <class 'codetiming._timer.TimerError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_3_test_edge_cases.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_3_test_edge_cases.py::test_start
========================= 1 failed, 1 passed in 0.02s ==========================
"""

import pytest
from unittest.mock import patch, MagicMock
from codetiming._timer import Timer
import time

@pytest.fixture(autouse=True)
def reset_timers():
    Timer.timers.clear()

def test_start_with_initial_text():
    with patch('builtins.print') as mock_print:
        timer = Timer(name="TestTimer", initial_text="Initial text for {name}")
        with timer:
            pass
        assert mock_print.call_count == 1
        expected_output = "Initial text for TestTimer"
        mock_print.assert_called_with(expected_output)

def test_start_without_initial_text():
    with patch('builtins.print') as mock_print:
        timer = Timer(name="TestTimer")
        with timer:
            pass
        assert mock_print.call_count == 1
        expected_output = "Timer TestTimer started"
        mock_print.assert_called_with(expected_output)

def test_start_raises_error_if_already_running():
    timer = Timer()
    timer._start_time = time.perf_counter()
    with pytest.raises(TimerError):
        timer.start()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer_start_0_test_edge_cases
codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_edge_cases.py:32:23: E0602: Undefined variable 'TimerError' (undefined-variable)


"""
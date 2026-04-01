
import pytest
from codetiming import Timer
from unittest.mock import patch, MagicMock

@pytest.fixture
def timer():
    return Timer()

def test_stop_invalid_input(timer):
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
    assert str(excinfo.value) == "Timer is not running. Use .start() to start it"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer_stop_4_test_invalid_input
codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_4_test_invalid_input.py:11:23: E0602: Undefined variable 'TimerError' (undefined-variable)


"""
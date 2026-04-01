
import pytest
from codetiming import TimerError
from unittest.mock import patch, MagicMock

@pytest.fixture
def timer():
    return Timer()

def test_stop_with_no_start(timer):
    with pytest.raises(TimerError) as excinfo:
        timer.stop()
    assert str(excinfo.value) == "Timer is not running. Use .start() to start it"

@patch('time.perf_counter', return_value=10.0)
def test_stop_with_mocked_time(mock_perf_counter, timer):
    timer._start_time = 5.0
    with patch.object(timer, 'logger', new=MagicMock()):
        assert timer.stop() == 5.0
        assert timer._start_time is None
        assert timer.last == 5.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timer_Timer_stop_1_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timer_Timer_stop_1_test_edge_case.py:8:11: E0602: Undefined variable 'Timer' (undefined-variable)


"""
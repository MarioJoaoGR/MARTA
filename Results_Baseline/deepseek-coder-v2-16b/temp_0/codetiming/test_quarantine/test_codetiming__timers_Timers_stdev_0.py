
# Module: codetiming._timers
import pytest
from codetiming import Timer
import time
import math
import statistics

# Test initialization with default name
def test_timer_init_default_name():
    timer = Timer()
    assert timer.name == "default_timer"

# Test initialization with custom name
def test_timer_init_custom_name():
    timer = Timer(name="CustomName")
    assert timer.name == "CustomName"

# Test starting the timer
def test_timer_start():
    timer = Timer()
    timer.start()
    time.sleep(0.1)  # Let's wait a bit to ensure there is some elapsed time
    assert timer.elapsed() >= 0.1

# Test stopping the timer without starting it first
def test_timer_stop_without_start():
    timer = Timer()
    with pytest.raises(TimerError):
        timer.stop()

# Test calculating standard deviation of timings
def test_stdev():
    timer = Timer()
    timer._timings['timing_name'] = [1.0, 2.0, 3.0]
    assert math.isnan(timer.stdev('other_name'))  # other_name should not exist
    std_dev = timer.stdev('timing_name')
    assert std_dev == statistics.stdev([1.0, 2.0, 3.0])

# Test calculating standard deviation with less than two values
def test_stdev_less_than_two_values():
    timer = Timer()
    timer._timings['timing_name'] = [1.0]
    assert math.isnan(timer.stdev('timing_name'))

# Test handling of KeyError when the timing name does not exist
def test_stdev_keyerror():
    timer = Timer()
    with pytest.raises(KeyError):
        timer.stdev('non_existent_name')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:24:11: E1101: Instance of 'Timer' has no 'elapsed' member (no-member)
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:29:23: E0602: Undefined variable 'TimerError' (undefined-variable)
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:35:4: E1101: Instance of 'Timer' has no '_timings' member (no-member)
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:36:22: E1101: Instance of 'Timer' has no 'stdev' member (no-member)
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:37:14: E1101: Instance of 'Timer' has no 'stdev' member (no-member)
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:43:4: E1101: Instance of 'Timer' has no '_timings' member (no-member)
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:44:22: E1101: Instance of 'Timer' has no 'stdev' member (no-member)
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0.py:50:8: E1101: Instance of 'Timer' has no 'stdev' member (no-member)

"""
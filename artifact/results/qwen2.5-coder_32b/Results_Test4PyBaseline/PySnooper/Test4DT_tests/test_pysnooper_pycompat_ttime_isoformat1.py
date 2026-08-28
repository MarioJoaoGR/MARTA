
from pysnooper.pycompat import time_isoformat
from datetime import time

def test_time_isoformat_default():
    t = time(12, 34, 56, 789012)
    assert time_isoformat(t) == '12:34:56.789012'

def test_time_isoformat_microseconds():
    t = time(9, 8, 7, 654321)
    assert time_isoformat(t, timespec='microseconds') == '09:08:07.654321'

def test_time_isoformat_zero_microseconds():
    t = time(23, 59, 59)
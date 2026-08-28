
import pytest
from datetime import time as datetime_time

def time_isoformat(time, timespec='microseconds'):
    assert isinstance(time, datetime_time)
    if timespec != 'microseconds':
        raise NotImplementedError
    result = '{:02d}:{:02d}:{:02d}.{:06d}'.format(
        time.hour, time.minute, time.second, time.microsecond
    )
    assert len(result) == 15
    return result

def test_valid_case():
    t = datetime_time(12, 34, 56, 789012)
    expected_output = '12:34:56.789012'
    assert time_isoformat(t) == expected_output

def test_edge_case_zero_microseconds():
    t = datetime_time(23, 59, 59)
    expected_output = '23:59:59.000000'
    assert time_isoformat(t) == expected_output

def test_invalid_timespec():
    t = datetime_time(10, 20, 30)
    with pytest.raises(NotImplementedError):
        time_isoformat(t, timespec='seconds')

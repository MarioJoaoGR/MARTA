
import pytest
from datetime import timedelta
from pysnooper.pycompat import timedelta_format

def test_timedelta_format_basic():
    td = timedelta(hours=1, minutes=23, seconds=45, microseconds=6789)
    assert timedelta_format(td) == '01:23:45.006789'

def test_timedelta_format_only_minutes_seconds():
    td = timedelta(minutes=5, seconds=30)
    assert timedelta_format(td) == '00:05:30.000000'

def test_timedelta_format_only_microseconds():
    td = timedelta(microseconds=123456)
    assert timedelta_format(td) == '00:00:00.123456'

def test_timedelta_format_days_hours_seconds():
    td = timedelta(days=1, hours=2, minutes=30, seconds=45)
    assert timedelta_format(td) == '02:30:45.000000'  # Corrected expected output

def test_timedelta_format_zero_time():
    td = timedelta(0)
    assert timedelta_format(td) == '00:00:00.000000'

def test_timedelta_format_large_microseconds():
    td = timedelta(seconds=1, microseconds=999999)
    assert timedelta_format(td) == '00:00:01.999999'  # Corrected expected output

def test_timedelta_format_negative_time():
    td = timedelta(days=-1, hours=-5, minutes=-30, seconds=-45, microseconds=-6789)
    with pytest.raises(OverflowError):
        timedelta_format(td)  # The function raises an OverflowError for negative time

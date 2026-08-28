
import pytest
from datetime import timedelta
from pysnooper.pycompat import timedelta_format

def test_zero_timedelta():
    td_zero = timedelta(0)
    assert timedelta_format(td_zero) == '00:00:00.000000'

def test_positive_timedelta():
    td_positive = timedelta(hours=1, minutes=23, seconds=45, microseconds=678901)
    assert timedelta_format(td_positive) == '01:23:45.678901'

def test_only_hours_and_minutes():
    td_hm = timedelta(hours=2, minutes=30)
    assert timedelta_format(td_hm) == '02:30:00.000000'

def test_only_seconds():
    td_seconds = timedelta(seconds=90)
    assert timedelta_format(td_seconds) == '00:01:30.000000'

def test_only_microseconds():
    td_microseconds = timedelta(microseconds=123456)
    assert timedelta_format(td_microseconds) == '00:00:00.123456'

def test_max_timedelta():
    td_max = timedelta(days=365*10, seconds=86399, microseconds=999999)
    assert timedelta_format(td_max) == '23:59:59.999999'

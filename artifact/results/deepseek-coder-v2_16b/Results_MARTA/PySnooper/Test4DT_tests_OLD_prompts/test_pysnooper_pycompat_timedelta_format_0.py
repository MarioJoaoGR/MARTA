
import pytest
from datetime import timedelta, time as datetime_time
import pysnooper.pycompat as pycompat

def test_timedelta_format_positive():
    td = timedelta(hours=12, minutes=34, seconds=56, microseconds=7890)
    assert pycompat.timedelta_format(td) == '12:34:56.007890'

def test_timedelta_format_zero():
    td = timedelta()
    assert pycompat.timedelta_format(td) == '00:00:00.000000'

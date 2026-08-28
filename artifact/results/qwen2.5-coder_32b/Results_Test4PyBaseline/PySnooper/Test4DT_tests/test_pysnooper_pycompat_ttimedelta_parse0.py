
import pytest
from pysnooper.pycompat import timedelta_parse
import datetime as datetime_module

def test_timedelta_parse_full_format():
    td = timedelta_parse("01:30:45.678901")
    assert td == datetime_module.timedelta(hours=1, minutes=30, seconds=45, microseconds=678901)

def test_timedelta_parse_no_microseconds():
    td = timedelta_parse("23:59:59.0")
    assert td == datetime_module.timedelta(hours=23, minutes=59, seconds=59)

def test_timedelta_parse_zero_padding():
    td = timedelta_parse("00:05:00.123456")
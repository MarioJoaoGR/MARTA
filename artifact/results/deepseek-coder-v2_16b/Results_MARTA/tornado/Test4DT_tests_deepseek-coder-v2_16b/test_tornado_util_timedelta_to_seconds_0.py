
import pytest
from datetime import timedelta
from tornado.util import timedelta_to_seconds

def test_timedelta_to_seconds_one_hour():
    td = timedelta(hours=1)
    assert timedelta_to_seconds(td) == 3600.0


def test_timedelta_to_seconds_one_minute():
    td = timedelta(minutes=1)
    assert timedelta_to_seconds(td) == 60.0
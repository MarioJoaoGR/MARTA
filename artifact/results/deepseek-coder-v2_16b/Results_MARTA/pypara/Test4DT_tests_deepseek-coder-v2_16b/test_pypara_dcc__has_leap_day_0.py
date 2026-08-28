
import pytest
import datetime
from pypara.dcc import _has_leap_day

def test_valid_range_with_leap_days():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    assert _has_leap_day(start_date, end_date) == True

def test_valid_range_without_leap_days():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    assert _has_leap_day(start_date, end_date) == False


import pytest
from pypara.dcc import _has_leap_day
import datetime
from unittest.mock import patch

def test_has_leap_day():
    # Test case 1: Range includes leap days (2020-2024)
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    assert _has_leap_day(start_date, end_date) == True

def test_no_leap_day():
    # Test case 2: Range does not include leap days (2021)
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    assert _has_leap_day(start_date, end_date) == False

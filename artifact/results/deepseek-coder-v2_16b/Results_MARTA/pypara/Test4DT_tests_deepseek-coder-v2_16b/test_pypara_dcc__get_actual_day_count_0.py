
import pytest
from pypara.dcc import _get_actual_day_count
import datetime

def test_get_actual_day_count_same_date():
    start_date = datetime.date(2017, 1, 1)
    end_date = datetime.date(2017, 1, 1)
    assert _get_actual_day_count(start_date, end_date) == 0

def test_get_actual_day_count_one_day():
    start_date = datetime.date(2017, 1, 1)
    end_date = datetime.date(2017, 1, 2)
    assert _get_actual_day_count(start_date, end_date) == 1

def test_get_actual_day_count_multiple_days():
    start_date = datetime.date(2017, 1, 1)
    end_date = datetime.date(2017, 1, 5)
    assert _get_actual_day_count(start_date, end_date) == 4

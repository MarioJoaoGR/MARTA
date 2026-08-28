
import pytest
import datetime
from pypara.dcc import _get_actual_day_count

# Test case for counting days between two specific dates
def test_get_actual_day_count_normal():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 1, 5)
    assert _get_actual_day_count(start_date, end_date) == 4

# Test case for counting days between the same date for a single-day range
def test_get_actual_day_count_same_date():
    same_date = datetime.date(2023, 1, 1)
    assert _get_actual_day_count(same_date, same_date) == 0

# Test case for counting days between two dates where end date is before start date
def test_get_actual_day_count_negative():
    early_end_date = datetime.date(2022, 12, 31)
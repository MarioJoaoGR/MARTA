# Module: pypara.dcc
import datetime
import pytest
from pypara.dcc import _has_leap_day

# Example 1: A range that includes leap days
def test_range_includes_leap_days():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    assert _has_leap_day(start_date, end_date) == True

# Example 2: A range that does not include leap days
def test_range_does_not_include_leap_days():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    assert _has_leap_day(start_date, end_date) == False

# Example 3: A range that includes a leap day within the specified dates
def test_range_includes_a_leap_day():
    start_date = datetime.date(2020, 2, 28)
    end_date = datetime.date(2021, 3, 1)
    assert _has_leap_day(start_date, end_date) == True

# Test with a range that does not include any leap days
def test_range_does_not_include_any_leap_days():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 12, 31)
    assert _has_leap_day(start_date, end_date) == False

# Test with a range that starts and ends on leap days
def test_range_starts_and_ends_on_leap_days():
    start_date = datetime.date(2020, 2, 29)
    end_date = datetime.date(2024, 2, 29)
    assert _has_leap_day(start_date, end_date) == True

# Test with a range that includes multiple leap days
def test_range_includes_multiple_leap_days():
    start_date = datetime.date(2016, 1, 1)
    end_date = datetime.date(2020, 12, 31)
    assert _has_leap_day(start_date, end_date) == True

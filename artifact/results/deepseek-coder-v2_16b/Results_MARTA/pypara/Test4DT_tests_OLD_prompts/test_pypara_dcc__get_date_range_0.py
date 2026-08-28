
import pytest
from pypara.dcc import _get_date_range
import datetime

def test_valid_input():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 1, 10)
    date_range = list(_get_date_range(start_date, end_date))
    assert len(date_range) == (end_date - start_date).days
    for i in range((end_date - start_date).days):
        assert date_range[i] == start_date + datetime.timedelta(days=i)

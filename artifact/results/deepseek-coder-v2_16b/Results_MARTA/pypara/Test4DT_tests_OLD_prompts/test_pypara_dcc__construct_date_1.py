
import pytest
from datetime import date, timedelta
from pypara.dcc import _construct_date

def test_valid_date():
    valid_date = _construct_date(2023, 10, 31)
    assert isinstance(valid_date, date), "Expected a datetime.date object"
    assert valid_date == date(2023, 10, 31)

def test_invalid_month():
    with pytest.raises(ValueError):
        _construct_date(2023, 13, 1)

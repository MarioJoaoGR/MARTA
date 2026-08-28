
import pytest
import datetime
from pypara.dcc import _construct_date

def test_valid_date():
    valid_date = _construct_date(2023, 10, 31)
    assert isinstance(valid_date, datetime.date), "Expected a datetime.date object"
    assert valid_date == datetime.date(2023, 10, 31), "Expected the constructed date to be 2023-10-31"

def test_invalid_month():
    with pytest.raises(ValueError):
        _construct_date(2023, 13, 1)


def test_negative_year():
    with pytest.raises(ValueError):
        _construct_date(-1, 1, 1)

def test_negative_month():
    with pytest.raises(ValueError):
        _construct_date(2023, -1, 1)

def test_negative_day():
    with pytest.raises(ValueError):
        _construct_date(2023, 1, -1)
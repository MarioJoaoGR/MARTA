
import datetime
import pytest
from pypara.dcc import _construct_date

# Test cases for valid dates
def test_valid_date():
    constructed_date = _construct_date(2023, 10, 31)
    assert isinstance(constructed_date, datetime.date), "Expected a datetime.date object"
    assert constructed_date == datetime.date(2023, 10, 31)

# Test cases for invalid year
def test_invalid_year():
    with pytest.raises(ValueError) as excinfo:
        _construct_date(-500, 10, 31)
    assert str(excinfo.value) == "year, month and day must be greater than 0."

# Test cases for invalid month
def test_invalid_month():
    with pytest.raises(ValueError) as excinfo:
        _construct_date(2023, -1, 31)
    assert str(excinfo.value) == "year, month and day must be greater than 0."

# Test cases for invalid day
def test_invalid_day():
    with pytest.raises(ValueError) as excinfo:
        _construct_date(2023, 10, -1)
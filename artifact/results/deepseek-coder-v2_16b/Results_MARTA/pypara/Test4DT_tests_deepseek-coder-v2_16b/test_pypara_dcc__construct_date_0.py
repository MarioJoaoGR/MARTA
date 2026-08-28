
import pytest
from pypara.dcc import _construct_date
import datetime

def test_valid_date():
    # Test a valid date construction
    year, month, day = 2023, 10, 31
    expected_date = datetime.date(year, month, day)
    assert _construct_date(year, month, day) == expected_date

def test_invalid_month():
    # Test invalid month value
    year, month, day = 2023, 13, 1
    with pytest.raises(ValueError):
        _construct_date(year, month, day)

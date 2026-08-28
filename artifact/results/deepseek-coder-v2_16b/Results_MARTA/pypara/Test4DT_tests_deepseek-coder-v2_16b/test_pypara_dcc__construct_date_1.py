
import pytest
import datetime
from pypara.dcc import _construct_date

def test_valid_date():
    year, month, day = 2023, 10, 31
    expected_date = datetime.date(year, month, day)
    assert _construct_date(year, month, day) == expected_date

def test_invalid_month():
    with pytest.raises(ValueError):
        year, month, day = 2023, 13, 1
        _construct_date(year, month, day)

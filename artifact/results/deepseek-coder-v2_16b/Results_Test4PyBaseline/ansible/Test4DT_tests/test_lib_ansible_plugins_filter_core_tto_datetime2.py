
# Module: ansible.plugins.filter.core
import pytest
import datetime
from ansible.plugins.filter.core import to_datetime

# Test cases for invalid inputs
def test_invalid_date_string():
    with pytest.raises(ValueError):
        to_datetime("invalid date string")

def test_invalid_format():
    with pytest.raises(ValueError):
        to_datetime("2023-04-15 12:30:00", format="invalid format")

# Test cases for the function `to_datetime` with default and custom formats
def test_default_format():
    result = to_datetime("2023-04-15 12:30:00")
    assert isinstance(result, datetime.datetime)
    assert result == datetime.datetime(2023, 4, 15, 12, 30, 0)

def test_custom_format():
    result = to_datetime("15/04/2023 12:30", format="%d/%m/%Y %H:%M")
    assert isinstance(result, datetime.datetime)
    assert result == datetime.datetime(2023, 4, 15, 12, 30)

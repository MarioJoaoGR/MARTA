
import pytest
from datetime import date, datetime
from typesystem.formats import DateFormat

# Test for valid input
def test_valid_input():
    df = DateFormat()
    today = date.today()
    result = df.serialize(today)
    assert isinstance(result, str), "Expected a string representation of the date"
    assert len(result) == 10, "Expected ISO format with year-month-day"

# Test for None input
def test_none_input():
    df = DateFormat()
    invalid_date = None
    result = df.serialize(invalid_date)
    assert result is None, "Expected None for non-date input"

# Test for invalid input type
def test_invalid_input():
    df = DateFormat()
    invalid_obj = 'not a date'
    with pytest.raises(AssertionError):
        df.serialize(invalid_obj)

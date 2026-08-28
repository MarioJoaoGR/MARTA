
import pytest
from datetime import date
from typesystem.formats import DateFormat

# Test for a valid datetime.date object
def test_valid_date():
    date_format = DateFormat()
    today = date.today()
    assert date_format.is_native_type(today) is True, "Expected a valid datetime.date to be recognized as such"

# Test for an invalid string representing a date
def test_invalid_string():
    date_format = DateFormat()
    today_str = 'not-a-real-date'
    assert date_format.is_native_type(today_str) is False, "Expected an invalid string to be recognized as not a native type"

# Test handling of None input
def test_none_input():
    date_format = DateFormat()
    none_value = None
    assert date_format.is_native_type(none_value) is False, "Expected None to be handled and recognized as not a datetime.date"

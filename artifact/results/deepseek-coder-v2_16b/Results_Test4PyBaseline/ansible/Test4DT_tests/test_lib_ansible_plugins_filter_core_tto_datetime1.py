
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

# Test cases for handling 'now' and 'preserve' inputs
def test_handle_now():
    # Assuming the function returns a sentinel value specific to the context when 'formatted_time' is 'now'
    with pytest.raises(ValueError):
        to_datetime('now')

def test_handle_preserve():
    with pytest.raises(ValueError):
        to_datetime('preserve')

# Test cases for error handling with incorrect formats or inputs
def test_error_handling_invalid_format():
    with pytest.raises(ValueError):
        to_datetime("2023-04-15 12:30:00", format="invalid format")

def test_error_handling_missing_time_component():
    with pytest.raises(ValueError):
        to_datetime("2023-04-15")  # Missing hours, minutes, and seconds

# Test cases for edge cases or specific scenarios
def test_edge_case_midnight():
    result = to_datetime("2023-04-15 00:00:00")
    assert isinstance(result, datetime.datetime)
    assert result == datetime.datetime(2023, 4, 15, 0, 0, 0)

def test_edge_case_leap_year():
    result = to_datetime("2024-02-29 12:30:00")
    assert isinstance(result, datetime.datetime)
    assert result == datetime.datetime(2024, 2, 29, 12, 30, 0)

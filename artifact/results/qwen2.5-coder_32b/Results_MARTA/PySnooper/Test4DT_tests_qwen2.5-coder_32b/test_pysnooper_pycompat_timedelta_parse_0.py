
import pytest
from datetime import timedelta as datetime_module
from pysnooper.pycompat import timedelta_parse


def test_valid_input_with_full_microseconds():
    # Test a valid input string with full microseconds
    result = timedelta_parse('01:23:45.678901')
    expected = datetime_module(seconds=5025, microseconds=678901)
    assert result == expected


def test_valid_input_zero_hours_minutes():
    # Test a valid input string with zero hours and minutes
    result = timedelta_parse('00:00:00.999999')
    expected = datetime_module(microseconds=999999)
    assert result == expected

def test_invalid_input_negative_hours():
    # Test invalid input with negative hours
    with pytest.raises(ValueError):
        timedelta_parse('-01:23:45')

def test_invalid_input_negative_minutes():
    # Test invalid input with negative minutes
    with pytest.raises(ValueError):
        timedelta_parse('01:-23:45')

def test_invalid_input_negative_seconds():
    # Test invalid input with negative seconds
    with pytest.raises(ValueError):
        timedelta_parse('01:23:-45')

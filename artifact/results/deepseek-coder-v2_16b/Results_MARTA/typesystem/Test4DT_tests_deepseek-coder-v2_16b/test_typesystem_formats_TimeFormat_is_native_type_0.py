
import pytest
import datetime
from typesystem.formats import TimeFormat

# Test for valid time instance
def test_valid_time_instance():
    time_format = TimeFormat()
    valid_time = datetime.time(12, 30, 0)
    assert time_format.is_native_type(valid_time) == True

# Test for invalid string
def test_invalid_string():
    time_format = TimeFormat()
    invalid_str = "not-a-real-time"
    assert time_format.is_native_type(invalid_str) == False

# Test for None input handling
def test_none_input():
    time_format = TimeFormat()
    none_value = None
    assert time_format.is_native_type(none_value) == False

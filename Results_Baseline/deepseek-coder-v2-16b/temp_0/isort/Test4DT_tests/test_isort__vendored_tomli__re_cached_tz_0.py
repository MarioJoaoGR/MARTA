
from datetime import timedelta, timezone

import pytest

from isort._vendored.tomli._re import cached_tz


# Test cases for the cached_tz function
def test_cached_tz_positive():
    result = cached_tz("1", "30", "+")
    assert isinstance(result, timezone), f"Expected a timezone object, but got {type(result)}"
    assert str(result) == "UTC+01:30", f"Expected UTC+01:30, but got {str(result)}"

def test_cached_tz_negative():
    result = cached_tz("2", "45", "-")
    assert isinstance(result, timezone), f"Expected a timezone object, but got {type(result)}"
    assert str(result) == "UTC-02:45", f"Expected UTC-02:45, but got {str(result)}"

def test_cached_tz_with_strings():
    hour_str = "1"
    minute_str = "30"
    sign_str = "+"
    result = cached_tz(hour_str, minute_str, sign_str)
    assert isinstance(result, timezone), f"Expected a timezone object, but got {type(result)}"
    assert str(result) == "UTC+01:30", f"Expected UTC+01:30, but got {str(result)}"

def test_cached_tz_with_integers():
    hour_int = 1
    minute_int = 30
    sign_str = "+"
    result = cached_tz(str(hour_int), str(minute_int), sign_str)
    assert isinstance(result, timezone), f"Expected a timezone object, but got {type(result)}"
    assert str(result) == "UTC+01:30", f"Expected UTC+01:30, but got {str(result)}"

def test_cached_tz_negative_values():
    hour_str = "-2"
    minute_str = "45"
    sign_str = "-"
    result = cached_tz(hour_str, minute_str, sign_str)
    assert isinstance(result, timezone), f"Expected a timezone object, but got {type(result)}"
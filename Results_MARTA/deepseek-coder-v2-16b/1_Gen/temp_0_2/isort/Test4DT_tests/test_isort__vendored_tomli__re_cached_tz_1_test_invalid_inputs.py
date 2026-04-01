
import pytest
from datetime import timezone, timedelta

def cached_tz(hour_str: str, minute_str: str, sign_str: str) -> timezone:
    sign = 1 if sign_str == "+" else -1
    return timezone(
        timedelta(
            hours=sign * int(hour_str),
            minutes=sign * int(minute_str),
        )
    )

def test_invalid_inputs():
    with pytest.raises(ValueError):
        cached_tz("5", "30", "+")  # Valid input, should not raise an error
        cached_tz("25", "60", "+")  # Invalid hour and minute values, should raise an error
        cached_tz("5", "30", "-1")  # Invalid sign value, should raise an error
        cached_tz("five", "thirty", "+")  # Non-integer hour and minute strings, should raise an error
        cached_tz("5", "30", "invalid_sign")  # Invalid sign string, should raise an error

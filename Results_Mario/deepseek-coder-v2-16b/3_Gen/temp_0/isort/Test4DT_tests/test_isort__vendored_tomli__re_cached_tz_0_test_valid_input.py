
from datetime import timedelta, timezone

import pytest


def cached_tz(hour_str: str, minute_str: str, sign_str: str) -> timezone:
    """
    Generate a timezone object based on the provided hour, minute, and sign strings.
    
    Parameters:
        hour_str (str): A string representing the hour component of the timezone offset.
                        Must be an integer between 0 and 23 inclusive.
        minute_str (str): A string representing the minute component of the timezone offset.
                          Must be an integer between 0 and 59 inclusive.
        sign_str (str): A string indicating the sign of the timezone offset, either "+" or "-".
    
    Returns:
        timezone: A Python `timezone` object representing the specified timezone offset.
    
    Examples:
        >>> cached_tz("1", "30", "+")
        <UTC+01:30>
        
        >>> cached_tz("2", "45", "-")
        <UTC-02:45>
        
        To use this function, simply call it with the appropriate strings for hour, minute, and sign. The returned object can be used in various datetime operations that require timezone information.
    """
    sign = 1 if sign_str == "+" else -1
    return timezone(
        timedelta(
            hours=sign * int(hour_str),
            minutes=sign * int(minute_str),
        )
    )

def test_valid_input():
    # Test valid input for hour, minute, and sign strings
    assert cached_tz("1", "30", "+") == timezone(timedelta(hours=1, minutes=30))
    assert cached_tz("2", "45", "-") == timezone(timedelta(hours=-2, minutes=-45))
    assert cached_tz("0", "0", "+") == timezone(timedelta(hours=0, minutes=0))
    assert cached_tz("12", "0", "+") == timezone(timedelta(hours=12, minutes=0))
    assert cached_tz("6", "30", "-") == timezone(timedelta(hours=-6, minutes=-30))
